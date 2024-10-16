import pygame

import constants
import player


def main():
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    # Delta time tracking
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    p1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(constants.RGB_BLACK)
        p1.update(dt)
        p1.draw(screen)
        pygame.display.flip()
        # Frames per second
        # Also dividing by 1000 to convert delta time to seconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
