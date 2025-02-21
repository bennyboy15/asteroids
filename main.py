from ctypes.wintypes import RGB
import pygame
from pygame.locals import *
from constants import *

def main():
    game = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # GAME LOOP
    while True:
        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # BACKGROUND BLACK
        screen.fill(RGB(0,0,0))
        # DISPLAY GAME
        pygame.display.flip()
    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
