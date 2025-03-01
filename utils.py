import pygame

def mouse_handler():
    postion = pygame.mouse.get_pos()
    button_pressed = ""
    if pygame.mouse.get_pressed()[0]:
        button_pressed = "left_click"
        return button_pressed, postion
    if pygame.mouse.get_pressed()[1]:
        button_pressed = "middle_click"
        return button_pressed, postion
    if pygame.mouse.get_pressed()[2]:
        button_pressed = "right_click"
        return button_pressed, postion


def keyboard_handler(key_press):
        key = pygame.key.name(key_press)
        if key == "enter":
            key = "\n"
        if key == "spacebar":
            key = " "

        return key

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_handler()
        if event.type == pygame.KEYDOWN:
            return str(keyboard_handler(event.key))
