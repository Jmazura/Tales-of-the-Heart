import pygame

class BasicButton:
    def __init__(self, img, pos, txt=False, text="", font=None, color=(75,75,75)):
        self.img = img
        self.img_Rect = self.img.get_rect()
        self.img_Rect.x = pos[0]
        self.img_Rect.y = pos[1]+50
        self.txt = txt;

        if txt==True:
            self.text = font.render(text,  False, color)
            self.textR = self.text.get_rect()
            self.textR.center = self.img_Rect.center

    def draw(self, surf):
        surf.blit(self.img, (self.img_Rect.x,self.img_Rect.y))
        if self.txt == True:
            surf.blit(self.text, (self.textR.center[0]-75,self.textR.center[1]-15))

    def add_text(self):
        return self.text

    def get_image(self):
        return self.img

    def get_rect(self):
        return self.img_Rect
