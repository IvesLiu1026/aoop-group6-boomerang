import pygame
from settings import *
from random import randint
from entity import Entity
from boomerang import Boomerang

class MagicPlayer:
	def __init__(self,animation_player):
		self.next_attack = True
		self.animation_player = animation_player
		self.sounds = {
		'heal': pygame.mixer.Sound('./audio/heal.wav'),
		'flame':pygame.mixer.Sound('./audio/Fire.wav')
		}
	def get_next_attack(self):
		return self.next_attack
	
	def attack(self,player,groups):
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
			if((direction.x!=0.0)|(direction.y!=0.0)):
				offset_x = (direction.x * 1) * TILESIZE
				offset_y = (direction.y * 1) * TILESIZE
				x = player.rect.centerx + offset_x #+ randint(-TILESIZE // 3, TILESIZE // 3)
				y = player.rect.centery + offset_y #+ randint(-TILESIZE // 3, TILESIZE // 3)
				self.boom = Boomerang(
									x,y,
									groups,
									groups[1],direction,player)
