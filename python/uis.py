import pygame

class BasicButton:
    def __init__(self, img, pos, txt=False, text="", font=None, color=(75,75,75)):
        self.img = img
        self.img_Rect = self.img.get_rect()
        self.img_Rect.center = pos

        if txt==True:
            self.text = font.render(text,  False, color)
            self.textR = self.text.get_rect()
            self.textR.center = self.img_Rect.center


    def add_text(self):
        return self.text


    def get_image(self):
        return self.img

    def get_rect(self):
        return self.img_Rect
