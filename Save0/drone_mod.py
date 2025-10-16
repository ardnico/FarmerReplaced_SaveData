import definition_page

def return_zero():
	size = get_world_size()
	while get_pos_x() != 0:
		if get_pos_x() > (size // 2):
			move(East)
		else:
			move(West)
	while get_pos_y() != 0:
		if get_pos_y() > (size // 2):
			move(North)
		else:
			move(South)

def move_drone():
	size = get_pos_x()
	if size < get_pos_y():
		size = get_pos_y()
	if get_world_size() < size:
		return_zero()
		return
	if size % 2 == 0:
		if get_pos_x() < size or get_pos_y() == 0:
			move(East)
		else:
			move(South)
	else:
		if get_pos_y() < size or get_pos_x() == 0:
			move(North)
		else:
			move(West)
	return



	
