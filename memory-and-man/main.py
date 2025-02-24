import pygame
from conventions import Point
from world import World


def main():
    pygame.init()
    running = True

    world = World()
    world.create_screen()

    starting_player_pos = Point((width * .4, height * .5))
    starting_beast_pos = Point((width * .6, height * .5))

    player = Player(screen)
    player.pos = starting_player_pos
    beast = Beast(screen)
    beast.pos = starting_beast_pos


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        screen.fill((10,10,10))

        beast.draw()
        player.draw()

        beast.move_towards(player.pos)
        player.move_towards(Point(pos=pygame.mouse.get_pos()))

        pygame.display.flip()

        dt = clock.tick(120) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()