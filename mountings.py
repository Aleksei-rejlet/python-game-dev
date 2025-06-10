import arcade as a
class Our_picture(a.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    def mounting(self,x,y):
        a.draw_triangle_filled(x1=x,y1=y+200,x2=x-80,y2=y+50,x3=x+80,y3=y+50,color=a.color.GRAY)
        a.draw_triangle_filled(x1=x,y1=y+200,x2=x-22,y2=y+160,x3=x+22,y3=y+160,color=a.color.BUBBLES)
        a.draw_triangle_outline(x1=x,y1=y+200,x2=x-80,y2=y+50,x3=x+80,y3=y+50,color=a.color.BLACK)
        a.draw_triangle_outline(x1=x,y1=y+200,x2=x-22,y2=y+160,x3=x+22,y3=y+160,color=a.color.BLACK)
    def river(self):
        a.draw_rectangle_filled(300,20,600,100,a.color.BLUEBERRY)
        a.draw_rectangle_filled(300,80,600,30,a.color.SANDSTORM)
    def on_draw(self):
        a.start_render()
        a.set_background_color(a.color.LIGHT_BLUE)
        a.draw_rectangle_filled(300,100,600,200,a.color.BRONZE)
        a.draw_circle_filled(100,350,20,a.color.YELLOW)
        self.mounting(200,120)
        self.mounting(400,120)
        self.mounting(300,120)
        self.river()
        
window = Our_picture(600,400,'Горы')
a.run()