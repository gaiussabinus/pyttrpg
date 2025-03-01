from screeninfo import get_monitors
import pygame

pygame.init()

monitors = get_monitors()
FONT = "comicsans"
SCREEN_WIDTH = int(monitors[0].width)
SCREEN_HEIGHT = int(monitors[0].height)
LABEL_FONT = pygame.font.SysFont("comicsans", 24)
