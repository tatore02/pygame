import pygame as pg
import random

pg.init()

#image
IMAGE_PATH = "asteroids/image/"
global player
player = pg.image.load(IMAGE_PATH + "player.png")
astSmall = pg.image.load(IMAGE_PATH + "astSmall.png")
astBig = pg.image.load(IMAGE_PATH + "astBig.png")
background = pg.image.load(IMAGE_PATH + "background.png")
pauseIcon = pg.image.load(IMAGE_PATH + "pause.png")
pauseIcon = pg.transform.scale(pauseIcon, (50,50))

#COSTANTI
WIDTH = 1228
HEIGHT = 670
DISPLAY = pg.display.set_mode((WIDTH,HEIGHT))
UNIT_SIZE = 3
FPS = 30

def start():
    global clock,playerX,playerY,playerRotation,life,fps
    clock = pg.time.Clock()
    playerX = WIDTH/2
    playerY = HEIGHT/2
    playerRotation = 0
    life = 3
    fps = 0

def draw():
    DISPLAY.blit(background, (0,0))
    global player
    player = pg.transform.rotate(player, playerRotation)
    DISPLAY.blit(player, (playerX,playerY))
    pg.display.set_caption(f"FPS: {fps:.2f}")

def update():
    pg.display.update()
    clock.tick(FPS)

def pause():
    restart = False
    while not restart:
        DISPLAY.blit(pauseIcon,(WIDTH/2-20,0))
        update()
        pg.time.delay(100)
        DISPLAY.blit(pauseIcon,(WIDTH/2-20,0))
        update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                restart = True
            if event.type == pg.QUIT:
                pg.quit()


start()
while True:
    draw()
    update()

    fps = clock.get_fps()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            pause()

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        playerY -= UNIT_SIZE*2
    if keys[pg.K_DOWN]:
        playerY += UNIT_SIZE*2
    playerRotation = 0
    if keys[pg.K_RIGHT]:
        playerRotation += UNIT_SIZE
    if keys[pg.K_LEFT]:
        playerRotation -= UNIT_SIZE
