import os
import pygame

pygame.init()

# Don't mind this it will just help to load images in our game
# If you want me to explain it well tell me xd
class Img:
	def __init__(self):

		self.game_dir = os.path.dirname(__file__)
		self.img_dir = os.path.join(self.game_dir, "Assests")

	def getImg(self, directory):
		return pygame.image.load(os.path.join(self.img_dir, directory))

	def readfolder(self, folder_dir):
		return os.listdir(os.path.join(self.img_dir, folder_dir))

	def resizeImg(self, img, size):
		self.img = pygame.transform.scale(img, size)
		return self.img

	def getallImg(self, path):
		self.assests_dir = self.readfolder(path)
		self.assests = {}
		for i in range(0,len(self.assests_dir)):
			self.assests_dir[i] = path +"/" +self.assests_dir[i]
			self.assests[i] = self.getImg(self.assests_dir[i])
			#print(self.button_assests_dir[i])
		return self.assests

class Font:
	def __init__(self):
		pass

	def draw(self, font, text, color, pos, surf):
		self.text = self.font.render(text, False, color)
		self.rect = self.text.get_rect()
		self.rect.center = pos
		surf.blit(self.text, self.rect)

	def load_font(self, path, size):
		self.font = pygame.font.Font(path, size)
		return self.font
