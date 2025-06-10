import arcade
import random
import time


# константы
#
SCREEN_TITLE = "Minesweeper"  # название окна
ROW_COUNT = 7  # количество строк на игровом поле
COLUMN_COUNT = 7  # количество столбцов на игровом поле
CELL_WIDTH = 100  # ширина одной ячейки
CELL_HEIGHT = 100  # высота одной ячейки
MARGIN = 2  # толщина границы (то есть линий между ячейками)
# ширина и высота окна
SCREEN_WIDTH = (CELL_WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (CELL_HEIGHT + MARGIN) * ROW_COUNT + MARGIN
MINES_COUNT = 5  # количество мин на игровом поле
ATTEMPTS = 10  # число попыток
MINE_IMAGE = 'games/Arcade/saper/attack.png'
TROPHY_IMAGE = 'games/Arcade/saper/trophy.jpg'


class Minesweeper(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.grid = []
        self.trophy = [random.randint(0, ROW_COUNT-1), random.randint(0, COLUMN_COUNT-1)]
        self.mines_coordinates = []
        self.mines_exploded = arcade.SpriteList()
        self.trophy_sprite = arcade.Sprite(TROPHY_IMAGE, 0.12)
        self.lives = 3
        self.defeat = False
        self.win = False

    def setup_grid(self):
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    def setup(self):
        mines = MINES_COUNT
        while mines > 0:
            row = random.randint(0, ROW_COUNT-1)
            column = random.randint(0, COLUMN_COUNT-1)
            if [row, column] not in self.mines_coordinates and [row, column] not in self.trophy:
                self.mines_coordinates.append([row, column])
                mines -= 1

    def on_draw(self):
        """Отрисовка объектов"""
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                color = self.get_cell_color(row, column)
                x = (CELL_WIDTH//2 + MARGIN) + (CELL_WIDTH + MARGIN) * column
                y = (CELL_HEIGHT//2 + MARGIN) + (CELL_HEIGHT + MARGIN) * row
                arcade.draw_rectangle_filled(x, y, CELL_WIDTH, CELL_HEIGHT, color)
        arcade.draw_text(f'Подорваные мины: {MINES_COUNT - len(self.mines_coordinates)}', 10, 10, arcade.color.BLACK)
        self.mines_exploded.draw()
        arcade.draw_text(f'Жизни: {self.lives}', 640, 10, arcade.color.BLACK)
        if self.lives == 0:
            self.defeat = True
            arcade.draw_text('Ты проиграл', SCREEN_WIDTH/3, SCREEN_HEIGHT/2, arcade.color.RED, 50)
        if self.win:
            self.trophy_sprite.draw()
            arcade.draw_text('Ты выиграл', SCREEN_WIDTH/3, SCREEN_HEIGHT/2, arcade.color.YELLOW, 50)

    def get_cell_color(self, row, column):
        if self.grid[row][column] == 0:
            color = arcade.color.LIGHT_BLUE
        if self.grid[row][column] == 1:
            color = arcade.color.RED
        if self.grid[row][column] == 2:
            color = arcade.color.BLUE
        if self.grid[row][column] == 3:
            color = arcade.color.GRAY_BLUE
        if self.grid[row][column] == 4:
            color = arcade.color.YELLOW
        return color

    def on_update(self, delta_time):
        if self.defeat or self.win:
            time.sleep(4)
            exit()

    def on_mouse_press(self, x, y, button, modifiers):
        column = x//(CELL_WIDTH + MARGIN)
        row = y//(CELL_HEIGHT + MARGIN)
        if [row, column] in self.mines_coordinates:
            self.grid[row][column] = 1
            mine_exploded = arcade.Sprite(MINE_IMAGE, 0.2)
            mine_exploded.center_x = (CELL_WIDTH//2 + MARGIN) + (CELL_WIDTH + MARGIN) * column
            mine_exploded.center_y = (CELL_HEIGHT//2 + MARGIN) + (CELL_HEIGHT + MARGIN) * row
            self.mines_exploded.append(mine_exploded)
            self.mines_coordinates.remove([row, column])
            self.lives -= 1
        if self.grid[row][column] == 3:
            self.grid[row][column] = 2
        if [row, column] == self.trophy:
            self.grid[row][column] = 4
            self.trophy_sprite.center_x = (CELL_WIDTH//2 + MARGIN) + (CELL_WIDTH + MARGIN) * column
            self.trophy_sprite.center_y = (CELL_HEIGHT//2 + MARGIN) + (CELL_HEIGHT + MARGIN) * row
            self.win = True

    def check_mouse_position(self, mouse_row, mouse_column, row, column):
        if row != mouse_row or column != mouse_column:
            if self.grid[row][column] == 3:
                return True

    def on_mouse_motion(self, x, y, dx, dy):
        mouse_column = x//(CELL_WIDTH + MARGIN)
        mouse_row = y//(CELL_HEIGHT + MARGIN)
        if mouse_column < COLUMN_COUNT and mouse_row < ROW_COUNT:
            if self.grid[mouse_row][mouse_column] == 0:
                self.grid[mouse_row][mouse_column] = 3
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    if self.check_mouse_position(mouse_row, mouse_column, row, column):
                        self.grid[row][column] = 0


game = Minesweeper(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup_grid()
game.setup()
arcade.run()
