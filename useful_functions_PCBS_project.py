def compute_list_possible_conditions(n_max_flashes,n_min_flashes,n_max_beeps,n_min_beeps,n_replications_per_condition):
	## Create a list of tuples, each tuple being of the form (n_flash,n_beeps)
	n_max_beeps = 4
	n_min_beeps = 0
	n_max_flashes = 4
	n_min_flashes = 1
	possible_n_flashes = list(range(n_max_flashes+1))[n_min_flashes:]
	possible_n_beeps = list(range(n_max_beeps+1))[n_min_beeps:]
	list_possible_conditions = [None] * len(possible_n_flashes) * len(possible_n_beeps)
	position_in_list_possible_conditions = 0
	for n_flash in list_possible_n_flashes:
    	for n_beep in list_possible_n_beeps:
        	list_possible_conditions[position_in_list_possible_conditions] = (n_flash,n_beep)
        	position_in_list_possible_conditions +=1
    return(list_possible_conditions)