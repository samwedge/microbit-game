from microbit import *
import time
import random


def pixels_to_image(pixels):
    pixels_str = ':'.join(
        [''.join(
            [str(v) for v in row]
        ) for row in pixels]
    )

    return Image(pixels_str)


def row_from_pos(pos):
    return [
        9 if pos == 0 else 0,
        9 if pos == 1 else 0,
        9 if pos == 2 else 0,
        9 if pos == 3 else 0, 
        9 if pos == 4 else 0,
    ]


def update_player_pos(pos):
    left = button_a.get_presses()
    right = button_b.get_presses()

    movement = right - left

    pos += movement

    if pos < 0:
        pos = 0
    if pos > 4:
        pos = 4
   
    return pos






player_pos = 2
frame_start = time.ticks_ms()
frame_duration = 1000
enemy_row_1 = [0, 0, 0, 0, 0]
enemy_row_2 = [0, 0, 0, 0, 0]
enemy_row_3 = [0, 0, 0, 0, 0]
enemy_row_4 = [0, 0, 0, 0, 0]


while True:

    player_pos = update_player_pos(player_pos)

    current_time = time.ticks_ms()
    if time.ticks_diff(current_time, frame_start) >= frame_duration:
        frame_start = current_time
        enemy_pos = random.randint(0, 4)
        enemy_row_4 = enemy_row_3
        enemy_row_3 = enemy_row_2
        enemy_row_2 = enemy_row_1
        enemy_row_1 = row_from_pos(enemy_pos)

    player_row = row_from_pos(player_pos)

    pixels = [
        enemy_row_1,
        enemy_row_2,
        enemy_row_3,
        enemy_row_4,
        player_row,
    ]

    display.show(pixels_to_image(pixels))

