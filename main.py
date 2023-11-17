import pygame
from default_config import *

class Game:
    def __init__(self, config):
        pygame.init()
        pygame.display.set_caption(config['title'])
        self.window = pygame.display.set_mode(config['resolution'])
        self.window.fill((255, 255, 255))
        
        self.fps = config['fps']
        self.clock = pygame.time.Clock()
        # self.running = True
        
        # self.playing = False
        # self.current_fps = 0
        # self.current_time = 0
    
    def run(self):
        # Game loop
        running = True

        while running:
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
                    ...

        pygame.quit()


if __name__ == "__main__":
    game = Game({
        "resolution": RESOLUTION,
        "fps": FPS,
        "title": TITLE
    })
    game.run()