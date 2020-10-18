#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 01, 2019, at 12:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'BLS_Clickable_Boxes'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jordan\\Documents\\Experiment Building\\6. Backwards Location Span\\bls reduced_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='Built_In_Display', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Stimulus"
StimulusClock = core.Clock()
Grid = visual.ImageStim(
    win=win,
    name='Grid', 
    image='Blank Grid.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Square = visual.Rect(
    win=win, name='Square',units='height', 
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[255,0,0], lineColorSpace='rgb',
    fillColor=[255,0,0], fillColorSpace='rgb255',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "Response"
ResponseClock = core.Clock()
grid = visual.ImageStim(
    win=win,
    name='grid', units='height', 
    image='Blank Grid.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.185, 0.185)[0], height=(0.185, 0.185)[1],
    ori=0, pos=(-0.386,.3875),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',units='height', 
    width=(0.185, 0.185)[0], height=(0.185, 0.185)[1],
    ori=0, pos=(-0.193,0.3875),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(0.185, 0.185)[0], height=(0.185, 0.185)[1],
    ori=0, pos=[0, 0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(0.185, 0.185)[0], height=(0.185, 0.185)[1],
    ori=0, pos=[0.193, 0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.386, 0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-.386, .19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
polygon_7 = visual.Rect(
    win=win, name='polygon_7',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-0.193, 0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
polygon_8 = visual.Rect(
    win=win, name='polygon_8',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0, 0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
polygon_9 = visual.Rect(
    win=win, name='polygon_9',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.193, 0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
polygon_10 = visual.Rect(
    win=win, name='polygon_10',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.386, 0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
polygon_11 = visual.Rect(
    win=win, name='polygon_11',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-0.386, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
polygon_12 = visual.Rect(
    win=win, name='polygon_12',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-0.193, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
polygon_13 = visual.Rect(
    win=win, name='polygon_13',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
polygon_14 = visual.Rect(
    win=win, name='polygon_14',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.193, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
polygon_15 = visual.Rect(
    win=win, name='polygon_15',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.386, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
polygon_16 = visual.Rect(
    win=win, name='polygon_16',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-0.386, -0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
polygon_17 = visual.Rect(
    win=win, name='polygon_17',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-0.193, -0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)
polygon_18 = visual.Rect(
    win=win, name='polygon_18',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0, -0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-19.0, interpolate=True)
polygon_19 = visual.Rect(
    win=win, name='polygon_19',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.193, -0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
polygon_20 = visual.Rect(
    win=win, name='polygon_20',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.386, -0.19415],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-21.0, interpolate=True)
polygon_21 = visual.Rect(
    win=win, name='polygon_21',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-0.386, -0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)
polygon_22 = visual.Rect(
    win=win, name='polygon_22',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[-0.193, -0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-23.0, interpolate=True)
polygon_23 = visual.Rect(
    win=win, name='polygon_23',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0, -0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-24.0, interpolate=True)
polygon_24 = visual.Rect(
    win=win, name='polygon_24',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.193, -0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-25.0, interpolate=True)
polygon_25 = visual.Rect(
    win=win, name='polygon_25',
    width=[0.185, 0.185][0], height=[0.185, 0.185][1],
    ori=0, pos=[0.386, -0.3875],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-26.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
squares = [polygon, polygon_2, polygon_3, polygon_4, polygon_5, polygon_6, polygon_7, polygon_8, polygon_9, polygon_10, polygon_11, polygon_12, polygon_13, polygon_14, polygon_15, polygon_16, polygon_17, polygon_18, polygon_19, polygon_20, polygon_21, polygon_22, polygon_23, polygon_24, polygon_25]

score = 0
wrongAnswer = 0

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
thx_txt = visual.TextStim(win=win, name='thx_txt',
    text='Good work! \n\nYou have completed this task.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
thx_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BLS_Trial_Picker.xlsx', selection='0:31'),
    seed=None, name='Trials')
thisExp.addLoop(Trials)  # add the loop to the experiment
thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in Trials:
    currentLoop = Trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Stimuli = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('BLS_Trial_List.xlsx', selection=rows),
        seed=None, name='Stimuli')
    thisExp.addLoop(Stimuli)  # add the loop to the experiment
    thisStimulus = Stimuli.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
    if thisStimulus != None:
        for paramName in thisStimulus:
            exec('{} = thisStimulus[paramName]'.format(paramName))
    
    for thisStimulus in Stimuli:
        currentLoop = Stimuli
        # abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
        if thisStimulus != None:
            for paramName in thisStimulus:
                exec('{} = thisStimulus[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Stimulus"-------
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        Square.setPos(location)
        # keep track of which components have finished
        StimulusComponents = [Grid, Square]
        for thisComponent in StimulusComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        StimulusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Stimulus"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = StimulusClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=StimulusClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Grid* updates
            if Grid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Grid.frameNStart = frameN  # exact frame index
                Grid.tStart = t  # local t and not account for scr refresh
                Grid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Grid, 'tStartRefresh')  # time at next scr refresh
                Grid.setAutoDraw(True)
            if Grid.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Grid.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Grid.tStop = t  # not accounting for scr refresh
                    Grid.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Grid, 'tStopRefresh')  # time at next scr refresh
                    Grid.setAutoDraw(False)
            
            # *Square* updates
            if Square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Square.frameNStart = frameN  # exact frame index
                Square.tStart = t  # local t and not account for scr refresh
                Square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Square, 'tStartRefresh')  # time at next scr refresh
                Square.setAutoDraw(True)
            if Square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Square.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Square.tStop = t  # not accounting for scr refresh
                    Square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Square, 'tStopRefresh')  # time at next scr refresh
                    Square.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimulusComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Stimulus"-------
        for thisComponent in StimulusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    # completed 1 repeats of 'Stimuli'
    
    
    # ------Prepare to start Routine "Response"-------
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse.clickSequence = []
    
    for square in squares:
        square.draw()
        square.color = 'white'
    # keep track of which components have finished
    ResponseComponents = [grid, key_resp, polygon, polygon_2, polygon_3, polygon_4, polygon_5, polygon_6, polygon_7, polygon_8, polygon_9, polygon_10, polygon_11, polygon_12, polygon_13, polygon_14, polygon_15, polygon_16, polygon_17, polygon_18, polygon_19, polygon_20, polygon_21, polygon_22, polygon_23, polygon_24, polygon_25, mouse]
    for thisComponent in ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Response"-------
    while continueRoutine:
        # get current time
        t = ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grid* updates
        if grid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grid.frameNStart = frameN  # exact frame index
            grid.tStart = t  # local t and not account for scr refresh
            grid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grid, 'tStartRefresh')  # time at next scr refresh
            grid.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        
        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(True)
        
        # *polygon_7* updates
        if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.tStart = t  # local t and not account for scr refresh
            polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            polygon_7.setAutoDraw(True)
        
        # *polygon_8* updates
        if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.tStart = t  # local t and not account for scr refresh
            polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
            polygon_8.setAutoDraw(True)
        
        # *polygon_9* updates
        if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_9.frameNStart = frameN  # exact frame index
            polygon_9.tStart = t  # local t and not account for scr refresh
            polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
            polygon_9.setAutoDraw(True)
        
        # *polygon_10* updates
        if polygon_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_10.frameNStart = frameN  # exact frame index
            polygon_10.tStart = t  # local t and not account for scr refresh
            polygon_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_10, 'tStartRefresh')  # time at next scr refresh
            polygon_10.setAutoDraw(True)
        
        # *polygon_11* updates
        if polygon_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_11.frameNStart = frameN  # exact frame index
            polygon_11.tStart = t  # local t and not account for scr refresh
            polygon_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_11, 'tStartRefresh')  # time at next scr refresh
            polygon_11.setAutoDraw(True)
        
        # *polygon_12* updates
        if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_12.frameNStart = frameN  # exact frame index
            polygon_12.tStart = t  # local t and not account for scr refresh
            polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
            polygon_12.setAutoDraw(True)
        
        # *polygon_13* updates
        if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_13.frameNStart = frameN  # exact frame index
            polygon_13.tStart = t  # local t and not account for scr refresh
            polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
            polygon_13.setAutoDraw(True)
        
        # *polygon_14* updates
        if polygon_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_14.frameNStart = frameN  # exact frame index
            polygon_14.tStart = t  # local t and not account for scr refresh
            polygon_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_14, 'tStartRefresh')  # time at next scr refresh
            polygon_14.setAutoDraw(True)
        
        # *polygon_15* updates
        if polygon_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_15.frameNStart = frameN  # exact frame index
            polygon_15.tStart = t  # local t and not account for scr refresh
            polygon_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_15, 'tStartRefresh')  # time at next scr refresh
            polygon_15.setAutoDraw(True)
        
        # *polygon_16* updates
        if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_16.frameNStart = frameN  # exact frame index
            polygon_16.tStart = t  # local t and not account for scr refresh
            polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
            polygon_16.setAutoDraw(True)
        
        # *polygon_17* updates
        if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_17.frameNStart = frameN  # exact frame index
            polygon_17.tStart = t  # local t and not account for scr refresh
            polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
            polygon_17.setAutoDraw(True)
        
        # *polygon_18* updates
        if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_18.frameNStart = frameN  # exact frame index
            polygon_18.tStart = t  # local t and not account for scr refresh
            polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
            polygon_18.setAutoDraw(True)
        
        # *polygon_19* updates
        if polygon_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_19.frameNStart = frameN  # exact frame index
            polygon_19.tStart = t  # local t and not account for scr refresh
            polygon_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_19, 'tStartRefresh')  # time at next scr refresh
            polygon_19.setAutoDraw(True)
        
        # *polygon_20* updates
        if polygon_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_20.frameNStart = frameN  # exact frame index
            polygon_20.tStart = t  # local t and not account for scr refresh
            polygon_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_20, 'tStartRefresh')  # time at next scr refresh
            polygon_20.setAutoDraw(True)
        
        # *polygon_21* updates
        if polygon_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_21.frameNStart = frameN  # exact frame index
            polygon_21.tStart = t  # local t and not account for scr refresh
            polygon_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_21, 'tStartRefresh')  # time at next scr refresh
            polygon_21.setAutoDraw(True)
        
        # *polygon_22* updates
        if polygon_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_22.frameNStart = frameN  # exact frame index
            polygon_22.tStart = t  # local t and not account for scr refresh
            polygon_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_22, 'tStartRefresh')  # time at next scr refresh
            polygon_22.setAutoDraw(True)
        
        # *polygon_23* updates
        if polygon_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_23.frameNStart = frameN  # exact frame index
            polygon_23.tStart = t  # local t and not account for scr refresh
            polygon_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_23, 'tStartRefresh')  # time at next scr refresh
            polygon_23.setAutoDraw(True)
        
        # *polygon_24* updates
        if polygon_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_24.frameNStart = frameN  # exact frame index
            polygon_24.tStart = t  # local t and not account for scr refresh
            polygon_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_24, 'tStartRefresh')  # time at next scr refresh
            polygon_24.setAutoDraw(True)
        
        # *polygon_25* updates
        if polygon_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_25.frameNStart = frameN  # exact frame index
            polygon_25.tStart = t  # local t and not account for scr refresh
            polygon_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_25, 'tStartRefresh')  # time at next scr refresh
            polygon_25.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [polygon,polygon_2,polygon_3,polygon_4,polygon_5,polygon_6,polygon_7,polygon_8,polygon_9,polygon_10,polygon_11,polygon_12,polygon_13,polygon_14,polygon_15,polygon_16,polygon_17,polygon_18,polygon_19,polygon_20,polygon_21,polygon_22,polygon_23,polygon_24,polygon_25]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        for square in squares:
            square.draw()
            if mouse.isPressedIn(square) and square.fillColor == 'white':
                square.color = 'black'
        
        for square in squares:
            if mouse.isPressedIn(square):
                if square.name not in mouse.clickSequence:
                    mouse.clickSequence.append(square.name)
                    thisExp.addData('clickSequence', mouse.clickSequence)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for Trials (TrialHandler)
    Trials.addData('mouse.x', mouse.x)
    Trials.addData('mouse.y', mouse.y)
    Trials.addData('mouse.leftButton', mouse.leftButton)
    Trials.addData('mouse.midButton', mouse.midButton)
    Trials.addData('mouse.rightButton', mouse.rightButton)
    Trials.addData('mouse.time', mouse.time)
    Trials.addData('mouse.clicked_name', mouse.clicked_name)
    if mouse.clickSequence == correct_seq:
        correct = 1
    else:
        correct = 0
    
    thisExp.addData('seq.corr', correct)
    
    if correct == 1:
        thisExp.addData('score', 1)
        score = score + 1
        wrongAnswer == 0
    else:
        thisExp.addData('score', 0)
        wrongAnswer +=1
        if wrongAnswer == 2:
            Trials.finished = True
                     
                     
    # the Routine "Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Trials'

# get names of stimulus parameters
if Trials.trialList in ([], [None], None):
    params = []
else:
    params = Trials.trialList[0].keys()
# save data for this loop
Trials.saveAsExcel(filename + '.xlsx', sheetName='Trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Thanks"-------
# update component parameters for each repeat
thx_key_resp.keys = []
thx_key_resp.rt = []
# keep track of which components have finished
ThanksComponents = [thx_txt, thx_key_resp]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Thanks"-------
while continueRoutine:
    # get current time
    t = ThanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thx_txt* updates
    if thx_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thx_txt.frameNStart = frameN  # exact frame index
        thx_txt.tStart = t  # local t and not account for scr refresh
        thx_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thx_txt, 'tStartRefresh')  # time at next scr refresh
        thx_txt.setAutoDraw(True)
    
    # *thx_key_resp* updates
    waitOnFlip = False
    if thx_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thx_key_resp.frameNStart = frameN  # exact frame index
        thx_key_resp.tStart = t  # local t and not account for scr refresh
        thx_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thx_key_resp, 'tStartRefresh')  # time at next scr refresh
        thx_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(thx_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if thx_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = thx_key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
