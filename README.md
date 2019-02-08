# CognitiveTasks

This is a set of code for administering a few cognitive tasks. 
The code is all written in Psychopy http://www.psychopy.org/. Psychopy needs ot be installed first. Also note that as of right now Psychopy uses python 2.7.

When the tasks are run data files will be created. These will be placed in a top level folder called data. If this folder does not exist it will be created. Within this data folder one folder will be created for each participant ID. By default the participant ID is 9999999. Every data file is named with the format: 
`[Task Name]_[Participant ID]_[Year]_[Month]_[Day]_[Time].csv`



## GUIs
There are two GUIs for task delivery.

### NCM_Experiment.py
This is a GUI which runs the FACE task and the DMS task and was used for teh behavioral aspect of this study. There are three versions of these tasks, as represented by the different buttons. The first is the demonstration of the task and is used for training of the participant about the aspects and mechanisms of the tasks.

The second is the staircase adaptive difficulty version of the two tasks. The third, is a block based version of the task using the estimated cognitive capacity from the staircase administration of the task. 

### NCM_fMRI_GUI.py
This is a GUI which runs the DMS task and the WORD tasks and will be used for the MRI aspect of this experiment.

This file looks for a file named BehavioralDataFolder.py in the folder ConfigFiles. This file contains a variable name of the location for all the behavioral data to be saved to. If this file does not exist, does not contain the expected info or contains the path of a folder that does not exist, a dialog box asks the user to select a folder. Once selected, this file is updated. Therefore, the user is only prompted once for this folder.

## Tasks
### Degraded Face Matching (FACE) Task
This experiment is  trial based where image pairs are presented and the participant determines whether the two images are of the same person. Face pairs are presented for 2500 milliseconds with a 500 ms intertrial interval in blocks of twelve trials each. Within a block of trials, all face pairs will have the same level of degradation. Blocks will be separated by 5 seconds of rest where the participant views a fixation cross-hair at the center of the screen. Successive blocks will present images with larger levels of degradation. Responses are recorded via a keyboard press.

Degradation of the faces is performed by adding noise to each image. This experiment used phase-scrambled noise by randomizing the phase component of the image in the frequency domain (Oppenheim & Lim, 1981; Thomson, 1999). This process preserves the frequency component of the image, while making the noise image. Different levels of degradation are created using different additive proportions of image and noise so that the total is always 100%. For example, an image with a noise level of ‘40’ is calculated as: 0.6*image + 0.4*noise. 

Faces for this study are from the Karolinska Directed Emotional Faces (KDEF), which were developed for use in psychological and medical research (Lundqvist, Flykt, & Öhman, 1998). This is a set of 4900 photographs of 70 different people displaying various emotional expressions. Images were taken from various perspectives around the person. For this experiment, only neutral expressions are used. Images on the left of the screen will be displayed with the face turned towards the center of the screen. Images on the right of the screen will also be displayed with the face turned towards the center of the screen. In this manner, even if the two images are of the same person they are not the same image. This design attempts to ensure the participant matches the images based on the person and not on other spatial aspects of the images.

### Delayed Match to Sample, Letters

This task uses visually presented letter stimuli (B. Rypma et al., 1999; Sternberg, 1966) and is a standard and widely used task with relatively minor adaptations from previous use with the task (Hillary et al., 2003; Steffener, Brickman, Rakitin, Gazes, & Stern, 2009; Stern et al., 2008). This experiment is trial based, where each trial is comprised of three parts. A trial begins with the presentation of letters in a 3x3 grid on the screen for 2.5 seconds. The participant is to study and remember the letters. After the letters are removed from the screen, a green crosshair is presented for 3.5 seconds. During this time, the participant is to remember the studied letters. Finally, a single probe letter is presented for 2.5 seconds. During this time window, participants are to determine whether or not they recognize the probe letter as one that they studied for this trial. Responses are recorded via a keyboard press. This task is presented in blocks of six trials separated by 16 seconds of rest where the participant views a white fixation cross-hair at the center of the screen. Successive blocks will have incrementally larger task demands, i.e. more letters to study per trial. Task demands range from one to eight letters. The last three seconds of the rest blocks have a countdown of 3-2-1 presented at one second per number.

The task demands for this task are manipulated based on the number of letters to study at each trial. There are eight levels of task demand possible. When the load level for a trial is less than eight, the remaining locations in the grid are filled with asterisks. Only consonant letters (except “W”) are used in order to minimize word forming of the studied letters. No letters in one trial can contain any of the letters used in the previous trial. Letters are not presented in alphabetical order. Letters to study are presented in uppercase while probe letters are in lowercase. This design ensures letters are not being matched based on visual features. 

### Semantic Richness

This is an event-related task presenting words. The task has 60 words and takes approximately 8:30 minutes. The ITI is jittered and the ITI durations and the trial order is optimized based on thousands of simulations. The simulations identify the Gamma distribution of ITIs that minimize the BOLD response required to significantly detect task related signal change. This optimization used multiple contrasts and the optimization aimed to find the smallest average BOLD signal required across all contrasts of interest. 

### Delayed Match to Sample, Spatial


