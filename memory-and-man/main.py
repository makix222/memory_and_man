import pygame
from conventions import Point
from character import Player, Beast

def main():
    pygame.init()
    width = 1200
    height = 800
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    starting_player_pos = Point((width * .4, height * .5))
    starting_beast_pos = Point((width * .6, height * .5))
    print(starting_beast_pos, starting_player_pos)

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

        screen.fill((80,80,80))

        beast.draw()
        player.draw()

        beast.move_towards(player.pos)
        player.move_towards(Point(pos=pygame.mouse.get_pos()))

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()