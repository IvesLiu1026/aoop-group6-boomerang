import pygame
from default_config import *

config = {
    "resolution": RESOLUTION,
    "fps": FPS,
    "title": TITLE
}

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        # self.rect.x, self.rect.y = 200, 200
        self.rect.center = (200, 200)
    
    def update(self):
        self.rect.x += 10 
        if self.rect.x > config['resolution'][0]:
            self.rect.x = 0

class Game:
    def __init__(self, config):
        pygame.init()
        pygame.display.set_caption(config['title'])
        self.window = pygame.display.set_mode(config['resolution'])
        self.fps = config['fps']
        
        self.window.fill((255, 255, 255))
        # self.clock = pygame.time.Clock()
        # self.running = True
        
        # self.playing = False
        # self.current_fps = 0
        # self.current_time = 0
    
    def run(self):
        running = True
        clock = pygame.time.Clock()

        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)

        while running:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # WASD
                    if event.key == pygame.K_w:
                        ...
                    elif event.key == pygame.K_a:
                        ...
                    elif event.key == pygame.K_s:
                        ...
                    elif event.key == pygame.K_d:
                        ...

            all_sprites.update()

            self.window.fill((255, 255, 255))
            all_sprites.draw(self.window)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game(config=config)
    game.run()