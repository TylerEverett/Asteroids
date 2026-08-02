import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH - 1, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0.0
    
    while running:
        # call to logger.py to get game state logs 
        log_state()

        # processing pygame event queue
        # quit allows to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen with black
        # also wipes anything from last frame
        screen.fill("black")

        # flip() allows display to put game data on screen 
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
