import pygame
import random
import math
from var import *

class Spritesheet:
	#class spritesheet will make it possible to load sheets of graphics, rather than individual ones
	def __init__(self, file):
		#initialize and set parameters of Spritesheet
		self.sheet = pygame.image.load(file).convert()
		
	def get_sprite(self, x, y, width, height):
		#Get_sprite method to select specific parts of entire sptiresheet
		sprite = pygame.Surface((width, height))
		sprite.blit(self.sheet, (0,0), (x, y, width, height)) 
		sprite.set_colorkey(BLACK)
		return sprite

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y): 
	#initialize class PLayer. game to access all variables in game. x and y for coords of player
	
		self.game = game
		self._layer = PLAYER_LAYER
		self.groups = self.game.all_sprites, self.game.player #adding player to all sprites group in main.py
		pygame.sprite.Sprite.__init__(self, self.groups) #calls init method for inherited class in Player
				
		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height	= TILE_SIZE
		
		self.x_change = 0
		self.y_change = 0
		
		self.facing = 'down'
		self.animation_loop = 1
		
		self.image = self.game.hero_spritesheet.get_sprite(0, 0, self.width, self.height)
		
		self.rect = self.image.get_rect() #this is the space of the player itself. which pixels belong to it like hit box
		self.rect.x = self.x
		self.rect.y = self.y
		
	def update(self):
		self.movement()
		self.animate()
		
		self.rect.x += self.x_change
		self.collide_blocks('x')
		self.collide_walls('x')

		self.rect.y += self.y_change
		self.collide_blocks('y')
		self.collide_walls('y')

		self.x_change = 0
		self.y_change = 0

	def movement(self):
		#create player movement upon pressing keys. 
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.x_change -= PLAYER_SPEED
			self.facing = 'left'
		if keys[pygame.K_RIGHT]:
			self.x_change += PLAYER_SPEED
			self.facing = 'right'
		if keys[pygame.K_UP]:
			self.y_change -= PLAYER_SPEED
			self.facing = 'up'		
		if keys[pygame.K_DOWN]:
			self.y_change += PLAYER_SPEED
			self.facing = 'down'
			
	def animate(self):
		#loop through hero sprites from hero_spritesheet in order to create animated look
		down_animations = [self.game.hero_spritesheet.get_sprite(0, 0, self.width, self.height), 
						self.game.hero_spritesheet.get_sprite(32, 0, self.width, self.height)]

		up_animations = [self.game.hero_spritesheet.get_sprite(96, 0, self.width, self.height), 
						self.game.hero_spritesheet.get_sprite(32, 96, self.width, self.height)]

		left_animations = [self.game.hero_spritesheet.get_sprite(0, 32, self.width, self.height), 
						self.game.hero_spritesheet.get_sprite(32, 32, self.width, self.height)]

		right_animations = [self.game.hero_spritesheet.get_sprite(0, 64, self.width, self.height), 
						self.game.hero_spritesheet.get_sprite(32, 64, self.width, self.height)]		

		if self.facing == 'down':
			if self.y_change == 0:
			#if no movement, static image hero
				self.image = self.game.hero_spritesheet.get_sprite(0, 0, self.width, self.height)
			else: 
			#use animation loop to filter through the previously determinted animation lists depending on direction facing
				self.image = down_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 2:
					self.animation_loop = 1

		if self.facing == 'up':
			if self.y_change == 0:
				self.image = self.game.hero_spritesheet.get_sprite(32, 96, self.width, self.height)
			else: 
				self.image = up_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 2:
					self.animation_loop = 1

		if self.facing == 'left':
			if self.x_change == 0:
				self.image = self.game.hero_spritesheet.get_sprite(0, 32, self.width, self.height)
			else: 
				self.image = left_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 2:
					self.animation_loop = 1
					
		if self.facing == 'right':
			if self.x_change == 0:
				self.image = self.game.hero_spritesheet.get_sprite(0, 64, self.width, self.height)
			else: 
				self.image = right_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 2:
					self.animation_loop = 1
			
	def collide_blocks(self, direction):
		#create player collisions with block tile

		if direction == "x":
			collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
			if collide:
				if self.x_change > 0:
					self.rect.x = collide[0].rect.left - self.rect.width
				if self.x_change < 0:
					self.rect.x = collide[0].rect.right
					
		if direction == "y":
			collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
			if collide:
				if self.y_change > 0:
					self.rect.y = collide[0].rect.top - self.rect.height
				if self.y_change < 0:
					self.rect.y = collide[0].rect.bottom
		
		if direction == "y":
			pass
			
	def collide_walls(self, direction):
		#create player collisions with wall tile in x and y directions
		if direction == "x":
			collide = pygame.sprite.spritecollide(self, self.game.walls, False)
			if collide:
				if self.x_change > 0:
					self.rect.x = collide[0].rect.left - self.rect.width
				if self.x_change < 0:
					self.rect.x = collide[0].rect.right
					
		if direction == "y":
			collide = pygame.sprite.spritecollide(self, self.game.walls, False)
			if collide:
				if self.y_change > 0:
					self.rect.y = collide[0].rect.top - self.rect.height
				if self.y_change < 0:
					self.rect.y = collide[0].rect.bottom
		
		if direction == "y":
			pass

