import pygame


class Button:
    def __init__(self, x, y, state1, state2, window):
        self.image = state1
        self.hover = state2
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.win = window

    def Draw_btn(self):
        action = False
        image = self.image
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            image = self.hover
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                action = False

        if self.image == self.hover and not self.rect.collidepoint(mouse_pos):
            image = self.image

        self.win.blit(image, (self.rect.x, self.rect.y))

        return action
