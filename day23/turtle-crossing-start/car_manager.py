from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        for item in self.cars:
            item.fd(self.car_speed)
            if item.xcor() < -320:
                item.hideturtle()
                self.cars.remove(item)


    def create_car(self):
        for _ in range(random.randint(1, 8)):
            car = Turtle(shape="square")
            car.shapesize(1, 2)
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(random.randint(280, 320), random.randint(-200, 200))
            self.cars.append(car)





