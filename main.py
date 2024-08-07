import time
import os

FPS = 30
LEFT_BOUND = 0
RIGHT_BOUND = 30
UP_BOUND = 0
DOWN_BOUND = 30
TIME_TO_MOVE = 10


def main():
    refresh_counter = 0
    x_move_counter = 0
    hit_left = True
    hit_right = False
    hit_bottom = False
    hit_top = True
    y_move_counter = 0

    while True:
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


def particle(x, y):
    print('\n' * y, ' ' * x, '.')


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
    main()
