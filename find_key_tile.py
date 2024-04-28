import os

p = (0, 0)

directions = [
(-1, 0),
(1, 0),
(0, 1),
(0, -1)
]

GROUND_TILE = 'g'
KEY_TILE = 'k'

map = [
[GROUND_TILE, GROUND_TILE, GROUND_TILE, GROUND_TILE],
[GROUND_TILE, GROUND_TILE, KEY_TILE, GROUND_TILE],
[GROUND_TILE, GROUND_TILE, GROUND_TILE, GROUND_TILE],
]

def addCoords(c1, c2):
	return (c1[0] + c2[0], c1[1] + c2[1])

def inBounds(c, map):
	return c[0] >= 0 and c[0] <= 2 and c[1] >= 0 and c[1] <= 3

def tileAt(map, c):
	return map[c[0]][c[1]]
	
visitedCoords = []

def findKeyTile(p, map, visitedCoords):
	visitedCoords.append(p)
	print(visitedCoords)
	print('\n')
	os.system("pause")
	
	print("checking if key tile at ", p)
	if (tileAt(map, p) == KEY_TILE):
		print("FOUND KEY TILE: ", tileAt(map, p))
		return p
		
	for d in directions:
		nextStep = addCoords(p, d)
		
		print("nextStep ", nextStep)
	
		if (inBounds(nextStep, map)):
			print(nextStep, " was in bounds")
			if (nextStep not in visitedCoords):
				return findKeyTile(nextStep, map, visitedCoords)
				

if __name__ == "__main__":
	print("searching")
		
	print(findKeyTile(p, map, visitedCoords))
	