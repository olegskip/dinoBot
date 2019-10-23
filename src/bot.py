from image import Image
import pyscreenshot
import time
from controller import Controller
import config
from threading import Thread

class Bot:
    def update(self):
        print("Starting...")
        self.controller = Controller()
        
        self.image = Image()

        while True:
            self.image.get_screenshot()
            if self.check_for_jump():
                self.controller.jump()


    image = None
    controller = None

    def check_for_jump(self):
        for x in range(50, 300, 5):
            if self.image.get_pixel(x, 25).color == config.cactus_color:
                return True
        return False
