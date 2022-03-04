import pygame
pygame.init()


class Map:
    def __init__(self, enemies):
        self.enemies = enemies

    def Draw_Map(self, window):
        for enemy in self.enemies:
            enemy.Draw_Enemy(window)

    def Move_map(self, x, y):
        for enemy in self.enemies:
            enemy.move_Enemy(y)


class Player:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

    def Draw_player(self, window):
        window.blit(self.skin, (self.x, self.y))

    def Mover_player(self, x):
        self.x += x


class Enemy:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

    def Draw_Enemy(self, window):
        window.blit(self.skin, (self.x, self.y))

    def move_Enemy(self, y_move):
        self.y += y_move
