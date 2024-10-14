import pygame

import constants


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(constants.RGB_BLACK)


if __name__ == "__main__":
    main()
