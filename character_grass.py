from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas()
grass.draw_now(400,30)
character.draw_now(400,90)
delay(1)

def run_circle():
    print('CIRCLE')
    pass
def run_retangle():
    print('RETANGLE')
    pass

while True:
    run_circle()
    run_retangle()





close_canvas()
