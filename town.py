import arcade as a
import random
class Our_picture(a.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    def house(self,x,y):
        a.draw_rectangle_filled(x,y,200,250,a.color.RAJAH)
        a.draw_rectangle_filled(x,y-75,60,100,a.color.BLACK_OLIVE)
        a.draw_rectangle_filled(x-40,y+15,40,60,a.color.ALMOND)
        a.draw_rectangle_filled(x+40,y+15,40,60,a.color.ALMOND)
        a.draw_rectangle_filled(x-40,y+80,40,60,a.color.ALMOND)
        a.draw_rectangle_filled(x+40,y+80,40,60,a.color.ALMOND)
    def road(self,x,y):
        timer = 7
        while timer > 0:
            a.draw_rectangle_filled(x+20,y,80,20,a.color.WHITE)
            timer -= 1
            x += 100

    def on_draw(self):
        a.start_render()
        a.set_background_color(a.color.DARK_PASTEL_PURPLE)
        a.draw_rectangle_filled(300,100,600,200,a.color.EBONY)
        self.house(500,250)
        self.road(0,70)
        


window = Our_picture(600,400,'Город')
a.run()