import arcade
import time
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Plants VS Zombies'


def lawn_x(x):
    if 250 < x < 326:
        column = 1
        center_x = 288
    elif 326 < x < 400:
        column = 2
        center_x = 363
    elif 400 < x < 485:
        column = 3
        center_x = 443
    elif 485 < x < 560:
        column = 4
        center_x = 522
    elif 560 < x < 640:
        column = 5
        center_x = 600
    elif 640 < x < 715:
        column = 6
        center_x = 678
    elif 715 < x < 785:
        column = 7
        center_x = 750
    elif 785 < x < 870:
        column = 8
        center_x = 827
    elif 870 < x < 960:
        column = 9
        center_x = 915
    return center_x, column


def lawn_y(y):
    if 29 < y < 130:
        line = 1
        center_y = 80
    elif 130 < y < 220:
        line = 2
        center_y = 175
    elif 220 < y < 323:
        line = 3
        center_y = 271
    elif 323 < y < 424:
        line = 4
        center_y = 370
    elif 424 < y < 527:
        line = 5
        center_y = 472
    return center_y, line


class Plant(arcade.AnimatedTimeSprite):
    def __init__(self, hp, cost):
        super().__init__(0.12)
        self.hp = hp
        self.cost = cost
        self.line = 0
        self.column = 0

    def update(self):
        if self.hp <= 0:
            self.kill()
            window.lawns.remove((self.line, self.column))

    def planting(self, center_x, center_y, line, column):
        self.center_x = center_x
        self.center_y = center_y
        self.line = line
        self.column = column


class Sunflower(Plant):
    def __init__(self):
        super().__init__(hp=80, cost=50)
        self.texture = arcade.load_texture('games/Arcade/pvz/sun1.png')
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/sun1.png'))
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/sun2.png'))
        self.time_spawn = time.time()

    def update(self):
        super().update()
        if time.time() - self.time_spawn >= 10:
            sun = Sun(self.center_x + 30, self.center_y + 30)
            window.spawn_suns.append(sun)
            self.time_spawn = time.time()


