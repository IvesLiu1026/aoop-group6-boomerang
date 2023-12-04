import pygame
from settings import *
from entity import Entity
from support import *
from math import sin

class Boomerang(Entity):
	def __init__(self,x,y,groups,obstacle_sprites,attack_sprites,direc):
		# general setup
		super().__init__(groups)
		self.sprite_type = 'boom'
		self.direc = direc
		# graphics setup
		#self.import_graphics(monster_name)
		#self.status = 'idle'
		#self.image = self.animations[self.status][self.frame_index]
		full_path = f'./graphics/weapons/axe/full.png'
		self.image = pygame.image.load(full_path).convert_alpha()
		#self.image = pygame.Surface((50, 50))
		self.rect = self.image.get_rect(topleft = (x,y))
		self.hitbox = self.rect.inflate(0,-10)
		self.speed = 20
		# movement
		#self.rect = self.image.get_rect(topleft = pos)
		#self.hitbox = self.rect.inflate(0,-10)
		self.attack_sprites = attack_sprites
		self.obstacle_sprites = obstacle_sprites
		# stats
		self.speed = 1
		self.attack_damage = 100
		self.health = 100

		# player interaction
		self.can_attack = True
		self.attack_time = None
		self.attack_cooldown = 400

		# invincibility timer

		# sounds
		self.hit_sound = pygame.mixer.Sound('./audio/hit.wav')
		self.hit_sound.set_volume(0.6)
	def movve(self,x,y):
		self.hitbox.x = self.hitbox.x + x
		self.hitbox.y = self.hitbox.y + y
		self.rect.center = self.hitbox.center
	
	

	def wave_value(self):
		value = sin(pygame.time.get_ticks())
		if value >= 0: 
			return 255
		else: 
			return 0


	def actions(self,player,speed):
			if((self.direc.x!=0.0 )&(self.direc.y!=0.0)):
				self.direction.x = speed*0.7*self.direc.x
				self.direction.y = speed*0.7*self.direc.y
			else:
				self.direction.x = speed*self.direc.x
				self.direction.y = speed*self.direc.y
			self.direction.normalize()
	def check_death(self):
		if self.rect.centerx > 1600 or self.rect.centerx < 0 or self.rect.centery > 900 or self.rect.centery < 0:
			self.kill()

	def update(self):
		self.check_death()
		self.movve(self.direction.x,self.direction.y)
		#self.animate()
		

	def boomerang_update(self,player):
		self.actions(player,self.speed)