# pylint: disable-all

# push-up counter sample

from microbit import *

count = 0
is_down = False
is_complete = False
total = 5
wait_time = 1500

while True:
    # reset
    if button_a.is_pressed():
        count = 0
        is_complete = False
        is_down = False
    if is_complete:
        display.show(Image.HAPPY)
    else:
        light_level = display.read_light_level()
        if (not is_down) and (light_level < 40):
            count = count + 1
            display.show(count)
            if count >= total:
                is_complete = True
            sleep(wait_time)
            is_down = True
        else:
            display.clear()
            if light_level >= 40:
                is_down = False
        
