from utilities import *
from settings import *
from uis import BasicButton


img = Img()
font = Font()

font1 = font.load_font("Assests/04B_30__.TTF", 30)
font2 = font.load_font("Assests/Pixelated Regular.ttf", 30)

angelGraphs = img.getallImg("❤️ Angel")
UIsG = img.getallImg("UIs")
UIsG[2] = img.resizeImg(UIsG[2], (370,85))
bg = img.getImg("bg.png")
bg = img.resizeImg(bg,(800,600))

class Menu:
    def __init__(self):

        text=["Start","Settings","Credits","Exit"]
        self.buttons = []
        for i in range(4):
            self.buttons.append(BasicButton(UIsG[2],GRID[11][i*4],True,text[i],font1))


    def draw(self, surf):
        surf.blit(bg, (0,0))
        for i in self.buttons:
            i.draw(surf)

    def update(self):
        #print(self.buttons[0].get_rect())
        pass

class Setting:
    def __init__(self):
        pass
