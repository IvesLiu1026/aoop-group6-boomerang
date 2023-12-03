import pygame
from settings import *
from entity import Entity
from support import *

class Boomerang(Entity):
	def __init__(self,x,y,groups,obstacle_sprites,attack_sprites):
		# general setup
		super().__init__(groups)
		self.sprite_type = 'boom'

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


	def actions(self,player):
			self.direction.x = 1
			self.direction.y = 1
	def check_death(self):
		if self.health <= 0:
			self.kill()

	def update(self):
		self.check_death()
		self.move(self.speed)
		#self.animate()
		

	def boomerang_update(self,player):
		self.actions(player)