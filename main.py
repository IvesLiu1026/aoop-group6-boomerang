import pygame
from default_config import *

from player import Player

config = {
    "resolution": RESOLUTION,
    "fps": FPS,
    "title": TITLE
}

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
        check_running = lambda: \
            not (pygame.QUIT in 
                 [event.type for event in pygame.event.get()])
        clock = pygame.time.Clock()

        all_sprites = pygame.sprite.Group()
        obstacle_sprites = pygame.sprite.Group()
        player = Player(pos=(0, 0), groups=(all_sprites), obstacle_sprites=obstacle_sprites)
        all_sprites.add(player)

        while running:
            clock.tick(self.fps)
            
            running = check_running()

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT: 
            #         running = False
            #     elif event.type == pygame.KEYDOWN:
            #         # WASD
            #         if event.key == pygame.K_w:
            #             ...
            #         elif event.key == pygame.K_a:
            #             ...
            #         elif event.key == pygame.K_s:
            #             ...
            #         elif event.key == pygame.K_d:
            #             ...

            all_sprites.update()

            self.window.fill((255, 255, 255))
            all_sprites.draw(self.window)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game(config=config)
    game.run()