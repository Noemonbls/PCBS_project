def compute_list_possible_conditions(n_max_flashes,n_min_flashes,n_max_beeps,n_min_beeps):
	## Create a list of tuples, each tuple being of the form (n_flash,n_beeps)
	list_possible_n_flashes = list(range(n_max_flashes+1))[n_min_flashes:]
	list_possible_n_beeps = list(range(n_max_beeps+1))[n_min_beeps:]
	list_possible_conditions = [None] * len(list_possible_n_flashes) * len(list_possible_n_beeps)
	position_in_list_possible_conditions = 0
	for n_flash in list_possible_n_flashes:
		for n_beep in list_possible_n_beeps:
			list_possible_conditions[position_in_list_possible_conditions] = (n_flash,n_beep)
			position_in_list_possible_conditions +=1
	return(list_possible_conditions)


def convert_eccentricity_to_cartesian_coordinates(eccentricity,desired_angle_in_degree):
	import math
	angle=math.radians(desired_angle_in_degree)
	x=math.sin(angle) * eccentricity
	y=math.cos(angle) * eccentricity
	return(x,y)

def convert_cartesian_coordinates_to_pixel_position(x,y,width_screen,height_screen):
	x_pixel = x*width_screen
	y_pixel = y*height_screen
	return(x_pixel,y_pixel)

def compute_norm_from_coordinates(x,y):
	norm= (x**2 + y**2)**1/2
