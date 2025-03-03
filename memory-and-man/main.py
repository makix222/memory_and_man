import pygame
from game import Game


def main():
    pygame.init()
    running = True

    game = Game()
    game.create_characters()

    while running:

        game.update()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False



        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()