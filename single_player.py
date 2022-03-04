import pygame
import os


import player_movement
# Insializing pygame
pygame.init()

WIDTH, HEIGHT = 1300, 800
SHIP_SIZE = (200, 200)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

BG_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'stars_texture.png')), (WIDTH, HEIGHT))

PLAYER_SHIP_1 = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(
    os.path.join('Assets\Ships', 'InfraredFurtive.png')),  180), SHIP_SIZE)

PLAYER_SHIP_2 = pygame.transform.rotate(pygame.image.load(
    os.path.join('Assets\Ships', 'Transtellar.png')), 180)

ENEMY_SHIP_1 = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(
    os.path.join('Assets\Ships', 'Warship.png')),  180), SHIP_SIZE)

ENEMY_SHIP_2 = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(
    os.path.join('Assets\Ships', 'InterstellarRunner.png')), 180), SHIP_SIZE)


enemy1 = player_movement.Enemy(100, -50, ENEMY_SHIP_1)
enemy2 = player_movement.Enemy(300, -50, ENEMY_SHIP_2)
enemy3 = player_movement.Enemy(500, -50, ENEMY_SHIP_1)
player = player_movement.Player(
    600-(100), 600, PLAYER_SHIP_1)

map = player_movement.Map([enemy1, enemy2, enemy3])


def Main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        WIN.blit(BG_IMG, (0, 0))
        player.Draw_player(WIN)
        map.Draw_Map(WIN)
        map.Move_map(0, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player.Mover_player(-5)
        if keys[pygame.K_d]:
            player.Mover_player(5)

        pygame.display.update()


if __name__ == "__main__":
    Main()
