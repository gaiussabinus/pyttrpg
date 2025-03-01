#!/usr/bin/env python3

import pygame
import time
from dice import *
from utils import *
from const import *

pygame.init()

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Label:
    def __init__(self,x,y,color,text):
        self.x = x
        self.y = y
        self.color = color
        self.text = text

    def update_text(self, input_text):
        if input_text[len(input_text)] == "backspace":
            input_text = input_text[:-1]
            return input_text
        else:
            return


    def draw(self, win):
        pygame.draw.rect(win, self.color, (0,0,self.x,self.y))
        label = LABEL_FONT.render(self.text,1,"black")
        win.blit(label, (5,5))

def main_loop():
    display_text = ""
    run = True
    menu = False
    start_time = time.time()
    message_label = Label(200,200,"red",display_text)

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time
        event = event_handler()
        if event is not None and len(event) >=1:
            display_text += event
            print(display_text)
        message_label.update_text(display_text)
        message_label.draw(display_surface)
        pygame.display.update()



'''
class Button():
    pass

class Phys_Obj():
    pass
'''


if __name__ == "__main__":
    main_loop()
