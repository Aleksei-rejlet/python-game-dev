
import arcade as a
class Our_picture(a.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    def on_draw(self):
        a.start_render()
        a.set_background_color(a.color.LIGHT_BLUE)
        a.draw_circle_filled(300,300,200,a.color.YELLOW)
        a.draw_circle_filled(380,350,20,a.color.BLACK)
        a.draw_circle_filled(220,350,20,a.color.BLACK)
        center_x = 300
        center_y = 230
        width = 150
        hight = 80
        start_angle = 180
        end_angle = 360
        line_width = 10
        a.draw_arc_outline(center_x,center_y,width,hight,a.color.BLACK,start_angle,end_angle,line_width)

window = Our_picture(600,600,'😃Смайлик😃')
a.run()