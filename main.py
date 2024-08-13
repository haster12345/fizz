import time
import os
import keyboard

FPS = 30
LEFT_BOUND = 0
RIGHT_BOUND = 30
UP_BOUND = 0
DOWN_BOUND = 30
TIME_TO_MOVE = 1  # every interation we move/ ie if this was 30 every 30 iterations we would move


def main():
    refresh_counter = 0
    move_counter = 0
    moving_left = False
    moving_right = False

    while True:
        if keyboard.is_pressed("d"):
            moving_right = True
            moving_left = False
        elif keyboard.is_pressed("a"):
            moving_left = True
            moving_right = False

        refresh_counter += 1
        if refresh_counter % TIME_TO_MOVE == 0:
            if moving_right:
                move_counter += 1
            elif moving_left:
                move_counter -= 1

        move(move_counter)
        refresh()


# Lines below allow it to move on its own
        # if move_counter >= RIGHT_BOUND:
        #     moving_right = False
        #     hit_left = True
        # elif move_counter <= LEFT_BOUND:
        #     moving_right = True
        #     hit_left = False


def refresh():
    """
    there is 1000 miliseconds in a second
    and we want 30 fps so that means we want 1 frame every 33 milliseconds
    """
    time.sleep(FPS/1000)
    os.system('cls')
    return


def move(left_move_counter):
    print(' ' * left_move_counter,  '.')
    return


if __name__ == '__main__':
    main()
