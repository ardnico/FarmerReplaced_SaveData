while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if j % 2 == 0:
				plant(Entities.tree)
			else:
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Carrot)
			if i % 2 == 0:
				if get_pos_y() == get_world_size() - 1:
					move(East)
					move(North)
				else:
					move(North)