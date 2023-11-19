import pygame
from entity import Entity
from weapon import Weapon

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, num, key_bindings):
        super().__init__(groups)
        
        self.key_bindings = key_bindings
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.num = num
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        self.status = ['none', 'none']
        self.obstacle_sprites = obstacle_sprites
        self.groups = groups
        self.speed = 5
        
    def create_attack(self):
        self.current_attack = Weapon(self.rect,self.status, groups=self.groups)

    def get_status(self):
        return self.status
    
    def update(self):
        self.input()
        # self.cooldowns()
        # self.get_status()
        self.animate()
        self.move(self.speed)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[self.key_bindings['up']]:
            self.direction.y = -1
            self.status[0] = 'up'
        elif keys[self.key_bindings['down']]:
            self.direction.y = 1
            self.status[0] = 'down'
        else:
            self.direction.y = 0
            self.status[0] = 'none'

        if keys[self.key_bindings['right']]:
            self.direction.x = 1
            self.status[1] = 'right'
        elif keys[self.key_bindings['left']]:
            self.direction.x = -1
            self.status[1] = 'left'
        else:
            self.direction.x = 0
            self.status[1] = 'none'

    def animate(self):
        self.rect = self.image.get_rect(center = self.hitbox.center)
