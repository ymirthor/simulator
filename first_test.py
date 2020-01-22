import pygame
import math

def car_display(angle, pos, size = (20,10), color = (20,200,20)):
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
    car_display(0, (x,y))


WIDTH, HEIGHT = 200, 200
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


time = 0
running = True
while running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time += 0.001
    car_path(time)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
