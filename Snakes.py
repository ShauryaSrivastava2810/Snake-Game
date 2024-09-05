from turtle import Turtle, Screen
Starting_Post = [(0, 0), (-20, 0), (-40, 0)]
movement = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class snakes:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in Starting_Post:
            self.add_segments(position)

    def add_segments(self, position):
        new = Turtle("square")
        new.penup()
        new.goto(position)
        new.color('Grey')
        self.segments.append(new)
        return self.segments

    def grow(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=newx, y=newy)
        self.segments[0].forward(movement)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)