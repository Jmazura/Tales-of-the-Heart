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
    #    surf.blit(bg, (0,0))
        for i in self.buttons:
            i.draw(surf)

    def update(self):
        self.running = True
        self.gameInstance = "MENU"
        rect = self.buttons[3].get_rect()
        mouse = pygame.mouse.get_pos()

        if rect[0] < mouse[0] and rect[0]+rect[2] > mouse[0]:
            if rect[1] < mouse[1] and rect[1]+rect[3] > mouse[1]:
                pressed = pygame.mouse.get_pressed()
                if pressed == (1,0,0):
                    self.running = False

        rect1 = self.buttons[2].get_rect()
        if rect1[0] < mouse[0] and rect1[0]+rect1[2] > mouse[0]:
            if rect1[1] < mouse[1] and rect1[1]+rect1[3] > mouse[1]:
                pressed = pygame.mouse.get_pressed()
                if pressed == (1,0,0):
                    self.gameInstance = "Credits"



class Credits:
    def __init__(self):
        self.b = BasicButton(UIsG[2], GRID[11][2], True, "BACK", font1)

    def draw(self, surf):
        self.b.draw(surf)

    def update(self):
        self.gameInstance = "Credits"
        mouse = pygame.mouse.get_pos()
        rect = self.b.get_rect()
        if rect[0] < mouse[0] and rect[0]+rect[2] > mouse[0]:
            if rect[1] < mouse[1] and rect[1]+rect[3] > mouse[1]:
                pressed = pygame.mouse.get_pressed()
                if pressed == (1,0,0):
                    print("WOKRIGN")
                    self.gameInstance = "MENU"
