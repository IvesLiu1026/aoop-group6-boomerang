import pygame
from settings import *
from entity import Entity
from support import *
from math import sin

class Boomerang(Entity):
	def __init__(self,x,y,groups,obstacle_sprites,attack_sprites,direc):
		# general setup
		super().__init__(groups)
		self.sprite_type = 'projectile'
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
		# movement
		#self.rect = self.image.get_rect(topleft = pos)
		#self.hitbox = self.rect.inflate(0,-10)
		self.attack_sprites = attack_sprites
		self.obstacle_sprites = obstacle_sprites
		# stats
		self.speed = 20
		self.attack_damage = 100
		self.health = 100
		self.next_attack = False

		# player interaction
		self.can_attack = True
		self.attack_time = None
		self.attack_cooldown = 400

		# invincibility timer

		# sounds
		self.hit_sound = pygame.mixer.Sound('./audio/hit.wav')
		self.hit_sound.set_volume(0.6)
	def move(self,x,y):
		self.hitbox.x = self.hitbox.x + x
		self.hitbox.y = self.hitbox.y + y
		self.rect.center = self.hitbox.center
	
	def getspeed(self,player):
		if self.speed > 0:
			self.speed = self.speed-0.5
		else:
			self.speed = -20
	

	def get_next_attack(self):
		return self.next_attack


	def actions(self,player,speed):
			if((self.direc.x!=0.0 )&(self.direc.y!=0.0)):
				self.direction.x = speed*0.7*self.direc.x
				self.direction.y = speed*0.7*self.direc.y
			else:
				self.direction.x = speed*self.direc.x
				self.direction.y = speed*self.direc.y
	def check_death(self):
		if self.rect.centerx > 1960 or self.rect.centerx < 0 or self.rect.centery >  1060 or self.rect.centery < 0:
			self.next_attack = True
			self.kill()

	def update(self):
		self.check_death()
		self.move(self.direction.x,self.direction.y)
		#self.animate()

	def boomerang_update(self,player):
		self.getspeed(player)
		self.actions(player,self.speed)