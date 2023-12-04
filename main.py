import pygame, sys
from settings import *
from level import Level

from debug import debug, debug_init

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		# self.screen = pygame.display.set_mode(RESOLUTION)
		# pygame.display.set_caption('Zelda')
		self.screen = pygame.Surface((2048, 1152)) # 32 * 18
		# self.screen = pygame.Surface((1024, 576))

		if FULLSCREEN:
			self.resolution = pygame.display.list_modes()[0]
			self.window = pygame.display.set_mode(self.resolution, pygame.FULLSCREEN)
		else: 
			self.resolution = RESOLUTION
			self.window = pygame.display.set_mode(self.resolution, 0)
        
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()

		self.level = Level(screen=self.screen)

		icon = pygame.image.load('./graphics/monsters/bamboo/attack/0.png')
		pygame.display.set_icon(icon)

		# sound 
		main_sound = pygame.mixer.Sound('./audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

		debug_init(self.screen)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			# debug(f'{self.resolution}')
			resized_screen = pygame.transform.scale(self.screen, self.resolution) 
			self.window.blit(resized_screen, (0, 0))
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()