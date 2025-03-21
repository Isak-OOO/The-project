import pygame as p

p.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = p.Rect((400, 300, 10, 20))
clock = p.time.Clock()

run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    p.draw.rect(screen, "white", player)
    
p.quit()