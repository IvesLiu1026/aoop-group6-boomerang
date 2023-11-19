import pygame, sys, button
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
        self.screen = pygame.Surface((1600, 900))
        self.window = pygame.display.set_mode(config['resolution'])
        self.fps = config['fps']
        
        self.screen.fill((255, 255, 255))
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
        player0 = Player(pos=(800, 450), groups=(all_sprites), obstacle_sprites=obstacle_sprites, num = 0, key_bindings = {
            'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d, 'attack': pygame.K_SPACE
        })
        player1 = Player(pos=(0, 0), groups=(all_sprites), obstacle_sprites=obstacle_sprites, num = 1, key_bindings = {
            'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'attack': pygame.K_RCTRL
        })
        all_sprites.add(player0)
        all_sprites.add(player1)
        
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
            
            self.screen.fill((255, 255, 255))
            all_sprites.draw(self.screen)
            
            resized_screen = pygame.transform.scale(self.screen, config['resolution']) 
            self.window.blit(resized_screen, (0, 0))
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game(config=config)
    game.run()