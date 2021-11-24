"""
File: brickbreaker.py
----------------
Classic brickbreaker game.
"""

import tkinter
import time
import random

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS+1) * SPACING ) / N_COLS

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 20

def main():
    # makes the canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')
    # creates bricks
    create_bricks(canvas)
    # creates ball in centre of canvas
    ball = canvas.create_oval((CANVAS_WIDTH / 2) - 20, (CANVAS_HEIGHT / 2) - 20, (CANVAS_WIDTH / 2) + 20, (CANVAS_HEIGHT / 2) + 20, fill="black")
    # creates paddle in centre of canvas
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, CANVAS_HEIGHT - 20, fill="black", outline="black")
    try:
        change_x = 10
        change_y = 10
        while True:
            # gets mouse location and reacts to it
            mouse_x = canvas.winfo_pointerx() - (PADDLE_WIDTH / 2) - 1
            if mouse_x + PADDLE_WIDTH > CANVAS_WIDTH:
                canvas.moveto(paddle, CANVAS_WIDTH - PADDLE_WIDTH)
            elif mouse_x - PADDLE_WIDTH / 2 < 0:
                canvas.moveto(paddle, 0)
            else:
                canvas.moveto(paddle, mouse_x)

            # moves ball
            canvas.move(ball, change_x, change_y)

            # ensures ball doesn't go beyond left or right walls
            if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
                change_x *= -1

            # ensures ball doesn't go beyond top wall
            if hit_top_wall(canvas, ball):
                change_y *= -1

            # makes ball bounce off an object
            if hit_object(canvas, ball, paddle):
                change_y *= -1

            # if hit_bottom_wall(canvas, ball):
            #     canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, width=300, fill="black", font='Courier New', text='GAME OVER!')

            # redraws canvas
            canvas.update()

            # pause
            time.sleep(1 / 40.)
    except:
        pass


def hit_object(canvas, ball, paddle):
    # To check for collision of ball with paddle
    ball_coords = canvas.coords(ball)
    x_1 = ball_coords[0]
    y_1 = ball_coords[1]
    x_2 = ball_coords[2]
    y_2 = ball_coords[3]
    results = canvas.find_overlapping(x_1, y_1, x_2, y_2)
    for object in results:
        if object == paddle or object == ball:
            return len(results) > 1
        else:
            canvas.delete(object)

def hit_left_wall(canvas, object):
    #detects left wall
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    #detects top wall
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    #detects right wall
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    #detects bottom wall
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT

def create_bricks(canvas):
    #creates 11 x 8 bricks
    for row in range(N_ROWS):
        for col in range(N_COLS + 1):
            draw_rectangle(canvas, row, col)

def draw_rectangle(canvas, row, col):
    # draws one brick
    x = col * BRICK_WIDTH
    y = row * BRICK_HEIGHT
    rect = canvas.create_rectangle(x + SPACING, y + SPACING, x + BRICK_WIDTH, y + BRICK_HEIGHT, fill="red", outline="red")
    return rect

def get_left_x(canvas, object):
    '''
    This friendly method returns the x coordinate of the left of an object.
    Recall that canvas.coords(object) returns a list of the object
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 0 is the left-x
    '''
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    '''
    This friendly method returns the y coordinate of the top of an object.
    Recall that canvas.coords(object) returns a list of the object
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 1 is the top-y
    '''
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    """
    This friendly method returns the x coordinate of the right of an object.
    Recall that canvas.coords(object) returns a list of the object
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 2 is the right-x
    """
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    '''
    This friendly method returns the y coordinate of the top of an object.
    Recall that canvas.coords(object) returns a list of the object
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 3 is the bottom-y
    '''
    return canvas.coords(object)[3]

def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()
