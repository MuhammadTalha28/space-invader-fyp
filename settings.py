import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import menu
from Buttons import Button
import game

pygame.font.init()
pygame.mixer.init()
pygame.init()


# constants
SETTINGS_FONT = pygame.font.SysFont('comicsans', 30)
TEXT_COLOR = (128, 128, 128)
WIDTH, HEIGHT = 1300,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
MUSIC_VOL = 0.5
SOUND_VOL = 0.5
HEALTH = 50
BACKGROUND_MUSIC = pygame.mixer.music.load('Assets\Music\spaceinvaders2.wav')
BACK_BTN = pygame.transform.scale(pygame.image.load(
    'Assets\Buttons\Back.png').convert_alpha(), (60, 60))
pygame.mixer.music.set_volume(MUSIC_VOL)

back_btn = Button(10, 10, BACK_BTN, BACK_BTN, WIN)
BG= pygame.transform.scale(pygame.image.load(
    'space_breaker_asset\Background\stars_texture.png').convert_alpha(), (1300, 800))


def Set_Draw():
    music_text = SETTINGS_FONT.render("Music Volume: ", 1, TEXT_COLOR)
    WIN.blit(BG, (0, 0))
    sound_text = SETTINGS_FONT.render("Sound Volume: ", 1, TEXT_COLOR)
    back_btn.Draw_btn()
    WIN.blit(music_text, (20, 85))
    WIN.blit(sound_text, (20, 235))

def Main():
    pygame.mixer.music.play()
    slider_music = Slider(WIN, 250, 100, WIDTH-350, 20, min=0,
                          max=100, step=1, handleColour=(0, 255, 200))

    slider_sound = Slider(WIN, 250, 250, WIDTH-350, 20, min=0,
                          max=100, step=1, handleColour=(0, 255, 200))

    music_output = TextBox(WIN, WIDTH-70, 85, 50, 50, fontSize=30)
    sound_output = TextBox(WIN, WIDTH-70, 235, 50, 50, fontSize=30)

    music_output.disable()
    sound_output.disable()
    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
            if back_btn.Draw_btn():
                menu.Main()


        

        MUSIC_VOL = slider_music.getValue()/100
        SOUND_VOL = slider_sound.getValue()/100
        pygame.mixer.music.set_volume(MUSIC_VOL)
        pygame.mixer.Sound.set_volume(game.BULLET_HIT_SOUND, SOUND_VOL)
        pygame.mixer.Sound.set_volume(game.ROCKET_HIT_SOUND, SOUND_VOL)
        pygame.mixer.Sound.set_volume(game.BULLET_SHOOT_SOUND, SOUND_VOL)
        pygame.mixer.Sound.set_volume(game.ROCKET_SHOOT_SOUND, SOUND_VOL)

        music_output.setText(slider_music.getValue())
        sound_output.setText(slider_sound.getValue())

        Set_Draw()
        pygame_widgets.update(events)
        pygame.display.update()


if __name__ == "__main__":
    Main()
