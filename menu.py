
from Buttons import Button
import game
import settings
import pygame
import os

# Insializing pygame
pygame.font.init()
pygame.mixer.init()
pygame.init()

# Importing Game screens

# Button

# Constants


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


WIDTH, HEIGHT = 1300, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
BG_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'stars_texture.png')), (WIDTH, HEIGHT))


# Buttons
BUTTON_SIZE = (261, 68)

START_BTN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Start.png')), BUTTON_SIZE).convert_alpha()

START_HOV = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Start_hov.png')), BUTTON_SIZE).convert_alpha()

SETTING_BTN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Settings.png')), BUTTON_SIZE).convert_alpha()

SETTING_HOV = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Setting_hov.png')), BUTTON_SIZE).convert_alpha()

CONTROL_BTN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Controls.png')), BUTTON_SIZE).convert_alpha()

CONTROL_HOV = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Control_hov.png')), BUTTON_SIZE).convert_alpha()

QUIT_BTN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Quit.png')), BUTTON_SIZE).convert_alpha()

QUIT_HOV = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Quit_hov.png')), BUTTON_SIZE).convert_alpha()

MENU_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Menu-bg.png')), (282, 365)).convert_alpha()

MENU_HEADING = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Buttons\Menu-Heading.png')), BUTTON_SIZE).convert_alpha()

MENU_BG_LOCx, MENU_BG_LOCy = (WIDTH//2-(282//2), HEIGHT//2)  # (11,67)
LOGO_WIDTH, LOGO_HEIGTH = 650, 217
LOGO = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Logo.png')), (LOGO_WIDTH, LOGO_HEIGTH)).convert_alpha()

BACKGROUND_MUSIC = pygame.mixer.music.get_volume()


# Functions


start_btn = Button(MENU_BG_LOCx+11, MENU_BG_LOCy+67, START_BTN, START_HOV, WIN)
settings_btn = Button(MENU_BG_LOCx+11, MENU_BG_LOCy +
                      (67*2), SETTING_BTN, SETTING_HOV, WIN)
control_btn = Button(MENU_BG_LOCx+11, MENU_BG_LOCy +
                     (67*3), CONTROL_BTN, CONTROL_HOV, WIN)
quit_btn = Button(MENU_BG_LOCx+11, MENU_BG_LOCy +
                  (67*4), QUIT_BTN, QUIT_HOV, WIN)


def Menu_Draw():

    WIN.blit(BG_IMG, (0, 0))
    WIN.blit(MENU_BG, (MENU_BG_LOCx, MENU_BG_LOCy))
    WIN.blit(MENU_HEADING, (MENU_BG_LOCx+11, MENU_BG_LOCy+10))
    WIN.blit(LOGO, ((WIDTH//2)-(LOGO_WIDTH//2), 100))
    start_btn.Draw_btn()
    settings_btn.Draw_btn()
    control_btn.Draw_btn()
    quit_btn.Draw_btn()
    pygame.display.update()


def Main():
    pygame.mixer.music.play()

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if start_btn.Draw_btn():
                game.main()
            if settings_btn.Draw_btn():
                settings.Main()
            if control_btn.Draw_btn():
                print("Controls")
            if quit_btn.Draw_btn():
                print("Quit")
                pygame.quit()
        Menu_Draw()


if __name__ == "__main__":
    Main()
