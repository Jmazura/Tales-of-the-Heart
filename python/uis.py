import pygame

class BasicButton(pygame.sprite.Sprite):
    def __init__(self, img, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
    #    self.image = pygame.Surface((200,200))
    #    self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)

    def draw(self):
        pass

    def update(self):
        pass


class Button(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
