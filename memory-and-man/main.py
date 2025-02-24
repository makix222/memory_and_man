import pygame
from conventions import Point
from character import Player, Beast

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    starting_player_pos = Point((screen.get_width() * 7/10,
                                screen.get_height() * 1/2))
    starting_beast_pos = Point((screen.get_width() * 2/10,
                                screen.get_height() * 1/2))
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
        # breakpoint()
        beast.draw()
        player.draw()

        # beast.pos.x += 1
        # player.pos.x += 1
        player.move_towards(beast.pos)
        beast.move_towards(player.pos)
        # player.move_towards(Point(pos=pygame.mouse.get_pos()))

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()