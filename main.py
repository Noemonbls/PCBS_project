""" This is a replication of Shams et al 2000 experiment.
At each trial, participants must report the number of flashes they perceive.
"""
## A few necessary imports
import random
import numpy as np
from expyriment import design, control, stimuli
from useful_functions_PCBS_project import compute_list_possible_conditions,convert_eccentricity_to_cartesian_coordinates, convert_cartesian_coordinates_to_pixel_position,compute_norm_from_coordinates
## Parameters of the experiment
n_max_flashes = 4
n_max_beeps = 4
n_min_flashes= 1
n_min_beeps = 0
N_REPLICATIONS_PER_CONDITION = 5 #each stimulus configuration is run 5 times on each observer
list_possible_conditions = compute_list_possible_conditions(n_max_flashes,n_min_flashes,n_max_beeps,n_min_beeps)
N_TRIALS= (len(list_possible_conditions)) * N_REPLICATIONS_PER_CONDITION
list_all_possible_trials = list_possible_conditions * N_REPLICATIONS_PER_CONDITION
random.shuffle(list_all_possible_trials)
MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 4000
waiting_time_after_fixation_cross = 1000

## Parameters of the stimuli
height_fixation_cross = 25
length_fixation_cross = 25
width_fixation_cross = 4

radius_target_in_degrees= 2 
position_target_in_degrees = 5 
desired_target_angle = 45  

colour_target = (255,255,255)
position_target = (100,200) 
radius_target = 100
time_between_targets = 50 #ms
time_between_beeps = 57 #ms


#Experiment initialization

exp = design.Experiment(name="debug_Shams2000", text_size=40)
control.initialize(exp)
width_screen,height_screen= exp.screen.size
diagonal_screen = np.sqrt(width_screen**2 + height_screen**2)
(x_coordinate_target,y_coordinate_target) = convert_eccentricity_to_cartesian_coordinates(position_target_in_degrees,desired_target_angle)
coordinates_radius_target = convert_eccentricity_to_cartesian_coordinates(radius_target_in_degrees,desired_target_angle)
position_target_pixels = convert_cartesian_coordinates_to_pixel_position(x_coordinate_target,y_coordinate_target,width_screen,height_screen)
print(coordinates_radius_target)
radius_target_pixels = int(compute_norm_from_coordinates(coordinates_radius_target[0],coordinates_radius_target[1]) * diagonal_screen)
##Stimuli creation
main_instructions = stimuli.TextScreen("Instructions",
    f"""From time to time, a series of 1-4 flashes will appear onscreen.

    Your task is to press the number key corresponding to the number of discs you perceived

    Do it as fast as possible (we measure your reaction time)

    Please keep fixation on the center cross

    Audio beeps will sometimes accompany the discs. Try not to get distracted by them

    There will be {N_TRIALS} trials in total.

    Press the space bar to start.""")
instructions_for_response = stimuli.TextScreen("","How many flashes did you perceive?")
fixation_cross=stimuli.FixCross(size=(height_fixation_cross,length_fixation_cross), line_width=width_fixation_cross)
beep = stimuli.Audio('beep.ogg')
target = stimuli.Circle(radius=radius_target_pixels,colour=colour_target,position=position_target_pixels)

fixation_cross_screen = stimuli.BlankScreen()
fixation_cross.plot(fixation_cross_screen)
target_plus_cross_screen = stimuli.BlankScreen()
target.plot(target_plus_cross_screen)
fixation_cross.plot(target_plus_cross_screen)

exp.add_data_variable_names(['trial', 'condition', 'respkey', 'RT',])

beep.preload()
target_plus_cross_screen.preload()
#Main experiment
control.start(skip_ready_screen=True)
main_instructions.present()
exp.keyboard.wait()
for i_trial in range(N_TRIALS):
    trial_condition = list_all_possible_trials[i_trial-1] #i-1 because of python indexing
    n_flash = trial_condition[0]
    n_beep=trial_condition[1]
    n_beep_presented = 0
    n_flash_presented = 0 
    fixation_cross_screen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    while n_flash_presented < n_flash and n_beep_presented < n_beep:
        n_flash_presented+=1
        n_beep_presented +=1
        beep.play()
        exp.clock.wait(time_between_beeps)
        target_plus_cross_screen.present()
        exp.clock.wait(time_between_flashes)
    key,rt = exp.keyboard.wait()
    exp.data.add(i_trial,[list_all_possible_trials[i_trial-1], key, rt])
control.end()
