from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 7
MOVE_INCREMENT = 0.5
X_AXIS = list(range(300, 700, 54))
Y_AXIS = list(range(-230, 260, 30))

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.penup()
        self.xcor_start = random.choice(X_AXIS)
        self.ycor_start = random.choice(Y_AXIS)
        self.goto(self.xcor_start, self.ycor_start)

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def increase_speed(self):
        global MOVE_DISTANCE, MOVE_INCREMENT
        if MOVE_DISTANCE <= 12:
            MOVE_DISTANCE += MOVE_INCREMENT

    def reset_speed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE = 8

def create_cars(num):
    cars = []
    for _ in range(num):
        new_car = CarManager()
        cars.append(new_car)
    return cars