from image import Image
import pyscreenshot
import time
from controller import Controller
import config
from threading import Thread
import win32gui
import time



class Bot:
    def __init__(self):
        print("Starting...")
        self.controller = Controller()
        self.image = Image()
        self.start_time = time.time()

    def update(self):
        while True:
            if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "chrome://dino/ - Google Chrome":
                self.image.get_screenshot()
                self.event_handler()

    def event_handler(self):
        max_x = 350
        #max_x = 300
        if time.time() - self.start_time > 20:
            max_x = 500
        if time.time() - self.start_time > 80:
            max_x = 850
        if time.time() - self.start_time > 200:
            max_x = 1000
        if time.time() - self.start_time > 400:
            max_x = 1200
        if time.time() - self.start_time > 600:
            max_x = 1500
        for x in range(120, max_x, 2):
            for y in range(config.bird_y, config.cactus_y, 5):
                if self.image.get_pixel(x, y).color == config.enemy_color or self.image.get_pixel(x, y).color == config.enemy_color:  # check for an enemy
                    self.controller.jump()
                    return True
        return False
