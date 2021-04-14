def compute_list_possible_conditions(n_max_flashes,n_min_flashes,n_max_beeps,n_min_beeps):
	## Create a list of tuples, each tuple being of the form (n_flash,n_beeps)
	if n_max_flashes == n_min_flashes : 
		list_possible_n_flashes = [n_max_flashes]
	else:
		list_possible_n_flashes = list(range(n_max_flashes+1))[n_min_flashes:]

	if n_max_beeps == n_min_beeps : 
		list_possible_n_beeps = [n_max_beeps]
	else:
		list_possible_n_beeps = list(range(n_max_beeps+1))[n_min_beeps:]

	list_possible_conditions = [None] * len(list_possible_n_flashes) * len(list_possible_n_beeps)
	position_in_list_possible_conditions = 0
	for n_flash in list_possible_n_flashes:
		for n_beep in list_possible_n_beeps:
			list_possible_conditions[position_in_list_possible_conditions] = (n_flash,n_beep)
			position_in_list_possible_conditions +=1
	return(list_possible_conditions)


def compute_list_possible_conditions_2002_experiment(n_max_flashes,n_min_flashes,n_max_beeps,n_min_beeps):
	## Create a list of tuples, each tuple being of the form (n_flash,n_beeps)
	if n_max_flashes == n_min_flashes : 
		list_possible_n_flashes = [n_max_flashes]
	else:
		list_possible_n_flashes = list(range(n_max_flashes+1))[n_min_flashes:]

	if n_max_beeps == n_min_beeps : 
		list_possible_n_beeps = [n_max_beeps]
	else:
		list_possible_n_beeps = list(range(n_max_beeps+1))[n_min_beeps:]

	list_possible_conditions = [None] * (len(list_possible_n_beeps)+(len(list_possible_n_flashes)-1)*2)
	position_in_list_possible_conditions = 0
	for n_flash in list_possible_n_flashes:
		if n_flash == 1 :
			for n_beep in list_possible_n_beeps:
				list_possible_conditions[position_in_list_possible_conditions] = (n_flash,n_beep)
				position_in_list_possible_conditions +=1
		else:
			for n_beep in [0,1]:
				list_possible_conditions[position_in_list_possible_conditions] = (n_flash,n_beep)
				position_in_list_possible_conditions +=1
	return(list_possible_conditions)