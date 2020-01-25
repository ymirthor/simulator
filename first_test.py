import pygame
import math
HEIGHT = 500
WIDTH = 1000
WINDOW_SIZE = (WIDTH, HEIGHT)

WHITE = (255,255,255)
BLACK = (0,0,0)

def center(length1, length2):
    return int(length1)//2 - int(length2)//2

def rect_display(window, angle, pos, size = (20,10), color = (20,200,20)):
    radians = angle * (math.pi / 180)
    x, y = pos
    w, h = size

    # Polarform = r*cos(theta), r*sin(theta)
    change_x, change_y = w/2, h/2
    radius = math.sqrt(change_x**2 + change_y**2)

    theta = math.atan(change_y / change_x) + radians
    p1 = (radius * math.cos(theta) + x, radius * math.sin(theta) + y)
    theta = math.atan(change_y / -change_x) + radians
    p2 = (radius * math.cos(theta) + x, radius * math.sin(theta) + y)
    theta = math.atan(-change_y / -change_x) + math.pi + radians
    p3 = (radius * math.cos(theta) + x, radius * math.sin(theta) + y)
    theta = math.atan(-change_y / change_x) + math.pi + radians
    p4 = (radius * math.cos(theta) + x, radius * math.sin(theta) + y)
    coordinates = [p1,p2,p3,p4]

    pygame.draw.polygon(window, color, coordinates)

def car_path(time = 0, start = (40,40), end = (190,190)):
    start_x, end_x, start_y, end_y = start[0], end[0], start[1], end[1]
    x,y = end_x-start_x*time, end_y-start_y*time
    rect_display(0, (x,y))

def check_click_on(rect, ret):
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if (rect[0] <= pos[0] <= rect[2] + rect[0]) and (rect[1] <= pos[1] <= rect[3] + rect[1]) and pressed[0]:
        return ret
    else:
        return False

def menu_button_display(window, color, pos, size, myfont, text = "", textColor = WHITE):
    button = pygame.draw.rect(window, color, [pos,size])

    textsurface = myfont.render(str(text), True, textColor)
    pos = [pos[0] + size[0]//2 - textsurface.get_rect()[2]//2, 
           pos[1] + size[1]//2 - textsurface.get_rect()[3]//2]

    window.blit(textsurface, pos)
    return button

def menu_display(window, myfont):
    margin = 200 # Sides
    margin_top = 100
    spacing = 5
    button_height = 100
    button_width = WIDTH - (2 * margin)
    buttons_size = (button_width, button_height)
    button_center = center(WIDTH, button_width)
    next = spacing + button_height

    pos = (button_center, margin_top)
    button = menu_button_display(window, BLACK, pos, buttons_size, myfont, "Play")
    screen = check_click_on(button, 3)

    pos = (button_center, margin_top + 1*next)
    button = menu_button_display(window, BLACK, pos, buttons_size, myfont, "Map")
    if not screen:
        screen = check_click_on(button, 2)

    pos = (button_center, margin_top + 2*next)
    button = menu_button_display(window, BLACK, pos, buttons_size, myfont, "Settings")
    if not screen:
        screen = check_click_on(button, 4)
    
    return screen

def back_button(window, color, pos = (10,10), size = (50,50)):
    button = pygame.draw.rect(window, color, [pos,size])

    x, y = size
    arrow_ = x - x * 0.2
    arrow_size = math.sqrt(2 * ((arrow_//2) ** 2))
    x_pos = pos[0] + x // 2
    y_pos = pos[1] + y // 2

    thickness = 5
    xside = math.sqrt(2 * (thickness ** 2))
    yside = arrow_ - xside
    size2 = yside // 2
    size2 += 3
    rect_display(window, 45, (x_pos, y_pos), (arrow_size, arrow_size), WHITE)
    rect_display(window, 45, (x_pos + xside, y_pos), (size2, size2), BLACK)
    return button

def map_display(window, myfont):
    screen = check_click_on(back_button(window, BLACK), 1)
    textsurface = myfont.render("Map", True, BLACK)
    window.blit(textsurface, (40,100))
    return screen

def game_display(window, myfont):
    screen = check_click_on(back_button(window, BLACK), 1)
    textsurface = myfont.render("Game", True, BLACK)
    window.blit(textsurface, (40,100))

    rect_display(window, 45, (400,400), (100,50))
    return screen

def settings_display(window, myfont):
    screen = check_click_on(back_button(window, BLACK), 1)
    textsurface = myfont.render("Settings", True, BLACK)
    window.blit(textsurface, (40,100))
    return screen

def game():
    pygame.font.init()
    myfont = pygame.font.SysFont('arial', 40)
    window = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    pressed = pygame.key.get_pressed()
    screen = 1
    screens = {1 : menu_display,
               2 : map_display,
               3 : game_display,
               4 : settings_display}

    running = True
    while running:
        window.fill(WHITE)
        change_screen = screens[screen](window, myfont)
        if change_screen:
            screen = change_screen
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(10)

game()

pygame.quit()