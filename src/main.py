import config
import sys
import win32gui
from windows_manager import WindowsManager
from bot import Bot


def main():
	windows_manager = WindowsManager()

	if not windows_manager.is_window(config.dino_title):
		print("Can not find the window of dino. Try to switch the tab to dino and restart.")
		sys.exit(-1)

	bot = Bot()
	try:
		bot.update()
	except KeyboardInterrupt:
		print("Stop!")
		bot.stopwatch.is_stopped = True
		sys.exit(-1)


if __name__ == '__main__':
	main()
