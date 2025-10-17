import drone_mod

drone_mod.return_zero()

for _ in range(get_world_size()**2):
	harvest()
	drone_mod.move_drone()