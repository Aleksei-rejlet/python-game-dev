import arcade
import random

# устанавливаем константы
SW = 800
SH = 600
ST = "Star Wars"


class Star_ship(arcade.Sprite):
    def update(self):
        if self.right >= SW:
            self.right = SW
        if self.left <= 0:
            self.left = 0


class Enemy(arcade.AnimatedTimeSprite):
    def __init__(self):
        super().__init__()
        self.textures.append(arcade.load_texture('games/Arcade/star wars/tie fighter.png'))
        self.textures.append(arcade.load_texture('games/Arcade/star wars/tie fighter2.png'))
        self.change_y = 2

    def update(self):
        self.center_y -= self.change_y
        if self.center_y < 0:
            window.lives -= 1
            self.kill()
            window.score -= 5


class Bullet(arcade.Sprite):
    def __init__(self):
        super().__init__('games/Arcade/star wars/laser.png', 0.8)
        self.change_y = 5
        self.laser_sound = arcade.load_sound('games/Arcade/star wars/laser.wav')

    def update(self):
        self.center_y += self.change_y
        if self.center_y >= SH:
            self.kill()


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('games/Arcade/star wars/space_background.png')
        self.star_ship = Star_ship('games/Arcade/star wars/x-wing.png', 0.5)
        self.music = arcade.load_sound('games/Arcade/star wars/star_wars.wav')
        arcade.play_sound(self.music)
        self.bullets = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.score = 0
        self.lives = 3
        self.game = True
        self.label = ''

    # начальные значения
    def setup(self):
        self.star_ship.center_x = SW/2
        self.star_ship.center_y = SH/7
        for i in range(50):
            enemy = Enemy()
            enemy.center_x = random.randint(20, SW-20)
            enemy.center_y = 50 * i + SH
            self.enemies.append(enemy)

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SW/2, SH/2, SW, SH, self.bg)
        self.star_ship.draw()
        self.bullets.draw()
        self.enemies.draw()
        arcade.draw_text(f'Счет: {self.score}', 20, SH-30, arcade.color.WHITE, 20)
        arcade.draw_text(f'Жизни: {self.lives}', SW-120, SH-30, arcade.color.WHITE, 20)
        arcade.draw_text(self.label, 300, SH/2, arcade.color.WHITE, 44)

    # игровая логика
    def update(self, delta_time):
        self.bullets.update()
        self.star_ship.update()
        self.enemies.update_animation()
        self.enemies.update()
        for bullet in self.bullets:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemies)
            if hit_list:
                bullet.kill()
                for enemy in hit_list:
                    enemy.kill()
                    self.score += 10
        hit_list_1 = arcade.check_for_collision_with_list(self.star_ship, self.enemies)
        if hit_list_1:
            for enemy in hit_list_1:
                enemy.kill()
                self.score -= 10
                self.lives -= 1

        if len(self.enemies) <= 0 and self.lives > 0:
            self.label = 'Победа'
            self.game = False
        if self.lives <= 0:
            self.label = 'Поражение'
            self.game = False
        if not self.game:
            self.star_ship.stop()
            for bullet in self.bullets:
                bullet.kill()
            for enemy in self.enemies:
                enemy.stop()
            # arcade.stop_sound(self.music)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.game:
            self.star_ship.center_x = x
            self.set_mouse_visible(False)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.game:
            bullet = Bullet()
            bullet.center_x = self.star_ship.center_x
            bullet.bottom = self.star_ship.top
            self.bullets.append(bullet)
            arcade.play_sound(bullet.laser_sound)


window = MyGame(SW, SH, ST)
window.setup()
arcade.run()
