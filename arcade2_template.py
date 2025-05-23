import arcade

# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Анимация"

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_x = 300
        self.center_y = 300
        self.radius = 60
        self.change_x = 5
        self.change_y = 3

    # отрисовка объектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius,arcade.color.PSYCHEDELIC_PURPLE)

    # логика
    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if (self.center_x + self.radius) > SCREEN_WIDTH or (self.center_x - self.radius) < 0:
            self.change_x = -self.change_x
            if self.radius > 10:
                self.radius -= 3
            else:
                self.radius += 2
        if (self.center_y + self.radius) > SCREEN_HEIGHT or (self.center_y - self.radius) < 0:
            self.change_y = -self.change_y
            if self.radius > 10:
                self.radius -= 3
            else:
                self.radius += 2
game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
