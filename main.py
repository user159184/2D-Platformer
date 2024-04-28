import pygame
import sys
from sprites import *
from var import * 

class Game: 
	#GAME OBJECT
	def __init__(self):
		#initialize class Game
		pygame.init()
		self.screen = pygame.display.set_mode((windowWidth, windowHeight))
		self.clock = pygame.time.Clock()
		self.running = True
		self.font = pygame.font.Font('fantasyfont.ttf', 60)
		
		self.hero_spritesheet = Spritesheet('./img/heroSpritesheet.png')
		self.terrain_spritesheet = Spritesheet('./img/terrain_spriteSheet.png')
		self.princessCopperberry_spritesheet = Spritesheet('./img/princessDidi_spriteSheet.png')
		self.coin_spritesheet = Spritesheet('./img/coin_spriteSheet.png')
		
		self.mainMenu_background = pygame.image.load('./img/mainMenu_background.png')
		self.levels_page_background = pygame.image.load('./img/characterSelection_background.png')
		self.helpPage_background = pygame.image.load('./img/helpPage_background.png')
		self.game_over_background = pygame.image.load('./img/game_over_background.png')
		
	def create_tilemap(self, map):
		#Create tilemap by reading provided map, assigning characters to terrain classes, creating tiles. 
		self.tilemap = map
		for i , row in enumerate(self.tilemap): #enumerate grants not only position (i) but value (row) in list tilemap
			for j, column in enumerate(row):
				Ground(self, j, i)
				if column == "B":
					Block(self, j, i) #j is x positon, i is y position
				if column == "W":
					Wall(self, j, i)
				if column == "C":
					Coin(self, j, i)
				if column == "N":
					Nextlevel(self, j, i)
				if column == "G":
					Princess(self, j, i)	
				if column == "A":
					Water(self, j, i)	
				if column == "P":
					Player(self, j, i)		
	
	def new_game(self, map): 
		#new game start
		self.playing = True
		
		self.all_sprites = pygame.sprite.LayeredUpdates() #create group of all sprites and make it possible to update them all at once
		self.player = pygame.sprite.LayeredUpdates()
		self.nextlevel = pygame.sprite.LayeredUpdates()
		self.blocks = pygame.sprite.LayeredUpdates() 
		self.coins = pygame.sprite.LayeredUpdates() 
		self.walls = pygame.sprite.LayeredUpdates() 
		self.water = pygame.sprite.LayeredUpdates() 

		self.create_tilemap(map)
		
	def events(self): 
		#game loop events
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
	
	def update(self): 
		#game loop updates
		self.all_sprites.update()
	
	def draw(self):
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		self.clock.tick(FPS)
		
	def main(self): 
		#game loop
		while self.playing:
			pygame.display.set_caption("Game")
			
			mouse_position = pygame.mouse.get_pos()
			mouse_pressed = pygame.mouse.get_pressed()
			
			back_button = Button(0, 0, 80, 32, WHITE, BROWN, 'Back', 29)
			
			if back_button.pressed(mouse_position, mouse_pressed):
				self.playing = False
				self.levels_page()
			
			self.screen.blit(back_button.image, back_button.rect)

			pygame.display.update()

			self.events() #each event. ex: key press
			self.update() #update game screen
			self.draw() #display all sprites on screen
	
	
	def main_menu(self):
		#main menu loop 
		main_menu = True
		
		while main_menu:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					main_menu = False
					self.running = False
			
			pygame.display.set_caption("Menu")
			title = self.font.render('Copperberry Quest', False, ORANGE)
			title_rect = title.get_rect(center=(windowWidth/2, 50))
		
			start_button = Button(10, 100, 100, 50, WHITE, BROWN, 'Start', 32)
			help_button = Button(10, 250, 100, 50, WHITE, BROWN, 'Help', 32)
			quit_button = Button(10, 400, 100, 50, WHITE, BROWN, 'Quit', 32)
			
			mouse_position = pygame.mouse.get_pos()
			mouse_pressed = pygame.mouse.get_pressed() #funtion returns a list. 0 = left click 1 = right click 2 = middle click
			
			if start_button.pressed(mouse_position, mouse_pressed):
				main_menu = False
				self.levels_page()
				
			if help_button.pressed(mouse_position, mouse_pressed):
				self.help_page()
				
			if quit_button.pressed(mouse_position, mouse_pressed):
				main_menu = False
				self.running = False
			
			self.screen.blit(self.mainMenu_background, (0,0))
			self.screen.blit(title, title_rect)
			self.screen.blit(start_button.image, start_button.rect)
			self.screen.blit(help_button.image, help_button.rect)
			self.screen.blit(quit_button.image, quit_button.rect)

			self.clock.tick(FPS)
			pygame.display.update()

	def levels_page(self):
		#levels page loop. choose which map will be played here.
		levels_page = True
		
		while levels_page:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					levels_page = False
					self.running = False
			
			pygame.display.set_caption("Levels Page")
		
			title = self.font.render('Choose Your Level', False, ORANGE)
			title_rect = title.get_rect(center=(windowWidth/2, 50))
		
			back_button = Button(0, 0, 80, 32, WHITE, BROWN, 'Back', 29)
			level1_button = Button(100, 90, 80, 32, WHITE, BROWN, 'Level 1', 29)
			level2_button = Button(100, 150, 80, 32, WHITE, BROWN, 'Level 2', 29)
			level3_button = Button(100, 210, 80, 32, WHITE, BROWN, 'Level 3', 29)

			mouse_position = pygame.mouse.get_pos()
			mouse_pressed = pygame.mouse.get_pressed() 
			
			if back_button.pressed(mouse_position, mouse_pressed):
				levels_page = False
				self.main_menu()
			
			if level1_button.pressed(mouse_position, mouse_pressed):
				levels_page = False
				self.new_game(map1)
				number_of_coins = map1_coins
				self.main()
			
			if level2_button.pressed(mouse_position, mouse_pressed):
				levels_page = False
				self.new_game(map2)
				number_of_coins = map2_coins
				self.main()
				
			if level3_button.pressed(mouse_position, mouse_pressed):
				levels_page = False
				self.new_game(map3)
				self.main()			
			
			self.screen.blit(self.levels_page_background, (0,0)) 
			self.screen.blit(title, title_rect)
			self.screen.blit(back_button.image, back_button.rect)
			self.screen.blit(level1_button.image, level1_button.rect)
			self.screen.blit(level2_button.image, level2_button.rect)
			self.screen.blit(level3_button.image, level3_button.rect)

			self.clock.tick(FPS)
			pygame.display.update()

	def help_page(self):
		#help page loop. Includes game instructions
		help_page = True
		
		while help_page:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					help_page = False
					self.running = False
			
			pygame.display.set_caption("Help Page")
		
			title = self.font.render('How To Play', False, ORANGE)
			title_rect = title.get_rect(center=(windowWidth/2, 50))
		
			back_button = Button(0, 0, 80, 32, WHITE, BROWN, 'Back', 29)

			mouse_position = pygame.mouse.get_pos()
			mouse_pressed = pygame.mouse.get_pressed() 
			
			if back_button.pressed(mouse_position, mouse_pressed):
				help_page = False
			
			self.screen.blit(self.helpPage_background, (0,0)) 
			self.screen.blit(title, title_rect)
			self.screen.blit(back_button.image, back_button.rect)

			self.clock.tick(FPS)
			pygame.display.update()

	def game_over(self):
		#game over loop. stop new game.
		text = self.font.render("Game over!", False, RED)
		text_rect = text.get_rect(center=(windowWidth/2, windowHeight/2))

		restart_button = Button(10, windowHeight - 60, 120, 50, WHITE, BROWN, 'Restart', 32)
		
		for sprite in self.all_sprites:
			sprite.kill()
			
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					
			mouse_position = pygame.mouse.get_pos()
			mouse_pressed = pygame.mouse.get_pressed() 
			
			if restart_button.pressed(mouse_position, mouse_pressed):
				self.levels_page()

			self.screen.blit(self.game_over_background, (0,0))
			self.screen.blit(text, text_rect)
			self.screen.blit(restart_button.image, restart_button.rect)
			self.clock.tick(FPS)
			pygame.display.update()

g = Game()
g.main_menu()
while g.running:
	g.main()
	
pygame.quit()
sys.exit()