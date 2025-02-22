from ctypes.wintypes import RGB
from player import Player
import pygame
from pygame.locals import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0 # delta time
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # GAME LOOP
    while True:
        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # BACKGROUND BLACK
        screen.fill(RGB(0,0,0))
        player.update(dt)
        player.draw(screen)
        # DISPLAY GAME
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        
    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
