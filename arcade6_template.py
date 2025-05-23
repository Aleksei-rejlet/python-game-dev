import arcade
# устанавливаем константы
SW = 1000
SH = 800
ST = "Динозавр"


class Dino(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.5
        if self.center_y <= 250:
            self.center_y = 250
            self.jump = False


class Cactus(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0:
            self.center_x = SW
            window.score += 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('games/arcade/dino/desert.png')
        self.dino = Dino(0.5)
        self.dino.textures = []
        texture_dino1 = 'games/arcade/dino/dino1.png'
        texture_dino2 = 'games/arcade/dino/dino2.png'
        texture_dino3 = 'games/arcade/dino/dino3.png'
        self.dino.textures.append(arcade.load_texture(texture_dino1))
        self.dino.textures.append(arcade.load_texture(texture_dino2))
        self.dino.textures.append(arcade.load_texture(texture_dino3))
        self.cactus = Cactus(0.5)
        self.cactus.textures = []
        texture_cactus1 = 'games/arcade/dino/cactus2.png'
        texture_cactus2 = 'games/arcade/dino/cactus3.png'
        self.cactus.textures.append(arcade.load_texture(texture_cactus1))
        self.cactus.textures.append(arcade.load_texture(texture_cactus1))
        self.cactus.textures.append(arcade.load_texture(texture_cactus1))
        self.cactus.textures.append(arcade.load_texture(texture_cactus2))
        self.cactus.textures.append(arcade.load_texture(texture_cactus2))
        self.cactus.textures.append(arcade.load_texture(texture_cactus2))
        self.score = 0
        self.game_bg = False

    # начальные значения
    def setup(self):
        self.dino.center_x = 100
        self.dino.center_y = 250
        self.cactus.center_x = SW
        self.cactus.center_y = 250
        self.cactus.change_x = 5

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SW/2, SH/2, SW, SH, self.bg)
        self.dino.draw()
        self.cactus.draw()
        arcade.draw_text(f'Счёт: {self.score}', 10, 700, arcade.color.AFRICAN_VIOLET, 40)
        if self.game_bg:
            self.bg = arcade.load_texture('games/arcade/dino/desertGO.png')

    # игровая логика
    def update(self, delta_time):
        self.dino.update_animation()
        self.dino.update()
        self.cactus.update_animation()
        self.cactus.update()
        if arcade.check_for_collision(self.dino, self.cactus):
            self.dino.stop()
            self.cactus.stop()
            window.game_bg = True

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and not self.dino.jump:
            self.dino.change_y = 12
            self.dino.jump = True

    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        pass


window = MyGame(SW, SH, ST)
window.setup()
arcade.run()
