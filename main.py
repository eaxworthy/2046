from turtle import Turtle, Screen

SCREEN_HEIGHT = 94
SCREEN_WIDTH = 94

screen = Screen()
screen.setup(width = SCREEN_WIDTH, height=SCREEN_HEIGHT)

board = [ [None for i in range(4)] for j in range(4)]

#testing coords for center of board squares
coords = [ [(i,j) for i in range(12, SCREEN_WIDTH, 23)] for j in range(12, SCREEN_HEIGHT,23)]

print(coords)

screen.exitonclick()
