import os
import fnmatch
import shutil
import csv
import pandas as pd
import numpy as np
BaseDir = '/home/jsteffen'
VisitFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/99012345/2018_Dec_12_1044_V001')
subid = '99012345'
TaskTag = 'DMS_'


def ReadFile(VisitFolder, subid, TaskTag):
    # Find the file that matches the TaskTag
    # If multiple CSV files are found then the user is prompted to pick one.
    # Un selected files are renamed with XXX at their beginning.
    # The next time this program is run on this folder there will now only be one file 
    # available and the user will not be prompted again
    Data = []
    # List all files in the visit folder
    ll = os.listdir(VisitFolder)
    # create the string you are looking for which is a combo of the subid and the task name
    SearchString = subid + '_' + TaskTag
    matching = fnmatch.filter(ll,SearchString+'*.csv')
    # It is possible that there are multipel files with similar names.
    # The following asks the user for the correct one and then renames the others
    count = 1
    if len(matching) > 1:
        # There are more than one file!
        print('There are multiple files found for %s'%(SearchString))
        for i in matching:
            # print the name and size of files
            SizeOfFile = np.round(os.stat(os.path.join(VisitFolder,matching[0])).st_size/1048)
            print('\t%d) %s, size = %0.0f kB'%(count, i,SizeOfFile))
            count += 1
        sel = input('Which one should be kept?  ')
        SelectedFile = matching[int(sel)-1]
        # Rename the unselected files so they will hopefully not be selected the next time!
        count = 1
        for i in matching:
            if not count == int(sel):
                OutName = 'XXX_' + i
                print(OutName)
                shutil.move(os.path.join(VisitFolder,i), os.path.join(VisitFolder, OutName))
            count += 1    
    elif len(matching) == 1:
        SelectedFile= matching[0]
    else:
        SelectedFile = False
        print('Did not find any files!!!')
    if SelectedFile != False:
        # Now open the file
        InputFile = os.path.join(VisitFolder, SelectedFile)
        # Read whole file into a dataframe
        # Note, in order for the data to be read as a dataframe all columns need to have headings.
        # If not an error is thrown
        Data = pd.read_csv(InputFile)
        # If the data is to be read into a big list use this:
        #    fid = open(InputFile, 'r')
        #    Data = csv.reader(fid)
        #    Data = list(Data)
    return Data
    
def ProcessVSTMBlock(Data):
    Out = {}
    # If there is an entry that is -99 it is a missing value and needs to be changed to NaN
    Data = Data.replace(-99, NaN)
    TabNResp = pd.pivot_table(Data, values = 'Corr', index = 'Load', aggfunc = 'count')
    TabRT = pd.pivot_table(Data, values = 'RT', index = 'Load', aggfunc = np.mean)    
    TabAcc = pd.pivot_table(Data, values = 'Corr', index = 'Load', aggfunc = np.mean)    
    Out['NResp'] = TabNResp
    Out['RT'] = TabRT
    Out['Acc'] = TabAcc
    return Out
    
def ProcessDMSBlock(Data):
    Out = {}
    # This finds the number of trials for which a response was made
    TabNResp = pd.pivot_table(Data, values = 'resp.corr', index = 'Load', aggfunc = 'count')
    # What is the average RT broken by load
    TabRT = pd.pivot_table(Data, values = 'resp.rt', index = 'Load', aggfunc = np.mean)    
    # What is the average accuracy
    TabAcc = pd.pivot_table(Data, values = 'resp.corr', index = 'Load', aggfunc = np.mean)    
    Out['NResp'] = TabNResp
    Out['RT'] = TabRT
    Out['Acc'] = TabAcc
    return Out    
    
def ProcessPattComp(Data):
    # First remove the practice rows from the data file
    Data_Run = Data[Data['Run.thisN'].notnull()]
    Out = {}
    Out['NResp'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Difficulty', aggfunc = 'count')
    Out['RT'] = pd.pivot_table(Data_Run, values = 'resp.rt', index = 'Difficulty', aggfunc = np.mean)
    Out['Acc'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Difficulty', aggfunc = np.mean)
    return Out
    
def ProcessAntonym(Data):
    # First remove the practice rows from the data file
    Data_Run = Data[Data['Trials.thisN'].notnull()]
    Out = {}
    Out['NResp'] = Data_Run['resp.corr'].count()
    Out['Acc'] = Data_Run['resp.corr'].mean()    
    Out['RT'] = Data_Run['resp.rt'].mean()
    return Out

def CheckWCSTErrors(CurrentRow, CurrentRule, PreviousRule):
    RuleList = []
    RuleList.append('Color')
    RuleList.append('Shape')
    RuleList.append('Count')   
    # Make this so it gets passed one row at a time because passing the entire DF is too much
    Sel = CurrentRow['Card%02d%s'%(int(CurrentRow['Card']),RuleList[CurrentRule])]
    Probe = CurrentRow['Probe%s'%(RuleList[CurrentRule])]
    # Do they match?
    Match = Sel == Probe
    Error = True
    PersError = False
    if Match:
        Error = False
    elif not Match:
    # If an error is made does it match the previous rule?
        Error = True
        PreviousProbe = CurrentRow['Probe%s'%(RuleList[PreviousRule])]
        if Sel == PreviousProbe:
            PersError = True
    
    return Error, PersError, Sel, Probe

def ProcessWCST(Data):
    # Remove the practice trials
    FindTask = DataWCST[DataWCST['TrialNum'].str.match('TrialNum')].index[0]
    Data_Run = DataWCST.iloc[FindTask+1:]
    PreviousRule = -1
    # Start counters for the number of errors
    NumTrials = 0
    NumErrors = 0
    NumPersErrors = 0
    # Cycle over each data row
    for i, CurrentRow in Data_Run.iterrows():
        NumTrials += 1
        # extrcat the current rule
        CurrentRule = int(CurrentRow['Rule'])
        if (PreviousRule != -1) and (CurrentRule != LastTrialRule):
            # If previous rule is -1 then leave it
            # if the current rule is different from the rule on the last trial, then change the previous rule
            # Then update the previous rule because the rules have changed
            PreviousRule = LastTrialRule
        # Check for errors on this row
        (Error, PersError, Sel, Probe) = CheckWCSTErrors(CurrentRow, CurrentRule, PreviousRule)
        # update error counters
        if Error: 
            NumErrors += 1
        if PersError:
            NumPersErrors += 1
        LastTrialRule = CurrentRule
        #print('%d, CurrentRule = %d, Probe = %d, Sel = %d, Error = %r, PerError = %r'%(i, CurrentRule, Probe, Sel, Error, PersError))    
    #print('Number of Trials: %d, Number of Errors: %d, Number Pers Errors: %d'%(NumTrials, NumErrors, NumPersErrors))
    Out = {}
    Out['NTrials'] = NumTrials
    Out['NErrors'] = NumErrors
    Out['NPersErrors'] = NumPersErrors
    return Out