class Princess(pygame.sprite.Sprite):
	def __init__(self, game, x, y): 
	#initialize class Princess. game to access all variables in game. x and y for coords of princess

		self.game = game
		self._layer = COIN_LAYER
		self.groups = self.game.all_sprites, self.game.coins
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height = TILE_SIZE
		
		self.x_change = 0
		self.y_change = 0
		
		self.image = self.game.princessCopperberry_spritesheet.get_sprite(0, 64, self.width, self.height)
		
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

class Coin(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
	#initialize class Coin. game to access all variables in game. x and y for coords of coin

		self.game = game
		self._layer = COIN_LAYER
		self.groups = self.game.all_sprites, self.game.coins
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height = TILE_SIZE
		
		self.image = self.game.coin_spritesheet.get_sprite(0, 0, self.width, self.height)
		
		self.animation_loop = 1
		
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		
	def update(self):
		self.collide_coin()
		self.animate()
		
	def animate(self):
		#loop through two coin sprites in order to create animated look

		animations = [self.game.coin_spritesheet.get_sprite(0, 0, self.width, self.height), 
						self.game.coin_spritesheet.get_sprite(0, 32, self.width, self.height)]

		self.image = animations[math.floor(self.animation_loop)]
		self.animation_loop += 0.1
		if self.animation_loop >= 2:
			self.animation_loop = 1
			
	def collide_coin(self):
	#check for collisions with tile coin and kill coin sprite upon collision with player
		global updated_map1_coins
		global updated_map2_coins
		global updated_map3_coins
		global updated_map4_coins

		collide = pygame.sprite.spritecollide(self, self.game.player, False)
		
		if collide:
			if self.game.tilemap == map1:
				if updated_map1_coins == 0:
					updated_map1_coins = map1_coins
					updated_map1_coins -= 1
				else:
					updated_map1_coins -= 1
				
			if self.game.tilemap == map2:
				if updated_map2_coins == 0:
					updated_map2_coins = map2_coins
					updated_map2_coins -= 1
				else:
					updated_map2_coins -= 1
				 
			if self.game.tilemap == map3:
				if updated_map3_coins == 0:
					updated_map3_coins = map3_coins
					updated_map3_coins -= 1
				else:
					updated_map1_coins -= 1
				
			if self.game.tilemap == map4:
				if updated_map4_coins == 0:
					updated_map4_coins = map4_coins
					updated_map4_coins -= 1
				else:
					updated_map4_coins -= 1
			
			self.kill()

class Block(pygame.sprite.Sprite):
	def __init__(self, game, x, y): 
	#initialize class Block. game to access all variables in game. x and y for coords of block tile
		
		self.game = game
		self._layer = BLOCK_LAYER
		self.groups = self.game.all_sprites, self.game.blocks
		pygame.sprite.Sprite.__init__(self, self.groups) #calling init method for inherited class pygame.sprites.Sprite #passing self.groups adds block class to sprite groups
		
		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height = TILE_SIZE
		
		self.image = self.game.terrain_spritesheet.get_sprite(0, 32, self.width, self.height)
		
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		
class Water(pygame.sprite.Sprite):
	def __init__(self, game, x, y): 
	#initialize class Water. game to access all variables in game. x and y for coords of water tile
		
		self.game = game
		self._layer = WATER_LAYER
		self.groups = self.game.all_sprites, self.game.water
		pygame.sprite.Sprite.__init__(self, self.groups) #calling init method for inherited class pygame.sprites.Sprite #passing self.groups adds block class to sprite groups
		
		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height = TILE_SIZE
		
		self.image = self.game.terrain_spritesheet.get_sprite(32, 32, self.width, self.height)
		
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

class Wall(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
	#initialize class wall. game to access all variables in game. x and y for coords of wall tile

		self.game = game
		self._layer = WALL_LAYER
		self.groups = self.game.all_sprites, self.game.walls
		pygame.sprite.Sprite.__init__(self, self.groups) #calling init method for inherited class pygame.sprites.Sprite #passing self.groups adds block class to sprite groups
		
		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height = TILE_SIZE
		
		self.image = self.game.terrain_spritesheet.get_sprite(32, 0, self.width, self.height)
		
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		
class Ground(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
	#initialize class ground. game to access all variables in game. x and y for coords of ground tile

		self.game = game
		self._layer = GROUND_LAYER
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups) #calling init method for inherited class pygame.sprites.Sprite #passing self.groups adds block class to sprite groups

		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height = TILE_SIZE
		
		self.image = self.game.terrain_spritesheet.get_sprite(32, 64, self.width, self.height)
		
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

class Nextlevel(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
	#initialize class nextLevel. game to access all variables in game. x and y for coords of nextLevel tile

		self.game = game
		self._layer = NEXTLVL_LAYER
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups) #calling init method for inherited class pygame.sprites.Sprite #passing self.groups adds block class to sprite groups

		self.x = x * TILE_SIZE
		self.y = y * TILE_SIZE
		self.width = TILE_SIZE
		self.height = TILE_SIZE
		
		self.image = self.game.terrain_spritesheet.get_sprite(0, 96, self.width, self.height)

		
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		
	def collide_nextLevel(self):
		#check for collisions with NextLevel tile
		collide = pygame.sprite.spritecollide(self, self.game.player, False)
		if collide:
				if self.game.tilemap == map1 and updated_map1_coins == 0:
					print(updated_map1_coins)
					self.game.new_game(map2)
				elif self.game.tilemap == map2 and updated_map2_coins == 0:
					self.game.new_game(map3)
				elif self.game.tilemap == map3 and updated_map3_coins == 0:
					self.game.new_game(map4)
				else:
					self.game.playing = False
					self.game.game_over()
				
	def update(self):
		self.collide_nextLevel()
		
class Button:
	def __init__(self, x, y, width, height, foreground, background, content, fontsize):
		#initialize class Button.

		self.font = pygame.font.Font('fantasyfont.ttf', fontsize)
		self.content = content
						
		self.x = x
		self.y = y
		self.width = width
		self.height = height
			
		self.foreground = foreground
		self.background = background
			
		self.image = pygame.Surface((self.width, self.height))
		self.image.fill(self.background)
		self.rect = self.image.get_rect()
		
		self.rect.x = self.x
		self.rect.y = self.y
			
		self.text = self.font.render(self.content, False, self.foreground)
		self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
		self.image.blit(self.text, self.text_rect)
	
	def pressed(self, position, pressed):
	#check is button had been pressed by user
		if self.rect.collidepoint(position):
			if pressed[0]: #in pygame.pressed 0 = left 1 = right and 2 = middle button 
				return True
			return False
		return False