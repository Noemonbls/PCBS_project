""" This is a replication of Shams et al 2000 experiment.
At each trial, participants must report the number of flashes they perceive.
"""
## A few necessary imports
import random
import numpy as np
from expyriment import design, control, stimuli, misc
from useful_functions_PCBS_project import compute_list_possible_conditions_2002_experiment
## Parameters of the experiment
n_max_flashes = 4
n_max_beeps = 4
n_min_flashes= 1
n_min_beeps = 0
N_REPLICATIONS_PER_CONDITION = 5 #each stimulus configuration is run 5 times on each observer
list_possible_conditions = compute_list_possible_conditions_2002_experiment(n_max_flashes,n_min_flashes,n_max_beeps,n_min_beeps)
N_TRIALS= (len(list_possible_conditions)) * N_REPLICATIONS_PER_CONDITION
list_all_possible_trials = [(1,0),(1,0),(1,2),(1,3),(4,0),(4,1)]
#list_all_possible_trials = list_possible_conditions * N_REPLICATIONS_PER_CONDITION
#random.shuffle(list_all_possible_trials)
MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
list_valid_keys = misc.constants.K_ALL_DIGITS + misc.constants.K_ALL_KEYPAD_DIGITS

## Parameters of the stimuli
height_fixation_cross = 25
length_fixation_cross = 25
width_fixation_cross = 4

radius_target_in_degrees= 2 
position_target_in_degrees = 5 
desired_target_angle = 45  

colour_target = (255,255,255)
position_target = (0,-300) 
radius_target = 75

frequency_beep = 3500 #Hz
duration_beep = 7*10 #ms
time_between_targets = 50*10 #ms
time_between_beeps = 50*10 #ms
time_presentation_target = 17*10 #ms
delay_first_beep_first_flash = 16*25 #ms


#Experiment initialization

exp = design.Experiment(name="debug_Shams2000", text_size=40)
control.initialize(exp)
##Stimuli creation
main_instructions = stimuli.TextScreen("Instructions",
    f"""From time to time, a series of 1-4 flashes will appear onscreen.

    Your task is to press the number key corresponding to the number of discs you perceived

    Do it as fast as possible (we measure your reaction time)

    Please keep fixation on the center cross

    Audio beeps will sometimes accompany the discs. Try not to get distracted by them

    There will be {N_TRIALS} trials in total.

    Press the space bar to start.""")
response_screen = stimuli.TextScreen("","How many flashes did you perceive?")
key_error_screen = stimuli.TextScreen("","Your answer is not a number, try again  ! ")

fixation_cross=stimuli.FixCross(size=(height_fixation_cross,length_fixation_cross), line_width=width_fixation_cross)
beep = stimuli.Tone(duration=duration_beep,frequency=frequency_beep)
target = stimuli.Circle(radius=radius_target,colour=colour_target,position=position_target)

fixation_cross_screen = stimuli.BlankScreen()
fixation_cross.plot(fixation_cross_screen)
target_plus_cross_screen = stimuli.BlankScreen()
target.plot(target_plus_cross_screen)
fixation_cross.plot(target_plus_cross_screen)

exp.add_data_variable_names(['trial', 'condition', 'respkey', 'RT',])

beep.preload()
target_plus_cross_screen.preload()
fixation_cross_screen.preload()
#Main experiment
control.start(skip_ready_screen=True)
main_instructions.present()
exp.keyboard.wait()
for i_trial in range(N_TRIALS):
    trial_condition = list_all_possible_trials[i_trial]
    n_flash = trial_condition[0]
    n_beep=trial_condition[1]
    n_beep_presented = 0
    n_flash_presented = 0 
    fixation_cross_screen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    if n_beep == 0:
        while n_flash_presented < n_flash : 
            target_plus_cross_screen.present()
            exp.clock.wait(time_presentation_target)
            fixation_cross_screen.present()
            exp.clock.wait(time_between_targets)
            n_flash_presented +=1

    elif n_beep > 0 :
        beep.play()
        exp.clock.wait(delay_first_beep_first_flash)
        n_beep_presented+=1
        target_plus_cross_screen.present()
        exp.clock.wait(time_presentation_target)
        fixation_cross_screen.present()
        n_flash_presented+=1
        if n_flash == 1 :
            exp.clock.wait(time_between_beeps - delay_first_beep_first_flash - time_presentation_target)
            while n_beep_presented < n_beep :
                beep.play()
                exp.clock.wait(time_between_beeps)
                n_beep_presented+=1
        elif n_flash > 1 :
            exp.clock.wait(time_between_targets)
            while n_flash_presented < n_flash : 
                target_plus_cross_screen.present()
                exp.clock.wait(time_presentation_target)
                fixation_cross_screen.present()
                exp.clock.wait(time_between_targets)
                n_flash_presented +=1
    response_screen.present()    
    key,rt = exp.keyboard.wait()
    while key not in list_valid_keys :
        key_error_screen.present()
        key,rt = exp.keyboard.wait()
    exp.data.add([i_trial,trial_condition,key,rt])


control.end()