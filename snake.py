from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):

        self.segments = []
        self.make_body()
        self.head = self.segments[0]

    def make_body(self):
        x_coordinate = 0
        for seg in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(x_coordinate)
            x_coordinate -= 20
            self.segments.append(segment)

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            self.segments[num].setposition(self.segments[num - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def body_up(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        last_segment = self.segments[-1].position()
        segment.setposition(last_segment)
        self.segments.append(segment)






