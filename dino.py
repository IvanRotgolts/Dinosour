import arcade
from constants import *

class Dino(arcade.Sprite):
    """Класс описывает динозавра из игры"""
    #атрибуты класса
    JUMPING_SPEED = 0
    GRAVITATION = 0.05

    def __init__(self, x, y, jumping_y, filename = BASE_PATH + "//images//dino1.png"):
        super().__init__(filename, 0.5)
        self.center_y = y
        self.center_x = x
        self.change_y = 0
        Dino.JUMPING_SPEED = jumping_y

    def update(self):
        self.center_y += self.change_y
        self.change_y -= Dino.GRAVITATION

    #останавливаем дино на линии
        if self.center_y < 200:
            self.center_y = 200
