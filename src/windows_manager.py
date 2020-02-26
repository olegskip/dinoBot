import config
import win32gui


class SimpleWindow:
	def __init__(self, title, pos, size):
		self.title = title
		self.pos = pos
		self.size = size

class WindowsManager:
	def __init__(self):
		self.windows = []
		win32gui.EnumWindows(self.callback, None)

	def callback(self, hwnd, extra):
		rect = win32gui.GetWindowRect(hwnd)
		x = rect[0]
		y = rect[1]
		w = rect[2] - x
		h = rect[3] - y
		title = win32gui.GetWindowText(hwnd)
		if title.strip() and w != 0 and h != 0:
			self.windows.append(SimpleWindow(title, (w, h), (x, y)))

	def is_window(self, title):
		result = False
		for window in self.windows:
			if window.title == title:
				result = True
		return result