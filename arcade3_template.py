import arcade

# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Пинг-понг"


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0


class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('games/arcade/ping-pong/ball.png', 0.5)
        self.bar = Bar('games/arcade/ping-pong/bar.png', 0.5)
        self.score = 0
        self.lives = 3
        self.game = False

    def setup(self):
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.ball.change_x = 5
        self.ball.change_y = 7
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 7
        self.bar.change_x = 0

    # отрисовка объектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        self.ball.draw()
        self.bar.draw()
        text_score = f'Счёт: {self.score}'
        arcade.draw_text(text_score, 10, 570, arcade.color.BLACK, 20)
        text_lives = f'Жизни: {self.lives}'
        arcade.draw_text(text_lives, 490, 570, arcade.color.BLACK, 20)
        text_game_over = 'Ты проиграл'
        if self.game:
            arcade.draw_text(text_game_over, 200, 300, arcade.color.BLACK, 30)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 4
        if key == arcade.key.LEFT:
            self.bar.change_x = -4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

    # логика
    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.bottom = self.bar.top
            self.ball.change_y = -self.ball.change_y
            self.score += 1
            print(self.score)
        if self.ball.bottom < 0:
            self.lives -= 1
            self.ball.center_y = 550
        if self.lives == 0:
            self.ball.stop()
            self.bar.stop()
            self.game = True


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
