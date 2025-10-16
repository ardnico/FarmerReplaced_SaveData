import defs

return_zero()

plant_table = []
for _ in range(get_world_size()):
	tmp_table = []
	for __ in range(get_world_size()):
		tmp_table.append([None])
	plant_table.append(tmp_table)

while True:
	move_drone()
	plant_actions(plant_table)