class Sun(arcade.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__('games/Arcade/pvz/sun.png', 0.15)
        self.center_x = position_x
        self.center_y = position_y

    def update(self):
        self.angle += 1


class Peashooter(Plant):
    def __init__(self):
        super().__init__(hp=100, cost=100,)
        self.texture = arcade.load_texture('games/Arcade/pvz/pea1.png')
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/pea1.png'))
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/pea2.png'))
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/pea3.png'))
        self.pea_spawn = time.time()

    def update(self):
        super().update()
        zombie_on_line = False
        for zombie in window.zombies:
            if self.line == zombie.line:
                zombie_on_line = True
        if time.time() - self.pea_spawn > 1.5 and zombie_on_line:
            pea = Pea(self.center_x + 10, self.center_y + 10)
            window.spawn_peas.append(pea)
            self.pea_spawn = time.time()


class Pea(arcade.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__('games/Arcade/pvz/bul.png', 0.15)
        self.center_x = position_x
        self.center_y = position_y
        self.damage = 1
        self.change_x = 9

    def update(self):
        self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:
            self.kill()
        hits = arcade.check_for_collision_with_list(self, window.zombies)
        if hits:
            for zombie in hits:
                zombie.hp -= self.damage
                arcade.play_sound(window.music_hit)
                self.kill()


class Wallnut(Plant):
    def __init__(self):
        super().__init__(hp=200, cost=50)
        self.texture = arcade.load_texture('games/Arcade/pvz/nut1.png')
        for i in range(20):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/nut1.png'))
        self.textures.append(arcade.load_texture('games/Arcade/pvz/nut2.png'))
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/nut3.png'))
        self.textures.append(arcade.load_texture('games/Arcade/pvz/nut2.png'))


class Torchwood(Plant):
    def __init__(self):
        super().__init__(hp=120, cost=175)
        self.texture = arcade.load_texture('games/Arcade/pvz/tree1.png')
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/tree1.png'))
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/tree2.png'))
        for i in range(3):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/tree3.png'))

    def update(self):
        super().update()
        fire_peas = arcade.check_for_collision_with_list(self, window.spawn_peas)
        for pea in fire_peas:
            pea.texture = arcade.load_texture('games/Arcade/pvz/firebul.png')
            pea.damage = 3


class Zombies(arcade.AnimatedTimeSprite):
    def __init__(self, hp, line):
        super().__init__(0.09)
        self.hp = hp
        self.line = line
        self.center_x = SCREEN_WIDTH
        self.change_x = 0.2

    def update(self):
        eating = False
        food = arcade.check_for_collision_with_list(self, window.plants)
        for plant in food:
            if self.line == plant.line:
                plant.hp -= 0.5
                eating = True
        if eating:
            self.change_x = 0
            self.angle = 15
        else:
            self.change_x = 0.2
            self.angle = 0
        self.center_x -= self.change_x
        if self.hp <= 0:
            self.kill()


class Ordinary_zombie(Zombies):
    def __init__(self, line):
        super().__init__(hp=8, line=line)
        self.texture = arcade.load_texture('games/Arcade/pvz/zom1.png')
        for i in range(4):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/zom1.png'))
        self.textures.append(arcade.load_texture('games/Arcade/pvz/zom2.png'))


class Conehead_zombie(Zombies):
    def __init__(self, line):
        super().__init__(hp=16, line=line)
        self.texture = arcade.load_texture('games/Arcade/pvz/zom1.png')
        for i in range(4):
            self.textures.append(arcade.load_texture('games/Arcade/pvz/cone1.png'))
        self.textures.append(arcade.load_texture('games/Arcade/pvz/cone2.png'))


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = True
        self.back = arcade.load_texture('games/Arcade/pvz/background.jpg')
        self.menu = arcade.load_texture('games/Arcade/pvz/menu_vertical.png')
        self.plants = arcade.SpriteList()
        self.seed = None
        self.lawns = []
        self.sun = 9900
        self.spawn_suns = arcade.SpriteList()
        self.spawn_peas = arcade.SpriteList()
        self.zombies = arcade.SpriteList()
        self.zombie_spawn = time.time()

    # начальные значения
    def setup(self):
        self.music = arcade.load_sound('games/Arcade/pvz/grasswalk.mp3')
        self.music_seed = arcade.load_sound('games/Arcade/pvz/seed.mp3')
        self.music_hit = arcade.load_sound('games/Arcade/pvz/hit.mp3')
        arcade.play_sound(self.music)

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.back)
        arcade.draw_texture_rectangle(60, 300, 130, 600, self.menu)
        self.plants.draw()
        if self.seed is not None:
            self.seed.draw()
        arcade.draw_text(f'{self.sun}', 30, 487, arcade.color.BROWN, 30)
        self.spawn_suns.draw()
        self.spawn_peas.draw()
        self.zombies.draw()

    # игровая логика
    def update(self, delta_time):
        if self.game:
            self.plants.update_animation()
            self.plants.update()
            self.spawn_suns.update()
            self.spawn_peas.update()
            self.zombies.update_animation()
            self.zombies.update()
            if time.time() - self.zombie_spawn > 6:
                center_y, line = lawn_y(random.randint(30, 520))
                zombie_type = random.randint(1, 5)
                if zombie_type == 1:
                    zombie = Conehead_zombie(line)
                else:
                    zombie = Ordinary_zombie(line)
                zombie.center_y = center_y
                self.zombies.append(zombie)
                self.zombie_spawn = time.time()

    # нажатить кнопку мыши
    def on_mouse_press(self, x, y, button, modifiers):
        if self.game:
            if 10 < x < 110 and 370 < y < 480:
                self.seed = Sunflower()
            if 10 < x < 110 and 255 < y < 365:
                self.seed = Peashooter()
            if 10 < x < 110 and 140 < y < 250:
                self.seed = Wallnut()
            if 10 < x < 110 and 25 < y < 135:
                self.seed = Torchwood()
            if self.seed is not None:
                self.seed.center_x = x
                self.seed.center_y = y
                self.seed.alpha = 128
        for sun in self.spawn_suns:
            if sun.left < x < sun.right and sun.bottom < y < sun.top:
                sun.kill()
                self.sun += 25

    # движение мыши
    def on_mouse_motion(self, x, y, dx, dy):
        if self.seed is not None:
            self.seed.center_x = x
            self.seed.center_y = y

    # отпустить кнопку мыши
    def on_mouse_release(self, x, y, button, modifiers):
        if self.seed is not None and 250 < x < 960 and 30 < y < 526:
            center_x, column = lawn_x(x)
            center_y, line = lawn_y(y)
            cost = self.seed.cost
            if (line, column) not in self.lawns and self.sun >= cost:
                self.seed.planting(center_x, center_y, line, column)
                self.seed.alpha = 255
                self.plants.append(self.seed)
                self.seed = None
                self.lawns.append((line, column))
                arcade.play_sound(self.music_seed)
                self.sun -= cost
        elif self.seed is not None and 0 < x < 130:
            self.seed = None
            

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
