# pylint: disable-all

# push-up counter sample

from microbit import *
count = 0
is_down = False
is_complete = False
while True:
    if is_complete:
        display.show(Image.HAPPY)
    else:
        light_level = display.read_light_level()
        if (not is_down) and (light_level < 40):
            count = count + 1
            display.show(count)
            if count >= 9:
                is_complete = True
            sleep(2000)
            is_down = True
        else:
            display.clear()
            if light_level >= 40:
                is_down = False
        
