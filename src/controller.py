from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
class Controller:
	def __init__(self):
		self.keyboard = KeyboardController()

	keyboard = None

	def jump(self):
		print("Jumping...")
		self.keyboard.press(Key.space)
		