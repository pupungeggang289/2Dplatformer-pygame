import pygame

import asset
import var
import const
import UI
import lang

import physics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(const.Font.title.render(lang.lang[var.lang]['game_title'], True, const.Color.black), UI.title_text)
    pygame.display.flip()

def mouse_up(x, y, button):
    pass