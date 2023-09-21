from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas()
grass.draw_now(400,30)
character.draw_now(400,90)










close_canvas()
