from utilities import *
from uis import BasicButton

img = Img()

angelGraphs = img.getallImg("❤️ Angel")
UIsG = img.getallImg("UIs")
UIsG[0] = img.resizeImg(UIsG[0], (600,200))

class menu:
    def __init__(self, gsprite):

        self.button = BasicButton(UIsG[0], 500,250)
        self.button1 = BasicButton(UIsG[0], 500,500)



        self.add_sprites(gsprite)

    def add_sprites(self, g):
        g.add(self.button)
        g.add(self.button1)

class setting:
    def __init__(self):
        self.gsprite = gsprite
