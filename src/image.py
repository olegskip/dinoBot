import config
from PIL import ImageGrab 
from pixel import Pixel


class Image:
	def __init__(self):
		self.get_screenshot()

	def get_size(self):
		return self.image.size

	def get_pixel(self, x, y):
		pixels = self.image.load()
		return Pixel((x, y), pixels[x, y])

	def get_screenshot(self):
		self.image = ImageGrab.grab(bbox=(100, 500, 1900, 750))
		if config.is_save_screenshot:
			self.image.save("screenshot.png")


	image = None
