import pygame

class Weapon(pygame.sprite.Sprite):

    def __init__(self,rect,status,groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'

        #graphic
        self.image = pygame.Surface((10,10))
        self.image.fill((0,255,0))

        #placement
        if status ==['right','none']:
            self.rect = self.image.get_rect(midleft = rect.midright + pygame.math.Vector2(-23,8))
        elif status == ['left','none']:
            self.rect = self.image.get_rect(midright = rect.midleft + pygame.math.Vector2(23,8))
        elif status == ['none','up']:
            self.rect = self.image.get_rect(midtop = rect.midbottom + pygame.math.Vector2(-10,-13))
        elif status == ['none','down']:
            self.rect = self.image.get_rect(midbottom = rect.midtop + pygame.math.Vector2(-10,13))
        elif status == ['right','up']:
            self.rect = self.image.get_rect(midright = rect.midleft + pygame.math.Vector2(23,8))
        elif status == ['left','up']:
            self.rect = self.image.get_rect(midtop = rect.midbottom + pygame.math.Vector2(-10,-13))
        elif status == ['right','down']:
            self.rect = self.image.get_rect(midbottom = rect.midtop + pygame.math.Vector2(-10,13))
        elif status == ['left','down']:
            self.rect = self.image.get_rect(midleft = rect.midright + pygame.math.Vector2(-23,8))
        else:
            self.rect = self.image.get_rect(center = rect.center)