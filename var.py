import pygame

#window
windowWidth = 640
windowHeight = 480
FPS = 60

#layers
BACK_BUTTON_LAYER = 5
INVENTORY_LAYER = 5
PLAYER_LAYER = 4
COIN_LAYER = 3
NEXTLVL_LAYER = 3
WATER_LAYER = 1
WALL_LAYER = 2
BLOCK_LAYER = 2
GROUND_LAYER = 1

#player 
PLAYER_SPEED = 2

#inventory
MAX_SLOTS = 5
MAX_STACK_SIZE = 10


#colours
RED = (255,0,0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (205, 127, 50)
GREEN = (0, 255, 0)
PURPLE = (186,85,211)
PINK = (219,112,147)
WHITE = (255, 255, 255)
ORANGE = (255, 172, 28)

#maps and tiles
TILE_SIZE = 32

map1 = [
	'....................',
	'WWWWWWWWWWWWWWWWWWWW',
	'W..AAA.BBB.........W',
	'W....C.............W',
	'W..................W',
	'W..........P.......W',
	'W..AA..............W',
	'W..AAA.......C.....W',
	'W..................W',
	'W.....BB.....AAA...W',
	'W......BB......N...W',
	'W..................W',
	'W...C........C.....W',
	'W..................W',
	'WWWWWWWWWWWWWWWWWWWW'
]

map1_coins = 4
updated_map1_coins = 4


map2 = [
	'....................',
	'WWWWWWWWWWWWWWWWWWWW',
	'W.P..........C.....W',
	'W.BBBBBBBBBBBBB.B..W',
	'W.B....C........B..W',
	'W.BBBBB.BBBBB......W',
	'WCB....B.....B.....W',
	'W.BBBB.BBBBB.......W',
	'W.......C.....B.B..W',
	'W.BBBBBBBBBBBBBBB..W',
	'W..AAAAAAAAAAC.....W',
	'W.BBBBBBBBBBBBBBBBBW',
	'W...ABBAAAABBAAAABNW',
	'WBBB.C..BB....BB...W',
	'WWWWWWWWWWWWWWWWWWWW'
]

map2_coins = 6
updated_map2_coins = 6


map3 = [
	'....................', 
	'WWWWWWWWWWWWWWWWWWWW', 
	'W.BP........B.....CW',
	'WAB....B....B..B...W', 
	'W.BBBBBBBB..B..BBB.W', 
	'W.B...BC.B..BBBBC..W',
	'W.....B..BAAAAAB...W', 
	'WA..BBB..BBBB..B...W', 
	'W.C........BB......W',
	'W...B..B...........W', 
	'W..BBBBBB....BBB...W', 
	'WAAB.........C.....W',
	'W..BBBBBBB..BBBBBB.W', 
	'W.....C.AAA.B..N...W', 
	'WWWWWWWWWWWWWWWWWWWW'
]

map3_coins = 7
updated_map3_coins = 7


map4 = [
	'....................', 
	'WWWWWWWWWWWWWWWWWWWW', 
	'WBBBBBBBBBBBBBBBP.BW',
	'W.......BB.....B..BW', 
	'W..BBBB....BB.....BW', 
	'W......BBBBBBBBBBBBW',
	'W..C.............C.W', 
	'W...B...........B..W', 
	'W....B.........B...W',
	'W.....B...C...B....W', 
	'W......B.....B.....W', 
	'W.......B...B......W',
	'W.........G........W', 
	'W..................W', 
	'WWWWWWWWWWWWWWWWWWWW'
]

map4_coins = 7
updated_map4_coins = 7

x = 30
y = 30
width = 60
height = 60


