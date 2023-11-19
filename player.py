import pygame
from entity import Entity
from weapon import Weapon

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites,num):
        super().__init__(groups)
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.num = num
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        self.status = ['none','none']
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

        # movement input
        if(self.num==0):
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status[0] = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status[0] = 'down'
            else:
                self.direction.y = 0
                self.status[0] = 'none'

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status[1] = 'right'
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status[1] = 'left'
            else:
                self.direction.x = 0
                self.status[1] = 'none'
            
            if keys[pygame.K_SPACE]:
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
        else:
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status[0] = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status[0] = 'down'
            else:
                self.direction.y = 0
                self.status[0] = 'none'

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status[1] = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status[1] = 'left'
            else:
                self.direction.x = 0
                self.status[1] = 'none'

    def animate(self):
        self.rect = self.image.get_rect(center = self.hitbox.center)
