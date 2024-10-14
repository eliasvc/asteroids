import pygame

import constants


def main():
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    # Delta time tracking
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(constants.RGB_BLACK)
        # Frames per second
        # Also dividing by 1000 to convert delta time to seconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
