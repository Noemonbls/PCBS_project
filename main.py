""" This is a replication of Shams et al 2000 experiment.
At each trial, participants must report the number of flashes they perceive.
"""
## A few necessary imports
import random
from expyriment import design, control, stimuli, Audio
from useful_functions_PCBS_project import compute_n_trials

## Parameters of the experiment
N_MAX_FLASHES = 4
N_MAX_BEEPS = 4
N_MIN_FLASHES = 1
N_MIN_BEEPS = 0
N_REPLICATIONS_PER_CONDITION = 5 #each stimulus configuration is run 5 times on each observer
list_possible_conditions = compute_list_possible_conditions(n_max_flashes,n_min_flashes,n_max_beeps,n_min_beeps)
N_TRIALS= (length(list_possible_conditions)) * N_REPLICATIONS_PER_CONDITION

MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 4000


## Parameters of the stimuli
height_fixation_cross = 25
length_fixation_cross = 25
width_fixation_cross = 4
radius_target = #2 degrees
eccentricity_target =  #5 degrees
time_between_targets = 50 #ms
time_between_beeps = 57 #ms


#Experiment initialization

exp = design.Experiment(name="Shams2000", text_size=40)
control.initialize(exp)

##Stimuli creation
blankscreen = stimuli.BlankScreen()
main_instructions = stimuli.TextScreen("Instructions",
    f"""From time to time, a series of 1-4 flashes will appear onscreen.

    Your task is to press the number key corresponding to the number of discs you perceived

    Do it as fast as possible (we measure your reaction time)

    Please keep fixation on the center cross

    Audio beeps will sometimes accompany the discs. Try not to get distracted by them

    There will be {N_TRIALS} trials in total.

    Press the space bar to start.""")
instructions_for_response = stimuli.TextScreen("","How many flashes did you perceive?")
fixation_cross=expyriment.stimuli.FixCross(size=(height_fixation_cross,length_fixation_cross), line_width=width_fixation_cross)
beep = Audio('beep.ogg')
target = stimuli.Circle()

exp.add_data_variable_names(['trial', 'wait', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
main_instructions.present()
exp.keyboard.wait()

for i_trial in range(N_TRIALS):
    number_to_present=str(random.randint(1,10))
    target = stimuli.TextLine(number_to_present, text_size=4)
    blankscreen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    target.present()
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
    exp.data.add([i_trial, waiting_time, key, rt])

control.end()
