import pygame
import random

pygame.init()

#COSTANTI
DISPLAY = pygame.display.set_mode((600,600))
UNIT_SIZE = 40

#VARIABILI GLOBALI
listFlower = []

#IMMAGINI
PATH = "pratoFiorito/immagini/"
flower = pygame.image.load(PATH + 'flower.png')
flower = pygame.transform.scale(flower, (UNIT_SIZE,UNIT_SIZE))

def start():
    for i in range(0,10):
        x = random.randint(0,15) * UNIT_SIZE
        y = random.randint(0,15) * UNIT_SIZE
        r = pygame.Rect((x,y),(UNIT_SIZE,UNIT_SIZE))
        listFlower.append(r)
        pygame.draw.rect(DISPLAY,'white',r)
        DISPLAY.blit(flower,(x,y))

def update():
    pygame.display.update()

def draw():
    for i in range(0,601,UNIT_SIZE):
        pygame.draw.line(DISPLAY,'white',(i,0),(i,600))
        pygame.draw.line(DISPLAY,'white',(0,i),(600,i))

start()

while True:
    draw()
    update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for r in listFlower:
                if pygame.Rect.collidepoint(r,pos[0],pos[1]):
                    print('hai perso')