import arcade as a
class Our_picture(a.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    def bird(self,x,y):
        a.draw_arc_outline(x,y,20,20,a.color.BLACK,0,90)
        a.draw_arc_outline(x+20,y,20,20,a.color.BLACK,90,180)
    def tree(self,x,y):
        a.draw_rectangle_filled(x,y,20,80,a.color.DARK_BROWN)
        a.draw_circle_filled(x,y+40,40,a.color.DARK_GREEN)
    def house(self,x,y):
        a.draw_rectangle_filled(x,y,120,100,a.color.CORN)
        a.draw_rectangle_filled(x,y,40,40,a.color.LIGHT_BLUE)
        a.draw_triangle_filled(x1=x,y1=y+100,x2=x-60,y2=y+50,x3=x+60,y3=y+50,color=a.color.RED_BROWN)
    def on_draw(self):
        a.start_render()
        a.set_background_color(a.color.LIGHT_BLUE)
        a.draw_rectangle_filled(300,100,600,200,a.color.OFFICE_GREEN)
        a.draw_circle_filled(100,350,20,a.color.YELLOW)
        self.bird(350,320)
        self.bird(400,300)
        self.bird(450,320)
        self.tree(120,160)
        self.tree(520,160)
        self.house(350,150)


    

window = Our_picture(600,400,'Пейзаж')
a.run()