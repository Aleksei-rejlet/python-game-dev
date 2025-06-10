import arcade
import random as r

# устанавливаем константы
SW = 800
SH = 600
SCREEN_TITLE = "Шаблон"


class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SW - 50:
            self.right = SW - 50
        if self.left < 50:
            self.left = 50


class Wall(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        if self.bottom < 0:
            self.center_y = SH - 30
            self.center_x = r.randint(30, SW-30)
            window.score += 1


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('games/arcade/race/background.png')
        self.car = Car('games/arcade/race/Audi.png', 0.8)
        self.wall = Wall('games/arcade/race/wall.png', 0.8)
        self.game = False
        self.score = 0

    # начальные значения
    def setup(self):
        wall_size = r.randint(30, SW - 30)
        self.car.center_x = SW / 2
        self.car.center_y = SH / 6
        self.car.change_x = 0
        self.wall.center_x = wall_size
        self.wall.center_y = SH - 30
        self.wall.change_y = -7

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SW / 2, SH / 2, SW, SH, self.bg)
        self.car.draw()
        self.wall.draw()
        text_end_game = 'Ты проиграл'
        if self.game:
            arcade.draw_text(text_end_game, SW/2, 300, arcade.color.AMAZON, 30)
        score_text = f'Счёт: {self.score}'
        arcade.draw_text(score_text, 50, 560, arcade.color.RED, 25)
        text_win = 'Ты выйграл'
        if self.score >= 15:
            arcade.draw_text(text_win, 300, 300, arcade.color.BLACK, 30)

    # игровая логика
    def update(self, delta_time):
        self.car.update()
        self.wall.update()
        if arcade.check_for_collision(self.wall, self.car):
            self.game = True
            self.car.stop()
            self.wall.stop()
        if self.score >= 15:
            self.car.stop()
            self.wall.stop()

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.car.change_x = 5
            self.car.angle = -20
        if key == arcade.key.LEFT:
            self.car.change_x = -5
            self.car.angle = 20

    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.car.change_x = 0
            self.car.angle = 0


window = MyGame(SW, SH, SCREEN_TITLE)
window.setup()
arcade.run()
