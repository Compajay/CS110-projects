import turtle
# some modifications i did to this code what modify the clouds 
#i also refactored and organized my code 
class SceneDrawer:
    def __init__(self, turtle_instance):
        self.t = turtle_instance
        self.t.speed(0)
        self.t.hideturtle()
        self.t.screen.bgcolor("skyblue")

    def jump_to(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def draw_rectangle(self, width, height, color):
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(width)
            self.t.left(90)
            self.t.forward(height)
            self.t.left(90)
        self.t.end_fill()

    def draw_triangle(self, length, color):
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(3):
            self.t.forward(length)
            self.t.left(120)
        self.t.end_fill()

    def draw_circle(self, radius, color):
        self.t.fillcolor(color)
        self.t.begin_fill()
        self.t.circle(radius)
        self.t.end_fill()

    def draw_cloud(self, x, y, scale=1.0):
         positions = [(-20, 0), (0, 10), (20, 0), (-10, -10), (10, -10)]
         for dx, dy in positions:
             self.jump_to(x + dx * scale, y + dy * scale)
             self.draw_circle(20 * scale, "white")

    def draw_sun(self):
        self.jump_to(200, 150)
        self.t.setheading(0)
        self.draw_circle(40, "yellow")

# had trouble with house but solved it out 
    def draw_house(self):
        self.jump_to(-75, -100)
        self.t.setheading(0)
        self.draw_rectangle(150, 100, "red")

  
        self.jump_to(-75, 0)
        self.t.setheading(0)
        self.draw_triangle(150, "brown")

  
        self.jump_to(-25, -100)
        self.t.setheading(0)
        self.draw_rectangle(50, 60, "yellow")
    
   
        self.jump_to(-65, -40)
        self.t.setheading(0)
        self.draw_rectangle(30, 30, "lightblue")

        self.jump_to(35, -40)
        self.t.setheading(0)
        self.draw_rectangle(30, 30, "lightblue")

    def draw_scene(self):
        self.draw_sun()
        self.draw_cloud(-200, 160)
        self.draw_cloud(-160, 180)
        self.draw_house()


def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    scene = SceneDrawer(t)
    scene.draw_scene()
    screen.exitonclick()

if __name__ == "__main__":
    main()

