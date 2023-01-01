import time
from turtle import Screen
from player import Player
from car_manager import CarManager, create_cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
game_cars = []
scoreboard = Scoreboard()

# creating 10 initial random cars
inital_cars = create_cars(10)
game_cars += inital_cars

screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create 5 random cars 
    if len(game_cars) < 25:
        new_cars = create_cars(5)
        game_cars += new_cars

    # move every car to the left    
    for car in game_cars:
        car.move()

    # remove car from list when car is out of bounds
    for car in game_cars:
        if car.xcor() < -320:
            car.hideturtle()
            game_cars.remove(car)

    # reset game when player collides with car 
    '''for car in game_cars:
        if player.distance(car) < 25:
            player.reset_position()
            player.reset_speed()
            scoreboard.reset_level()
            for each_car in game_cars:
                each_car.reset_speed()'''

    # end game when player collides with car
    for car in game_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False
    
    # detect reaching finish line
    if player.reached_finish_line():
        player.reset_position()
        player.increase_speed()
        for car in game_cars:
            car.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()