import arcade
from constants import *
from dino import *

class Game(arcade.Window):
    def __init__(self, width, height, title) :
        super().__init__(width, height, title) 
        #фон для игры
        self.background = arcade.load_texture(BASE_PATH + "//images//bg.png")
        self.dino = Dino(300, 200, 5)

    def on_draw(self):
        self.clear()
        #отрисовываем фон
        arcade.draw_texture_rectangle(
            SCREEN_HEIGHT/2,
            SCREEN_WIDTH/2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background
        )
        self.dino.draw()
    
    def update(self, delta_time):
        self.dino.update()
        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.dino.change_y = Dino.JUMPING_SPEED
        















window = Game(600, 600, 'Dinosour') 
arcade.run()