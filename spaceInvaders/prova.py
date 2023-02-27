import pygame

pygame.init()

UNIT_SIZE = 40
display = pygame.display.set_mode((600,600))
    
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(30)

def disegna():
    for i in range(0,601,UNIT_SIZE):
        pygame.draw.line(display,'green',(i,0),(i,600))
        pygame.draw.line(display,'green',(0,i),(600,i))
    #STEP 1
    y = 600 - UNIT_SIZE
    for i in range(0,3):
        x = UNIT_SIZE * 3
        for j in range(0,2):
            r = pygame.Rect(x,y,UNIT_SIZE,UNIT_SIZE)
            pygame.draw.rect(display,'green',r)
            x += UNIT_SIZE
        y -= UNIT_SIZE
    #STEP 2
    y = 600 - UNIT_SIZE
    for i in range(0,3):
        x = UNIT_SIZE * 8
        for j in range(0,2):
            r = pygame.Rect(x,y,UNIT_SIZE,UNIT_SIZE)
            pygame.draw.rect(display,'green',r)
            x += UNIT_SIZE
        y -= UNIT_SIZE
    #STEP 3
    y += UNIT_SIZE
    for i in range(0,2):
        x = UNIT_SIZE * 7
        for j in range(0,3):
            r = pygame.Rect(x,y,UNIT_SIZE,UNIT_SIZE)
            pygame.draw.rect(display,'green',r)
            x -= UNIT_SIZE
        y -= UNIT_SIZE
    #STEP 4
    L = 600
    pygame.draw.polygon(display,'green',[(UNIT_SIZE*5,L-UNIT_SIZE),(UNIT_SIZE*5,L-UNIT_SIZE*2),(UNIT_SIZE*6,L-UNIT_SIZE*2)])
    pygame.draw.polygon(display,'green',[(UNIT_SIZE*7,L-UNIT_SIZE*2),(UNIT_SIZE*8,L-UNIT_SIZE*2),(UNIT_SIZE*8,L-UNIT_SIZE)])
    #STEP 5
    pygame.draw.polygon(display,'green',[(UNIT_SIZE*3,L-UNIT_SIZE*3),(UNIT_SIZE*4,L-UNIT_SIZE*3),(UNIT_SIZE*4,L-UNIT_SIZE*4)])
    pygame.draw.polygon(display,'green',[(UNIT_SIZE*9,L-UNIT_SIZE*4),(UNIT_SIZE*9,L-UNIT_SIZE*3),(UNIT_SIZE*10,L-UNIT_SIZE*3)])
    #STEP 6
    r = pygame.Rect(UNIT_SIZE*4,L-UNIT_SIZE*4,UNIT_SIZE,UNIT_SIZE)
    pygame.draw.rect(display,'green',r)
    r = pygame.Rect(UNIT_SIZE*8,L-UNIT_SIZE*4,UNIT_SIZE,UNIT_SIZE)
    pygame.draw.rect(display,'green',r)


while True:

    disegna()
    aggiorna()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
