import config
import win32gui
import time
from controller import Controller
from stopwatch import Stopwatch
from threading import Thread
from datetime import datetime
from image import Image


class Bot:
	def __init__(self):
		print("Starting...")
		self.controller = Controller()
		self.image = Image()
		self.stopwatch = Stopwatch()

	def update(self):
		while True:
			if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == config.dino_title:
				self.image.get_screenshot()
				self.event_handler()

	def event_handler(self):
		max_x = 400
		if self.stopwatch.get_time() > 20:
			max_x = 500
		elif self.stopwatch.get_time() > 60:
			max_x = 1110
		elif self.stopwatch.get_time() > 80:
			max_x = 1200
		elif self.stopwatch.get_time() > 100:
			max_x = 1300
		elif self.stopwatch.get_time() > 120:
			max_x = 1500
		for x in range(120, max_x, 2): 
			for y in range(config.bird_y, config.cactus_y, 5):
				if self.image.get_pixel(x, y).color == config.enemy_color: # check for an enemy
					if self.controller.jump():
						print("[" + datetime.now().strftime("%H:%M:%S") + "; " + str(self.stopwatch.get_time())  + "] Jumping...")
					return True
		return False
