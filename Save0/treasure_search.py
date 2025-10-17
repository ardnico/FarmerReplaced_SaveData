import drone_mod
import ts_defs

# return to zero point and summon the maze
def summon_maze():
	drone_mod.return_zero()
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def get_maze_map():
	N = get_world_size()
	maze_map = []
	for _ in range(N):
		tmp_array = []
		for __ in range(N):
			tmp_array.append(ts_defs.undefined_point)
		maze_map.appen(tmp_array)
	return maze_map

def explorer_this_point(maze_map):
	x = get_pos_x()
	y = get_pos_y()
	forward = ts_defs.undefined_point
	current_point = maze_map[y][x]
	# check current map value
	if current_point == ts_defs.undefined_point:
		current_point = 0
		# set status bits
		if can_move(East):
			current_point += ts_defs.base_bit ** ts_defs.east_bit * ts_defs.can_pass
			forward = ts_defs.east_bit
		if can_move(West):
			current_point += ts_defs.base_bit ** ts_defs.west_bit * ts_defs.can_pass
			forward = ts_defs.west_bit
		if can_move(North):
			current_point += ts_defs.base_bit ** ts_defs.north_bit * ts_defs.can_pass
			forward = ts_defs.north_bit
		if can_move(South):
			current_point += ts_defs.base_bit ** ts_defs.south_bit * ts_defs.can_pass
			forward = ts_defs.south_bit
		
	return maze_map