from pico2d import *
import game_framework
import game_world
import pause_mode
import title_mode
from boy import Boy
from grass import Grass

pause_started_at = None
paused_key_events = []


def handle_events(event_list=None):
    global boy
    if event_list is None:
        event_list = get_events()
    for index, event in enumerate(event_list):
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            pause_mode.handle_events(event_list[index + 1:])
            return
        else:
            boy.handle_event(event)



def init():
    global boy


    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    global pause_started_at
    pause_started_at = get_time()
    paused_key_events.clear()


def resume():
    global pause_started_at
    boy.idle_started_at += get_time() - pause_started_at
    pause_started_at = None
    for event in paused_key_events:
        boy.handle_event(event)
    paused_key_events.clear()


def finish():
    global boy, pause_started_at
    game_world.clear()
    boy = None
    pause_started_at = None
    paused_key_events.clear()
