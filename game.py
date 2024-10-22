from microbit import *

def pixels_to_image(pixels):
    pixels_str = ':'.join(
        [''.join(
            [str(v) for v in row]
        ) for row in pixels]
    )

    return Image(pixels_str)


player_pos = 2


while True:

    left = button_a.get_presses()
    right = button_b.get_presses()

    movement = right - left

    player_pos += movement

    if player_pos < 0:
        player_pos = 0
    if player_pos > 4:
        player_pos = 4

    player_row = [
        9 if player_pos == 0 else 0,
        9 if player_pos == 1 else 0,
        9 if player_pos == 2 else 0,
        9 if player_pos == 3 else 0, 
        9 if player_pos == 4 else 0,
    ]

    pixels = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        player_row,
    ]

    display.show(pixels_to_image(pixels))

