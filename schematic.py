import mcschematic

def generateSchematic(filename: str, path: str):

	string = open("message.txt").read()
	FILL = "0"

	while (len(string)<1024):
		string = string + FILL

	schem = mcschematic.MCSchematic()

	BLOCK = 'minecraft:barrel{Items:[{Slot:0,id:redstone,Count:1}]}'
	ZERO = 'minecraft:tinted_glass'

	coordinateList = []

	for k in range(8):
		z = 16 + k*5

		for i in range(16):
			if i < 8:
				x =-16 + i*2
				if i%2==0:
					for j in range(8):
						y = (-j*2) - 14
						coordinate = [x,y,z]
						coordinateList.append(coordinate)

				else:
					for j in range(8):
						y = (-j*2) - 15
						coordinate = [x,y,z]
						coordinateList.append(coordinate)

			elif i >= 8:
				x =-14 + (i*2)
				if i%2==0:
					for j in range(8):
						y = (-j*2) - 15
						coordinate = [x,y,z]
						coordinateList.append(coordinate)

				else:
					for j in range(8):
						y = (-j*2) - 14
						coordinate = [x,y,z]
						coordinateList.append(coordinate)

	for i,bit in zip(range(len(coordinateList)),string):
		if bit == "1":
			schem.setBlock(tuple(coordinateList[i]), BLOCK)
		else:
			schem.setBlock(tuple(coordinateList[i]), ZERO)

	schem.save(path, filename, mcschematic.Version.JE_1_18_2)
