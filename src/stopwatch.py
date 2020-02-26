import config
import threading
import win32gui
import time


class Stopwatch():
	def __init__(self):
		self.thread_timer = threading.Thread(target=self.update_timer)
		self.is_stopped = False
		self.is_false_window = False
		self.start_time = time.time()
		self.thread_timer.start()
		print("Start the stopwatch")

	def wrong_window(self):
		self.is_false_window = True
		start_time = time.time()
		while not self.is_stopped:
			if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == config.dino_title:
				self.start_time = self.start_time + (time.time() - start_time)
				self.is_false_window = False
				return 
			time.sleep(0.0001)

	def get_time(self):
		return int(time.time() - self.start_time)

	def update_timer(self):
		while not self.is_stopped:
			time.sleep(0.0001)
			if self.is_false_window:
				continue
			if win32gui.GetWindowText(win32gui.GetForegroundWindow()) != config.dino_title:
				self.wrong_window()
