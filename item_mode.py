from pico2d import *

image = None
opened = False


def init():
    global image, opened
    image = load_image('item_select.png')
    opened = False


def finish():
    global image, opened
    image = None
    opened = False


def handle_event(event, boy):
    global opened
    if event.type != SDL_KEYDOWN:
        return False
    if event.key == SDLK_i:
        opened = not opened
        return True
    if opened:
        choices = {
            SDLK_0: 0, SDLK_KP_0: 0,
            SDLK_1: 1, SDLK_KP_1: 1,
            SDLK_2: 2, SDLK_KP_2: 2,
        }
        if event.key in choices:
            boy.ball_type = choices[event.key]
            return True
    return False


def render(boy):
    if not opened:
        return
    x, y = get_canvas_width() - 150, get_canvas_height() - 125
    image.draw(x, y)
    selected_y = y + {0: 65, 1: 0, 2: -65}[boy.ball_type]
    draw_rectangle(x - 130, selected_y - 25, x + 130, selected_y + 25)
