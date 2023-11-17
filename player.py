import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.obstacle_sprites = obstacle_sprites

        self.speed = 5

    def update(self):
        self.input()
        # self.cooldowns()
        # self.get_status()
        self.animate()
        self.move(self.speed)

    def input(self):
        keys = pygame.key.get_pressed()

        # movement input
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def animate(self):
        self.rect = self.image.get_rect(center = self.hitbox.center)
