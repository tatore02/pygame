import pygame
import random

pygame.init()

#COSTANTI
FPS = 10
DISPLAY = pygame.display.set_mode((500,500))
UNIT_SIZE = 25

#variabili
direction = 'r'
gameOver = False
bodyParts = 1
playerX = list()
playerY = list()
playerX.append(250)
playerY.append(250)
#player = pygame.Rect(playerX,playerY,UNIT_SIZE,UNIT_SIZE)


appleX = int(random.randint(0,21)) * UNIT_SIZE
appleY = int(random.randint(0,21)) * UNIT_SIZE
apple = pygame.Rect(appleX,appleY,UNIT_SIZE,UNIT_SIZE)

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def draw():
    DISPLAY.fill('black')
    i=0
    while i < bodyParts:
        pygame.draw.rect(DISPLAY, 'green', [playerX[i], playerY[i], UNIT_SIZE, UNIT_SIZE])
        i += 1
    pygame.draw.rect(DISPLAY, 'red', [appleX, appleY, UNIT_SIZE, UNIT_SIZE])

    i=0
    while i < 500:
        pygame.draw.line(DISPLAY, 'white', (i,0),(i,500))
        i += UNIT_SIZE
    i=0
    while i < 500:
        pygame.draw.line(DISPLAY, 'white', (0,i),(500,i))
        i += UNIT_SIZE

def move():
    if bodyParts > 1:
        i = bodyParts
        while i > 0:
            playerX[i] = playerX[i-1]
            playerY[i] = playerY[i-1]
            i -= 1
    if direction == 'r':
        playerX[0] += UNIT_SIZE
    if direction == 'l':
        playerX[0] -= UNIT_SIZE
    if direction == 'u':
        playerY[0] -= UNIT_SIZE
    if direction == 'd':
        playerY[0] += UNIT_SIZE

def checkCollision():
    if playerX[0] > 500 or playerX[0] < 0 or playerY[0]>500 or playerY[0]<0:
          return True
    if bodyParts > 1:
        i=0
        while i > 0:
            if playerY[0] == playerX[i] and playerY[0] == playerY[i]:
                return True
            i -= 1
    return False

def upgradeApple():
    pygame.draw.rect(DISPLAY, 'black', [appleX, appleY, UNIT_SIZE, UNIT_SIZE])
    global appleX
    appleX = int(random.randint(0,21)) * UNIT_SIZE
    global appleY
    appleY = int(random.randint(0,21)) * UNIT_SIZE
    playerX.append(None)
    playerY.append(None)
    bodyParts += 1


 

while not gameOver:
    move()
    draw()
    update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if direction != 'r':
                direction = 'l'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if direction != 'l':
                direction = 'r'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if direction != 'd':
                direction = 'u'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if direction != 'p':
                direction = 'd'

        if event.type == pygame.QUIT:
            gameOver = True

    if playerX[0] == appleX and playerY[0] == appleY:
        upgradeApple()

    if checkCollision():
         break

pygame.quit()