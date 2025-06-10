import arcade
import random

# устанавливаем константы
SW = 650
SH = 480
ST = 'Flappy pinguin'


class Pinguin(arcade.AnimatedTimeSprite):
    def __init__(self):
        super().__init__(1)
        self.textures.append(arcade.load_texture('games/arcade/flappy bird/penguin1.png'))
        self.textures.append(arcade.load_texture('games/arcade/flappy bird/penguin2.png'))
        self.textures.append(arcade.load_texture('games/arcade/flappy bird/penguin3.png'))

    def update(self):
        self.center_y += self.change_y
        self.angle += self.change_angle
        self.change_y -= 0.4
        self.change_angle -= 0.4
        if self.center_y >= SH:
            self.center_y = SH
        if self.center_y <= 0:
            self.center_y = 0
        if self.angle >= 40:
            self.angle = 40
        if self.angle <= -30:
            self.angle = -30


class ColumnTop(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0:
            self.center_x = SW
            self.center_y = random.randint(380, 480)
            window.score += 1


class ColumnBottom(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0:
            self.center_x = SW
            self.center_y = random.randint(0, 70)


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        bg1 = 'games/arcade/flappy bird/space.png'
        self.bg = arcade.load_texture(bg1)
        self.pinguin = Pinguin()
        self.columns = arcade.SpriteList()
        self.game_over = False
        self.score = 0

    # начальные значения
    def setup(self):
        self.pinguin.center_x = 100
        self.pinguin.center_y = 180
        self.pinguin.change_y = 0
        self.pinguin.change_angle = 0
        for i in range(5):
            column_top = ColumnTop('games/arcade/flappy bird/column_top.png', 1)
            column_top.center_x = 130 * i + SW
            column_top.center_y = 400
            column_top.change_x = 5
            self.columns.append(column_top)

            column_bot = ColumnBottom('games/arcade/flappy bird/column_bottom.png', 1)
            column_bot.center_x = 130 * i + SW
            column_bot.center_y = 80
            column_bot.change_x = 5
            self.columns.append(column_bot)

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SW/2, SH/2, SW, SH, self.bg)
        self.pinguin.draw()
        self.columns.draw()
        arcade.draw_text(f'Счёт: {self.score}', 30, 30, arcade.color.AERO_BLUE, 30)
        if self.game_over:
            self.bg = arcade.load_texture('games/arcade/flappy bird/game_over_PNG56.png')

    # игровая логика
    def update(self, delta_time):
        self.pinguin.update_animation()
        self.pinguin.update()
        self.columns.update()
        hit_list = arcade.check_for_collision_with_list(self.pinguin, self.columns)
        if hit_list:
            self.pinguin.stop()
            self.game_over = True
            for column in self.columns:
                column.stop()

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.pinguin.change_y = 7
            self.pinguin.change_angle = 5


window = MyGame(SW, SH, ST)
window.setup()
arcade.run()
