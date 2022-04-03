from settings import *

class Cath(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200,200))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (15,15)

    def draw(self):
        pass

    def udpate(self):
        pass
