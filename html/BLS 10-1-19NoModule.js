﻿/******************** 
 * Bls 10-1-19 Test *
 ********************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'BLS 10-1-19';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const TrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TrialsLoopBegin, TrialsLoopScheduler);
flowScheduler.add(TrialsLoopScheduler);
flowScheduler.add(TrialsLoopEnd);
flowScheduler.add(ThanksRoutineBegin);
flowScheduler.add(ThanksRoutineEachFrame);
flowScheduler.add(ThanksRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var StimulusClock;
var Grid;
var Square;
var ResponseClock;
var grid;
var key_resp;
var polygon;
var polygon_2;
var polygon_3;
var polygon_4;
var polygon_5;
var polygon_6;
var polygon_7;
var polygon_8;
var polygon_9;
var polygon_10;
var polygon_11;
var polygon_12;
var polygon_13;
var polygon_14;
var polygon_15;
var polygon_16;
var polygon_17;
var polygon_18;
var polygon_19;
var polygon_20;
var polygon_21;
var polygon_22;
var polygon_23;
var polygon_24;
var polygon_25;
var mouse;
var ThanksClock;
var thx_txt;
var thx_key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Stimulus"
  StimulusClock = new util.Clock();
  Grid = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Grid', units : undefined, 
    image : 'Blank Grid.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  Square = new visual.Rect ({
    win: psychoJS.window, name: 'Square', units : 'height', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([255, 0, 0]),
    fillColor: new util.Color([255, 0, 0]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "Response"
  ResponseClock = new util.Clock();
  grid = new visual.ImageStim({
    win : psychoJS.window,
    name : 'grid', units : undefined, 
    image : 'Blank Grid.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.386), 0.3875],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  polygon_2 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_2', units : 'height', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.193), 0.3875],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  polygon_3 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_3', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0, 0.3875],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  polygon_4 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_4', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.193, 0.3875],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  polygon_5 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_5', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.386, 0.3875],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  polygon_6 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_6', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.386), 0.19415],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  polygon_7 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_7', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.193), 0.19415],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  polygon_8 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_8', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0, 0.19415],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  polygon_9 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_9', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.193, 0.19415],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -10, interpolate: true,
  });
  
  polygon_10 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_10', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.386, 0.19415],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -11, interpolate: true,
  });
  
  polygon_11 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_11', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.386), 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -12, interpolate: true,
  });
  
  polygon_12 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_12', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.193), 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -13, interpolate: true,
  });
  
  polygon_13 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_13', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -14, interpolate: true,
  });
  
  polygon_14 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_14', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.193, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -15, interpolate: true,
  });
  
  polygon_15 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_15', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.386, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -16, interpolate: true,
  });
  
  polygon_16 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_16', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.386), (- 0.19415)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -17, interpolate: true,
  });
  
  polygon_17 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_17', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.193), (- 0.19415)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -18, interpolate: true,
  });
  
  polygon_18 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_18', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0, (- 0.19415)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -19, interpolate: true,
  });
  
  polygon_19 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_19', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.193, (- 0.19415)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -20, interpolate: true,
  });
  
  polygon_20 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_20', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.386, (- 0.19415)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -21, interpolate: true,
  });
  
  polygon_21 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_21', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.386), (- 0.3875)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -22, interpolate: true,
  });
  
  polygon_22 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_22', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [(- 0.193), (- 0.3875)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -23, interpolate: true,
  });
  
  polygon_23 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_23', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0, (- 0.3875)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -24, interpolate: true,
  });
  
  polygon_24 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_24', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.193, (- 0.3875)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -25, interpolate: true,
  });
  
  polygon_25 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_25', 
    width: [0.185, 0.185][0], height: [0.185, 0.185][1],
    ori: 0, pos: [0.386, (- 0.3875)],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -26, interpolate: true,
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Thanks"
  ThanksClock = new util.Clock();
  thx_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'thx_txt',
    text: 'Good work! \n\nYou have completed this task.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  thx_key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var Trials;
var currentLoop;
var trialIterator;
function TrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'BLS_Trial_Picker.xlsx',
    seed: undefined, name: 'Trials'});
  psychoJS.experiment.addLoop(Trials); // add the loop to the experiment
  currentLoop = Trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = Trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(Trials));
    const StimuliLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(StimuliLoopBegin, StimuliLoopScheduler);
    thisScheduler.add(StimuliLoopScheduler);
    thisScheduler.add(StimuliLoopEnd);
    thisScheduler.add(ResponseRoutineBegin);
    thisScheduler.add(ResponseRoutineEachFrame);
    thisScheduler.add(ResponseRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

var Stimuli;
function StimuliLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Stimuli = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'BLS_Trial_List.xlsx', rows),
    seed: undefined, name: 'Stimuli'});
  psychoJS.experiment.addLoop(Stimuli); // add the loop to the experiment
  currentLoop = Stimuli;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = Stimuli[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisStimulus = result.value;
    thisScheduler.add(importConditions(Stimuli));
    thisScheduler.add(StimulusRoutineBegin);
    thisScheduler.add(StimulusRoutineEachFrame);
    thisScheduler.add(StimulusRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function StimuliLoopEnd() {
  psychoJS.experiment.removeLoop(Stimuli);

  return Scheduler.Event.NEXT;
}


function TrialsLoopEnd() {
  psychoJS.experiment.removeLoop(Trials);

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var StimulusComponents;
function StimulusRoutineBegin() {
  //------Prepare to start Routine 'Stimulus'-------
  t = 0;
  StimulusClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  Square.setPos(location);
  // keep track of which components have finished
  StimulusComponents = [];
  StimulusComponents.push(Grid);
  StimulusComponents.push(Square);
  
  StimulusComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
var continueRoutine;
function StimulusRoutineEachFrame() {
  //------Loop for each frame of Routine 'Stimulus'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = StimulusClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Grid* updates
  if (t >= 0.0 && Grid.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Grid.tStart = t;  // (not accounting for frame time here)
    Grid.frameNStart = frameN;  // exact frame index
    Grid.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Grid.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Grid.setAutoDraw(false);
  }
  
  // *Square* updates
  if (t >= 0.0 && Square.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Square.tStart = t;  // (not accounting for frame time here)
    Square.frameNStart = frameN;  // exact frame index
    Square.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Square.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Square.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  StimulusComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function StimulusRoutineEnd() {
  //------Ending Routine 'Stimulus'-------
  StimulusComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var gotValidClick;
var ResponseComponents;
function ResponseRoutineBegin() {
  //------Prepare to start Routine 'Response'-------
  t = 0;
  ResponseClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  // setup some python lists for storing info about the mouse
  // current position of the mouse:
  mouse.x = [];
  mouse.y = [];
  mouse.leftButton = [];
  mouse.midButton = [];
  mouse.rightButton = [];
  mouse.time = [];
  mouse.clicked_name = [];
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  ResponseComponents = [];
  ResponseComponents.push(grid);
  ResponseComponents.push(key_resp);
  ResponseComponents.push(polygon);
  ResponseComponents.push(polygon_2);
  ResponseComponents.push(polygon_3);
  ResponseComponents.push(polygon_4);
  ResponseComponents.push(polygon_5);
  ResponseComponents.push(polygon_6);
  ResponseComponents.push(polygon_7);
  ResponseComponents.push(polygon_8);
  ResponseComponents.push(polygon_9);
  ResponseComponents.push(polygon_10);
  ResponseComponents.push(polygon_11);
  ResponseComponents.push(polygon_12);
  ResponseComponents.push(polygon_13);
  ResponseComponents.push(polygon_14);
  ResponseComponents.push(polygon_15);
  ResponseComponents.push(polygon_16);
  ResponseComponents.push(polygon_17);
  ResponseComponents.push(polygon_18);
  ResponseComponents.push(polygon_19);
  ResponseComponents.push(polygon_20);
  ResponseComponents.push(polygon_21);
  ResponseComponents.push(polygon_22);
  ResponseComponents.push(polygon_23);
  ResponseComponents.push(polygon_24);
  ResponseComponents.push(polygon_25);
  ResponseComponents.push(mouse);
  
  ResponseComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var prevButtonState;
function ResponseRoutineEachFrame() {
  //------Loop for each frame of Routine 'Response'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ResponseClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *grid* updates
  if (t >= 0.0 && grid.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    grid.tStart = t;  // (not accounting for frame time here)
    grid.frameNStart = frameN;  // exact frame index
    grid.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *polygon* updates
  if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon.tStart = t;  // (not accounting for frame time here)
    polygon.frameNStart = frameN;  // exact frame index
    polygon.setAutoDraw(true);
  }

  
  // *polygon_2* updates
  if (t >= 0.0 && polygon_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_2.tStart = t;  // (not accounting for frame time here)
    polygon_2.frameNStart = frameN;  // exact frame index
    polygon_2.setAutoDraw(true);
  }

  
  // *polygon_3* updates
  if (t >= 0.0 && polygon_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_3.tStart = t;  // (not accounting for frame time here)
    polygon_3.frameNStart = frameN;  // exact frame index
    polygon_3.setAutoDraw(true);
  }

  
  // *polygon_4* updates
  if (t >= 0.0 && polygon_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_4.tStart = t;  // (not accounting for frame time here)
    polygon_4.frameNStart = frameN;  // exact frame index
    polygon_4.setAutoDraw(true);
  }

  
  // *polygon_5* updates
  if (t >= 0.0 && polygon_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_5.tStart = t;  // (not accounting for frame time here)
    polygon_5.frameNStart = frameN;  // exact frame index
    polygon_5.setAutoDraw(true);
  }

  
  // *polygon_6* updates
  if (t >= 0.0 && polygon_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_6.tStart = t;  // (not accounting for frame time here)
    polygon_6.frameNStart = frameN;  // exact frame index
    polygon_6.setAutoDraw(true);
  }

  
  // *polygon_7* updates
  if (t >= 0.0 && polygon_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_7.tStart = t;  // (not accounting for frame time here)
    polygon_7.frameNStart = frameN;  // exact frame index
    polygon_7.setAutoDraw(true);
  }

  
  // *polygon_8* updates
  if (t >= 0.0 && polygon_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_8.tStart = t;  // (not accounting for frame time here)
    polygon_8.frameNStart = frameN;  // exact frame index
    polygon_8.setAutoDraw(true);
  }

  
  // *polygon_9* updates
  if (t >= 0.0 && polygon_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_9.tStart = t;  // (not accounting for frame time here)
    polygon_9.frameNStart = frameN;  // exact frame index
    polygon_9.setAutoDraw(true);
  }

  
  // *polygon_10* updates
  if (t >= 0.0 && polygon_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_10.tStart = t;  // (not accounting for frame time here)
    polygon_10.frameNStart = frameN;  // exact frame index
    polygon_10.setAutoDraw(true);
  }

  
  // *polygon_11* updates
  if (t >= 0.0 && polygon_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_11.tStart = t;  // (not accounting for frame time here)
    polygon_11.frameNStart = frameN;  // exact frame index
    polygon_11.setAutoDraw(true);
  }

  
  // *polygon_12* updates
  if (t >= 0.0 && polygon_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_12.tStart = t;  // (not accounting for frame time here)
    polygon_12.frameNStart = frameN;  // exact frame index
    polygon_12.setAutoDraw(true);
  }

  
  // *polygon_13* updates
  if (t >= 0.0 && polygon_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_13.tStart = t;  // (not accounting for frame time here)
    polygon_13.frameNStart = frameN;  // exact frame index
    polygon_13.setAutoDraw(true);
  }

  
  // *polygon_14* updates
  if (t >= 0.0 && polygon_14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_14.tStart = t;  // (not accounting for frame time here)
    polygon_14.frameNStart = frameN;  // exact frame index
    polygon_14.setAutoDraw(true);
  }

  
  // *polygon_15* updates
  if (t >= 0.0 && polygon_15.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_15.tStart = t;  // (not accounting for frame time here)
    polygon_15.frameNStart = frameN;  // exact frame index
    polygon_15.setAutoDraw(true);
  }

  
  // *polygon_16* updates
  if (t >= 0.0 && polygon_16.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_16.tStart = t;  // (not accounting for frame time here)
    polygon_16.frameNStart = frameN;  // exact frame index
    polygon_16.setAutoDraw(true);
  }

  
  // *polygon_17* updates
  if (t >= 0.0 && polygon_17.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_17.tStart = t;  // (not accounting for frame time here)
    polygon_17.frameNStart = frameN;  // exact frame index
    polygon_17.setAutoDraw(true);
  }

  
  // *polygon_18* updates
  if (t >= 0.0 && polygon_18.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_18.tStart = t;  // (not accounting for frame time here)
    polygon_18.frameNStart = frameN;  // exact frame index
    polygon_18.setAutoDraw(true);
  }

  
  // *polygon_19* updates
  if (t >= 0.0 && polygon_19.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_19.tStart = t;  // (not accounting for frame time here)
    polygon_19.frameNStart = frameN;  // exact frame index
    polygon_19.setAutoDraw(true);
  }

  
  // *polygon_20* updates
  if (t >= 0.0 && polygon_20.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_20.tStart = t;  // (not accounting for frame time here)
    polygon_20.frameNStart = frameN;  // exact frame index
    polygon_20.setAutoDraw(true);
  }

  
  // *polygon_21* updates
  if (t >= 0.0 && polygon_21.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_21.tStart = t;  // (not accounting for frame time here)
    polygon_21.frameNStart = frameN;  // exact frame index
    polygon_21.setAutoDraw(true);
  }

  
  // *polygon_22* updates
  if (t >= 0.0 && polygon_22.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_22.tStart = t;  // (not accounting for frame time here)
    polygon_22.frameNStart = frameN;  // exact frame index
    polygon_22.setAutoDraw(true);
  }

  
  // *polygon_23* updates
  if (t >= 0.0 && polygon_23.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_23.tStart = t;  // (not accounting for frame time here)
    polygon_23.frameNStart = frameN;  // exact frame index
    polygon_23.setAutoDraw(true);
  }

  
  // *polygon_24* updates
  if (t >= 0.0 && polygon_24.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_24.tStart = t;  // (not accounting for frame time here)
    polygon_24.frameNStart = frameN;  // exact frame index
    polygon_24.setAutoDraw(true);
  }

  
  // *polygon_25* updates
  if (t >= 0.0 && polygon_25.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon_25.tStart = t;  // (not accounting for frame time here)
    polygon_25.frameNStart = frameN;  // exact frame index
    polygon_25.setAutoDraw(true);
  }

  // *mouse* updates
  if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse.tStart = t;  // (not accounting for frame time here)
    mouse.frameNStart = frameN;  // exact frame index
    mouse.status = PsychoJS.Status.STARTED;
    mouse.mouseClock.reset();
    prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        const xys = mouse.getPos();
        mouse.x.push(xys[0]);
        mouse.y.push(xys[1]);
        mouse.leftButton.push(buttons[0]);
        mouse.midButton.push(buttons[1]);
        mouse.rightButton.push(buttons[2]);
        mouse.time.push(mouse.mouseClock.getTime());
        // check if the mouse was inside our 'clickable' objects
        gotValidClick = false;
        for (const obj of [polygon,polygon_2,polygon_3,polygon_4,polygon_5,polygon_6,polygon_7,polygon_8,polygon_9,polygon_10,polygon_11,polygon_12,polygon_13,polygon_14,polygon_15,polygon_16,polygon_17,polygon_18,polygon_19,polygon_20,polygon_21,polygon_22,polygon_23,polygon_24,polygon_25]) {
          if (obj.contains(mouse)) {
            gotValidClick = true;
            mouse.clicked_name.push(obj.name)
          }
        }
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ResponseComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ResponseRoutineEnd() {
  //------Ending Routine 'Response'-------
  ResponseComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('mouse.x', mouse.x);
  psychoJS.experiment.addData('mouse.y', mouse.y);
  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
  psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
  psychoJS.experiment.addData('mouse.time', mouse.time);
  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
  
  // the Routine "Response" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var ThanksComponents;
function ThanksRoutineBegin() {
  //------Prepare to start Routine 'Thanks'-------
  t = 0;
  ThanksClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  thx_key_resp.keys = undefined;
  thx_key_resp.rt = undefined;
  // keep track of which components have finished
  ThanksComponents = [];
  ThanksComponents.push(thx_txt);
  ThanksComponents.push(thx_key_resp);
  
  ThanksComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function ThanksRoutineEachFrame() {
  //------Loop for each frame of Routine 'Thanks'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ThanksClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *thx_txt* updates
  if (t >= 0.0 && thx_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    thx_txt.tStart = t;  // (not accounting for frame time here)
    thx_txt.frameNStart = frameN;  // exact frame index
    thx_txt.setAutoDraw(true);
  }

  
  // *thx_key_resp* updates
  if (t >= 0.0 && thx_key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    thx_key_resp.tStart = t;  // (not accounting for frame time here)
    thx_key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { thx_key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { thx_key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { thx_key_resp.clearEvents(); });
  }

  if (thx_key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = thx_key_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ThanksComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ThanksRoutineEnd() {
  //------Ending Routine 'Thanks'-------
  ThanksComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}