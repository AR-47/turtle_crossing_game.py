from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 6
FINISH_LINE_Y = 270

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reached_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def increase_speed(self):
        global MOVE_DISTANCE
        if MOVE_DISTANCE <= 12:
            MOVE_DISTANCE += 2
    
    def reset_speed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE = 6