harvest()
plant(Entities.Pumpkin)
while True:
	while can_harvest() == False:
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
	if get_entity_type() == Entities.Pumpkin:
		harvest()
		break
	else:
		plant(Entities.Pumpkin)
