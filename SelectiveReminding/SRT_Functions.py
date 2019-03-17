def PresentWordSelection(WordListObjects, trialClock, mouse, event, endExpNow, win):
    
    from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
    
    SelectedColor = 'blue'                                
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_text = []
    gotValidClick = False  # until a click is received

    # Set word colors back to white
    for i in WordListObjects:
        i.setColor('white', 'rgb255')
        
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [mouse, WordListObjects[0], WordListObjects[1], WordListObjects[2], WordListObjects[3], WordListObjects[4], WordListObjects[5],WordListObjects[6], WordListObjects[7], WordListObjects[8], WordListObjects[9], WordListObjects[10], WordListObjects[11],WordListObjects[12],WordListObjects[13],WordListObjects[14],WordListObjects[15],WordListObjects[16],WordListObjects[17],key_resp_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------

    CorrectRecog = 0
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(trialClock.getTime())
                    # check if the mouse was inside our 'clickable' objects
                    for obj in WordListObjects:
                                        # text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_text.append(obj.text)
                    # HERE is where accuracy is assessed
                    for obj in WordListObjects:#[text3,text5,text6,text7,text14, text15, text16, text17, text18, text22, text23, text24]:
                        if obj.contains(mouse):
                            CorrectRecog += 1
        # *text1* updates
        if t >= 0.0 and WordListObjects[0].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[0].tStart = t
            WordListObjects[0].frameNStart = frameN  # exact frame index
            WordListObjects[0].setAutoDraw(True)
        # *text2* updates
        if t >= 0.0 and WordListObjects[1].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[1].tStart = t
            WordListObjects[1].frameNStart = frameN  # exact frame index
            WordListObjects[1].setAutoDraw(True)
         # *text2* updates
        if t >= 0.0 and WordListObjects[2].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[2].tStart = t
            WordListObjects[2].frameNStart = frameN  # exact frame index
            WordListObjects[2].setAutoDraw(True)
        # *text2* updates
        if t >= 0.0 and WordListObjects[3].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[3].tStart = t
            WordListObjects[3].frameNStart = frameN  # exact frame index
            WordListObjects[3].setAutoDraw(True)
        # *text2* updates
        if t >= 0.0 and WordListObjects[4].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[4].tStart = t
            WordListObjects[4].frameNStart = frameN  # exact frame index
            WordListObjects[4].setAutoDraw(True)           # *text2* updates
        if t >= 0.0 and WordListObjects[5].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[5].tStart = t
            WordListObjects[5].frameNStart = frameN  # exact frame index
            WordListObjects[5].setAutoDraw(True)  
                # *text2* updates
        if t >= 0.0 and WordListObjects[6].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[6].tStart = t
            WordListObjects[6].frameNStart = frameN  # exact frame index
            WordListObjects[6].setAutoDraw(True)  
                # *text2* updates
        if t >= 0.0 and WordListObjects[7].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[7].tStart = t
            WordListObjects[7].frameNStart = frameN  # exact frame index
            WordListObjects[7].setAutoDraw(True)  
                # *text2* updates
        if t >= 0.0 and WordListObjects[8].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[8].tStart = t
            WordListObjects[8].frameNStart = frameN  # exact frame index
            WordListObjects[8].setAutoDraw(True)  
        if t >= 0.0 and WordListObjects[9].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[9].tStart = t
            WordListObjects[9].frameNStart = frameN  # exact frame index
            WordListObjects[9].setAutoDraw(True)      
        if t >= 0.0 and WordListObjects[10].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[10].tStart = t
            WordListObjects[10].frameNStart = frameN  # exact frame index
            WordListObjects[10].setAutoDraw(True)      
        if t >= 0.0 and WordListObjects[11].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[11].tStart = t
            WordListObjects[11].frameNStart = frameN  # exact frame index
            WordListObjects[11].setAutoDraw(True)          
        if t >= 0.0 and WordListObjects[12].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[12].tStart = t
            WordListObjects[12].frameNStart = frameN  # exact frame index
            WordListObjects[12].setAutoDraw(True)      
        if t >= 0.0 and WordListObjects[13].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[13].tStart = t
            WordListObjects[13].frameNStart = frameN  # exact frame index
            WordListObjects[13].setAutoDraw(True)      
        if t >= 0.0 and WordListObjects[14].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[14].tStart = t
            WordListObjects[14].frameNStart = frameN  # exact frame index
            WordListObjects[14].setAutoDraw(True)           
        if t >= 0.0 and WordListObjects[15].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[15].tStart = t
            WordListObjects[15].frameNStart = frameN  # exact frame index
            WordListObjects[15].setAutoDraw(True)      
        if t >= 0.0 and WordListObjects[16].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[16].tStart = t
            WordListObjects[16].frameNStart = frameN  # exact frame index
            WordListObjects[16].setAutoDraw(True)          
        if t >= 0.0 and WordListObjects[17].status == NOT_STARTED:
            # keep track of start time/frame for later
            WordListObjects[17].tStart = t
            WordListObjects[17].frameNStart = frameN  # exact frame index
            WordListObjects[17].setAutoDraw(True)      
#        if t >= 0.0 and WordListObjects[18].status == NOT_STARTED:
#            # keep track of start time/frame for later
#            WordListObjects[18].tStart = t
#            WordListObjects[18].frameNStart = frameN  # exact frame index
#            WordListObjects[18].setAutoDraw(True)      
#        if t >= 0.0 and WordListObjects[19].status == NOT_STARTED:
#            # keep track of start time/frame for later
#            WordListObjects[19].tStart = t
#            WordListObjects[19].frameNStart = frameN  # exact frame index
#            WordListObjects[19].setAutoDraw(True)      
#        if t >= 0.0 and WordListObjects[20].status == NOT_STARTED:
#            # keep track of start time/frame for later
#            WordListObjects[20].tStart = t
#            WordListObjects[20].frameNStart = frameN  # exact frame index
#            WordListObjects[20].setAutoDraw(True)          
#        if t >= 0.0 and WordListObjects[21].status == NOT_STARTED:
#            # keep track of start time/frame for later
#            WordListObjects[21].tStart = t
#            WordListObjects[21].frameNStart = frameN  # exact frame index
#            WordListObjects[21].setAutoDraw(True)      
#        if t >= 0.0 and WordListObjects[22].status == NOT_STARTED:
#            # keep track of start time/frame for later
#            WordListObjects[22].tStart = t
#            WordListObjects[22].frameNStart = frameN  # exact frame index
#            WordListObjects[22].setAutoDraw(True)      
#        if t >= 0.0 and WordListObjects[23].status == NOT_STARTED:
#            # keep track of start time/frame for later
#            WordListObjects[23].tStart = t
#            WordListObjects[23].frameNStart = frameN  # exact frame index
#            WordListObjects[23].setAutoDraw(True)    
#        
        
        if mouse.isPressedIn(WordListObjects[0]):
            WordListObjects[0].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[1]):
            WordListObjects[1].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[2]):
            WordListObjects[2].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[3]):
            WordListObjects[3].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[4]):
            WordListObjects[4].setColor(SelectedColor, 'rgb255')        
        if mouse.isPressedIn(WordListObjects[5]):
            WordListObjects[5].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[6]):
            WordListObjects[6].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[7]):
            WordListObjects[7].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[8]):
            WordListObjects[8].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[9]):
            WordListObjects[9].setColor(SelectedColor, 'rgb255')   
        if mouse.isPressedIn(WordListObjects[10]):
            WordListObjects[10].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[11]):
            WordListObjects[11].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[12]):
            WordListObjects[12].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[13]):
            WordListObjects[13].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[14]):
            WordListObjects[14].setColor(SelectedColor, 'rgb255')     
        if mouse.isPressedIn(WordListObjects[15]):
            WordListObjects[15].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[16]):
            WordListObjects[16].setColor(SelectedColor, 'rgb255')
        if mouse.isPressedIn(WordListObjects[17]):
            WordListObjects[17].setColor(SelectedColor, 'rgb255')
#        if mouse.isPressedIn(WordListObjects[18]):
#            WordListObjects[18].setColor(SelectedColor, 'rgb255')
#        if mouse.isPressedIn(WordListObjects[19]):
#            WordListObjects[19].setColor(SelectedColor, 'rgb255')     
#        if mouse.isPressedIn(WordListObjects[20]):
#            WordListObjects[20].setColor(SelectedColor, 'rgb255')
#        if mouse.isPressedIn(WordListObjects[21]):
#            WordListObjects[21].setColor(SelectedColor, 'rgb255')
#        if mouse.isPressedIn(WordListObjects[22]):
#            WordListObjects[22].setColor(SelectedColor, 'rgb255')
#        if mouse.isPressedIn(WordListObjects[23]):
#            WordListObjects[23].setColor(SelectedColor, 'rgb255')  
    # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    # Remove the words from the screen
    for i in WordListObjects:
        i.setAutoDraw(False)
    win.flip()
    return WordListObjects, mouse