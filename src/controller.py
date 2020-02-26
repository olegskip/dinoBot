import config
import win32gui
import time
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key


class Controller:
	def __init__(self):
		self.keyboard = KeyboardController()

	def jump(self):
		if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == config.dino_title:
			self.keyboard.press(Key.space)
			return True