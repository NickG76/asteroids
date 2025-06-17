import pygame
from constants import *

def main():
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        pygame.display.flip()
        dt += pygame.time.Clock().tick(60) / 1000
        print(f"Delta Time: {dt:.2f} seconds")
    

if __name__ == "__main__":
    main()
