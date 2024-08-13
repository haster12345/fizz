import time
import os
import argparse
from typing import List

FPS = 30
LEFT_BOUND = 0
RIGHT_BOUND = 30
UP_BOUND = 0
DOWN_BOUND = 30
TIME_TO_MOVE = 15


def main(target: tuple):
    while True:
        refresh_counter = 0
        x_coord = 0
        y_coord = 0
        number_of_steps = min(target)
        x_steps = (target[0] - x_coord) // number_of_steps
        y_steps = (target[1] - y_coord) // number_of_steps
        steps = 0

        while steps != number_of_steps:
            refresh_counter += 1
            if refresh_counter % TIME_TO_MOVE == 0:
                if (x_coord + 1) == target[0]:
                    x_coord += 1

                if (y_coord + 1) == target[1]:
                    y_coord += 1

                else:
                    x_coord += x_steps * steps
                    y_coord += y_steps * steps
                    steps += 1
            particle(x_coord, y_coord)
            refresh()

    return


def particle(x, y):
    print('\n' * y, ' ' * x, '.')


def sim_particle():
    refresh_counter = 0
    x_move_counter = 0
    hit_left = True
    hit_right = False
    hit_bottom = False
    hit_top = True
    y_move_counter = 0
    while not hit_right:
        refresh_counter += 1
        if refresh_counter % TIME_TO_MOVE == 0:
            x_move_counter += 1
            y_move_counter += 1
        particle(x_move_counter, y_move_counter)
        refresh()
        if x_move_counter == RIGHT_BOUND:
            hit_right = True
            hit_left = False
            hit_bottom = True
            hit_top = False

    while not hit_left:
        refresh_counter += 1
        if refresh_counter % TIME_TO_MOVE == 0:
            x_move_counter -= 1
            y_move_counter -= 1
        particle(x_move_counter, y_move_counter)
        refresh()
        if x_move_counter == 0:
            hit_right = False
            hit_left = True
            hit_top = True
            hit_bot = False
    return


def refresh():
    """
    there is 1000 miliseconds in a second
    and we want 30 fps so that means we want 1 frame every 33 milliseconds
    """
    time.sleep(FPS/1000)
    os.system('clear')
    return


def move(left_move_counter):
    print(' ' * left_move_counter,  '.' )
    return


def move_y(y_move_counter):
    print('\n'* y_move_counter, '.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Fizz',
        description='Animation engine in Python'
    )
    parser.add_argument('-m', '--move', default=(0,0))
    args = parser.parse_args()
    x = int(args.move.split(',')[0])
    y = int(args.move.split(',')[1])
    print(x,y)
    main(target=(x,y))
