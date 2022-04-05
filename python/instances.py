from utilities import *
from uis import BasicButton
import pygame

img = Img()
font = Font()

font1 = font.load_font("Assests/04B_30__.TTF", 40)
font2 = font.load_font("Assests/Pixelated Regular.ttf", 40)

angelGraphs = img.getallImg("❤️ Angel")
UIsG = img.getallImg("UIs")
UIsG[1] = img.resizeImg(UIsG[1], (450,300))
bg = img.getImg("bg.png")
bg = img.resizeImg(bg,(800,600))

class Menu:
    def __init__(self):
        self.button1 = BasicButton(UIsG[1], ((800/3)*2,150-50),True,"Start",font1)
        self.button2 = BasicButton(UIsG[1], ((800/3)*2,300-90),True,"Setting",font1)
        self.button3 = BasicButton(UIsG[1], ((800/3)*2,450-130),True,"Credits",font1)
        self.button4 = BasicButton(UIsG[1], ((800/3)*2,600-170),True,"Exit",font1)

    def draw(self, surf):
        surf.blit(bg, (0,0))

        surf.blit(self.button1.get_image(), self.button1.get_rect())
        surf.blit(self.button1.add_text(),(((800/3)*2)- 85,150-70))
        surf.blit(self.button2.get_image(), self.button2.get_rect())
        surf.blit(self.button2.add_text(),(((800/3)*2)- 85,300-110))
        surf.blit(self.button3.get_image(), self.button3.get_rect())
        surf.blit(self.button3.add_text(),(((800/3)*2)- 85,450-150))
        surf.blit(self.button4.get_image(), self.button4.get_rect())
        surf.blit(self.button4.add_text(),(((800/3)*2)- 85,600-190))
    def update(self):
        pass

class Setting:
    def __init__(self):
        pass
