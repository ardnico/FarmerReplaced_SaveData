import definition_page
import drone_mod

pumpkin_count = definition_page.pumpkin_size ** 2

plant_table = []
for _ in range(get_world_size()):
	tmp_table = []
	for __ in range(get_world_size()):
		tmp_table.append([None])
	plant_table.append(tmp_table)

def reset_plant_table_whithin_p():
	global plant_table
	for i in range(definition_page.pumpkin_size):
		for j in range(definition_page.pumpkin_size):
			plant_table[i][j] = None

def stay_revival_pumpkin():
	if get_ground_type() == Grounds.Grassland:
		till()
	while True:
		while can_harvest() == False:
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
		if get_entity_type() == Entities.Pumpkin:
			break
		else:
			plant(Entities.Pumpkin)

def chk_pumpkin():
	global plant_table
	if get_entity_type() != Entities.pumpkin:
		plant(Entities.Pumpkin)
		return
	global pumpkin_count

	if plant_table[get_pos_y()][get_pos_x()] != Entities.Pumpkin:
		pumpkin_count -= 1
		if pumpkin_count == 0:
			while can_harvest() == False:
				do_a_flip()
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
			harvest()
			pumpkin_count = definition_page.pumpkin_size ** 2
			reset_plant_table_whithin_p()
			return 		
		else:
			stay_revival_pumpkin()
	plant_table[get_pos_y()][get_pos_x()] = Entities.Pumpkin

def multi_plant_action():
	global plant_table
	if can_harvest():
		harvest()
	if get_ground_type() == Grounds.Grassland:
		till()
	tmp_num = (get_pos_x() + get_pos_y()) % len(definition_page.plant_species)
	plant(definition_page.plant_species[tmp_num])
	plant_table[get_pos_y()][get_pos_x()] = get_entity_type()

def pluse_nut():
	global plant_table
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
	if num_items(Items.Water) > 0:
		if get_water() < 1:
			use_item(Items.Water)
	multi_plant_action()

def plant_actions():
	global plant_table
	if get_ground_type() == Grounds.Grassland:
		till()
	if get_pos_x() > definition_page.pumpkin_size or get_pos_y() > definition_page.pumpkin_size:
		multi_plant_action()
		pluse_nut()
	else:
		chk_pumpkin()
	drone_mod.move_drone()


	
		