import pygame
import settings
import menu
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

# CONSTANTS
WIDTH, HEIGHT = 1300, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 'Reliving the childhood'")
TEXT_COLOR = (255, 255, 255)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
SHIP_WIDTH, SHIP_HEIGHT = 90, 80


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 90)


RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 270)

MOVEMENT_SPEED = 15
BULLET_SPEED = 25
ROCKET_SPEED = 17
MAX_BULLETS = 2
MAX_ROCKETS = 1
RED_BULLET_COLOR = (255, 0, 0)
YELLOW_BULLET_COLOR = (255, 255, 0)

BORDER = pygame.Rect((WIDTH//2)-2.5, 0, 5, HEIGHT)
BORDER_COLOR = (0, 0, 0)


SPACE_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'stars_texture.png')), (WIDTH, HEIGHT))

GALAXY = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'galaxy.png')), (200, 200))

# USER EVENTS

YELLOW_HIT_BULLET = pygame.USEREVENT + 1
RED_HIT_BULLET = pygame.USEREVENT + 2
YELLOW_HIT_ROCKET = pygame.USEREVENT + 3
RED_HIT_ROCKET = pygame.USEREVENT + 4

# Sounds
BULLET_SHOOT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'bullet.wav'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'bullet_hit.mp3'))
ROCKET_SHOOT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'rocket.wav'))
ROCKET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'bullet_hit.mp3'))

# FUNCTIONS


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, red_rocket, yellow_rocket):  # Drawing on screen
    WIN.blit(SPACE_BG, (0, 0))
    pygame.draw.rect(WIN, BORDER_COLOR, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, TEXT_COLOR)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, TEXT_COLOR)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED_BULLET_COLOR, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW_BULLET_COLOR, bullet)

    for rocket in red_rocket:
        pygame.draw.rect(WIN, RED_BULLET_COLOR, rocket)

    for rocket in yellow_rocket:
        pygame.draw.rect(WIN, YELLOW_BULLET_COLOR, rocket)

    pygame.display.update()


def Yellow_movement(keys_pressed, yellow):

    if keys_pressed[pygame.K_a] and yellow.x + MOVEMENT_SPEED > 15:  # Backwards Key
        yellow.x -= MOVEMENT_SPEED

    if keys_pressed[pygame.K_d] and yellow.x - MOVEMENT_SPEED + yellow.width < BORDER.x - 15:  # Forwards Key
        yellow.x += MOVEMENT_SPEED

    if keys_pressed[pygame.K_w] and yellow.y - MOVEMENT_SPEED > -15:  # Up Key
        yellow.y -= MOVEMENT_SPEED

    if keys_pressed[pygame.K_s] and yellow.y + MOVEMENT_SPEED + yellow.height < HEIGHT:  # Down Key
        yellow.y += MOVEMENT_SPEED


def Red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x + MOVEMENT_SPEED > BORDER.x + BORDER.width + 15:  # BackWards Key
        red.x -= MOVEMENT_SPEED

    if keys_pressed[pygame.K_RIGHT] and red.x - MOVEMENT_SPEED + red.width < WIDTH - 5:  # Forwards Key
        red.x += MOVEMENT_SPEED

    if keys_pressed[pygame.K_UP] and red.y - MOVEMENT_SPEED > 0:  # Up Key
        red.y -= MOVEMENT_SPEED

    if keys_pressed[pygame.K_DOWN] and red.y + MOVEMENT_SPEED + red.height < HEIGHT:  # Down Key
        red.y += MOVEMENT_SPEED


def Move_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT_BULLET))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT_BULLET))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def Move_rockets(yellow_rockets, red_rockets, yellow, red):
    for rockets in yellow_rockets:
        rockets.x += ROCKET_SPEED
        if red.colliderect(rockets):
            pygame.event.post(pygame.event.Event(RED_HIT_ROCKET))
            yellow_rockets.remove(rockets)
        elif rockets.x > WIDTH:
            yellow_rockets.remove(rockets)

    for rockets in red_rockets:
        rockets.x -= ROCKET_SPEED
        if yellow.colliderect(rockets):
            pygame.event.post(pygame.event.Event(YELLOW_HIT_ROCKET))
            red_rockets.remove(rockets)
        elif rockets.x < 0:
            red_rockets.remove(rockets)


def Winner(text):
    winner_text = WINNER_FONT.render(text, 1, TEXT_COLOR)
    WIN.blit(winner_text, (WIDTH//2 - winner_text.get_width() //
                           2, HEIGHT//2 - winner_text.get_height()//2))

    pygame.display.update()

    pygame.time.delay(5000)


def main():  # Main Function
    pygame.mixer.music.play()

    red = pygame.Rect(WIDTH - 300, HEIGHT//2, SHIP_WIDTH, SHIP_HEIGHT)
    yellow = pygame.Rect(100, HEIGHT//2, SHIP_WIDTH, SHIP_HEIGHT)

    yellow_rockets = []
    red_rockets = []

    yellow_bullets = []
    red_bullets = []

    red_health = 50
    yellow_health = 50

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # Shoot bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y+yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                    BULLET_SHOOT_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_SHOOT_SOUND.play()

            # Shoot Rockets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and len(yellow_rockets) < MAX_ROCKETS:
                    rockets = pygame.Rect(
                        yellow.x + yellow.width, yellow.y+yellow.height//2 - 2, 20, 15)
                    yellow_rockets.append(rockets)
                    ROCKET_SHOOT_SOUND.play()

                if event.key == pygame.K_RALT and len(red_rockets) < MAX_ROCKETS:
                    rockets = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 20, 15)
                    red_rockets.append(rockets)
                    ROCKET_SHOOT_SOUND.play()

            if event.type == RED_HIT_BULLET:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT_BULLET:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == RED_HIT_ROCKET:
                red_health -= 4
                ROCKET_HIT_SOUND.play()

            if event.type == YELLOW_HIT_ROCKET:
                yellow_health -= 4
                ROCKET_HIT_SOUND.play()

        winner_text = ""

        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            Winner(winner_text)
            menu.Main()
            break

        Move_bullets(yellow_bullets, red_bullets, yellow, red)
        Move_rockets(yellow_rockets, red_rockets, yellow, red)

        keys_pressed = pygame.key.get_pressed()
        # Movements for YellowShip
        Yellow_movement(keys_pressed, yellow)
        Red_movement(keys_pressed, red)

        # Drawing n screen
        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health, red_rockets, yellow_rockets)

    main()


if __name__ == "__main__":
    main()
