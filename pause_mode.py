import game_framework
import play_mode
import title_mode
from pico2d import *


def init():
    pass


def finish():
    pass


def handle_events(event_list=None):
    if event_list is None:
        event_list = get_events()
    for index, event in enumerate(event_list):
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            play_mode.handle_events(event_list[index + 1:])
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            game_framework.change_mode(title_mode)
            return
        elif (event.type in (SDL_KEYDOWN, SDL_KEYUP) and
              event.key in (SDLK_LEFT, SDLK_RIGHT)):
            play_mode.paused_key_events.append(event)


def update():
    pass


def render():
    play_mode.render()
