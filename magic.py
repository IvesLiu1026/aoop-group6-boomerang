import pygame
from settings import *
from random import randint

class MagicPlayer:
	def __init__(self,animation_player):
		self.animation_player = animation_player
		self.sounds = {
		'heal': pygame.mixer.Sound('./audio/heal.wav'),
		'flame':pygame.mixer.Sound('./audio/Fire.wav')
		}

	def heal(self,player,strength,cost,groups):
		if player.energy >= cost:
			self.sounds['heal'].play()
			player.health += strength
			player.energy -= cost
			if player.health >= player.stats['health']:
				player.health = player.stats['health']
			self.animation_player.create_particles('aura',player.rect.center,groups)
			self.animation_player.create_particles('heal',player.rect.center,groups)

	def flame(self,player,cost,groups):
			player.energy -= cost
			self.sounds['flame'].play()
			if player.dir == [2,0]: direction = pygame.math.Vector2(1,0) # right
			elif player.dir == [2,1]: direction = pygame.math.Vector2(-1,0) # left
			elif player.dir == [0,2]: direction = pygame.math.Vector2(0,-1) # up
			elif player.dir == [0,0]: direction = pygame.math.Vector2(1,-1) # up right
			elif player.dir == [0,1]: direction = pygame.math.Vector2(-1,-1) # up left
			elif player.dir == [1,0]: direction = pygame.math.Vector2(1,1) # down right
			elif player.dir == [1,1]: direction = pygame.math.Vector2(-1,1) # down left
			elif player.dir == [1,2]: direction = pygame.math.Vector2(0,1) # down
			else : direction = pygame.math.Vector2(0,0)
			for i in range(1,5):
				if((direction.x!=0.0)|(direction.y!=0.0)):
					offset_x = (direction.x * i) * TILESIZE
					offset_y = (direction.y * i) * TILESIZE
					x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('flame',(x,y),groups)