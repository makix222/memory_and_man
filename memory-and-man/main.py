import pygame
from game import Game
from enums import UserEvents


def main():
    pygame.init()
    running = True

    game = Game()
    game.create_screen()
    game.create_characters()

    while running:

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        game.update()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()