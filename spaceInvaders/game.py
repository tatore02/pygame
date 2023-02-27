import pygame
import random

pygame.init()

#immagini
PATH = "spaceInvaders/immagini/"
player = pygame.image.load(PATH + "player.png")
green = pygame.image.load(PATH + "green.png")
background = pygame.image.load(PATH + "background.png")
shot = pygame.image.load(PATH + "shot.png")
shot.fill(color='GREEN')
enemy = pygame.image.load(PATH + "red.png")
heart = pygame.image.load(PATH + "heart.png")

#COSTANTI
WIDTH = 1228
HEIGHT = 670
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
UNIT_SIZE = 3
WALL_SIZE = 15
FPS = 50
ENEMY_WIDTH = enemy.get_width()
ENEMY_HEIGHT = enemy.get_height()
FONT = pygame.font.SysFont('Comic Sans MS', 30, bold=True)


#VARIABILI GLOBALI
shots = []
enemies = []
shotsEnemies = []
life = 3
walls = []

#CLASSI
class Shot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def drawShot(self):
        if self.y > 0:
            self.y -= UNIT_SIZE * 2
            DISPLAY.blit(shot, (self.x,self.y))
        else:
            shots.remove(self)
    def checkCollisionWall(self):
        for w in walls:
            if self.x > w.x and self.x < w.x+WALL_SIZE and self.y > w.y and self.y < w.y+WALL_SIZE:
                walls.remove(w)
                return True

class ShotEnemy(Shot):
    def drawShot(self):
        if self.y < 670:
            self.y += UNIT_SIZE*2
            DISPLAY.blit(shot, (self.x,self.y))
        else:
            shotsEnemies.remove(self)
    def checkCollisionPlayer(self):
        if self.x > playerX and self.x < playerX+player.get_width() and self.y > playerY:
            shotsEnemies.remove(self)
            return True

class Enemy:
    def __init__(self,x,y):
        self.xPart = x  #coordinate di partenza
        self.yPart = y
        self.x = x  #coordinate mobili
        self.y = y
        self.vel = UNIT_SIZE
        self.direction = 'r'
    def drawEnemy(self):
        DISPLAY.blit(enemy, (self.x,self.y))
    def move(self):
        #muovi a destra o sinistra
        if self.x == self.xPart + (UNIT_SIZE*25):
            self.direction = 'l'
        elif self.x == self.xPart - (UNIT_SIZE*25):
            self.direction = 'r'
        #cambia direzione
        if self.direction == 'r':
            self.x += UNIT_SIZE/3
        elif self.direction == 'l':
            self.x -= UNIT_SIZE/3
        #muovi i nemici verso il basso

    def checkCollision(self):
        #collision with player
        if self.x > playerX and self.x < playerX+player.get_width() and self.y > playerY:
            life -= 1
            enemies.remove(self)
        #collision with shots
        for s in shots:
            if s.x > self.x and s.x < self.x+ENEMY_WIDTH and s.y > self.y and s.y < self.y+ENEMY_HEIGHT:
                shots.remove(s)
                return True
        return False
    
def createWall(x,y):
    #STEP 1
    tmpX = x
    tmpY = y
    for i in range(0,3):
        x = tmpX
        for j in range(0,2):
            r = pygame.Rect(x,y,WALL_SIZE,WALL_SIZE)
            walls.append(r)
            x += WALL_SIZE
        y -= WALL_SIZE
    #STEP 2
    y = tmpY
    for i in range(0,3):
        x = tmpX + WALL_SIZE * 5
        for j in range(0,2):
            r = pygame.Rect(x,y,WALL_SIZE,WALL_SIZE)
            walls.append(r)
            x += WALL_SIZE
        y -= WALL_SIZE
    #STEP 3
    y += WALL_SIZE
    for i in range(0,2):
        x = tmpX + WALL_SIZE * 4
        for j in range(0,3):
            r = pygame.Rect(x,y,WALL_SIZE,WALL_SIZE)
            walls.append(r)
            x -= WALL_SIZE
        y -= WALL_SIZE
    #non aggiungo i poligoni poichè essi non prevedono un costruttore, ma solo una funzione per disegnarli al momento

def start():
    global playerX, playerY
    playerX = WIDTH/2 - player.get_width()/2
    playerY = HEIGHT-20 - player.get_height()
    #creazione nemici
    for j in range(50,351,100):
        for i in range(100,1101,200):
            enemies.append(Enemy(i,j))
    #creazione muri
    createWall(108,HEIGHT-100)
    createWall(415,HEIGHT-100)
    createWall(722,HEIGHT-100)
    createWall(1029,HEIGHT-100)

def draw():
    DISPLAY.blit(background, (0,0))
    DISPLAY.blit(player, (playerX,playerY))
    if life == 3:
        DISPLAY.blit(heart,(1100,0))
        DISPLAY.blit(heart,(1140,0))
        DISPLAY.blit(heart,(1180,0))
    elif life == 2:
        DISPLAY.blit(heart,(1140,0))
        DISPLAY.blit(heart,(1180,0))
    elif life == 1:
        DISPLAY.blit(heart,(1180,0))

    for e in enemies:
        e.drawEnemy()
    for w in walls:
        pygame.draw.rect(DISPLAY,'green',w)
    for s in shots:
        s.drawShot()
    for s in shotsEnemies:
        s.drawShot()

    #debug
    #puntiRender = FONT.render(str(nTurn), 1, (255,255,255))
    #DISPLAY.blit(puntiRender, (100,0))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    
start()

while life > 0:
    draw()
    update()

    for e in enemies:
        e.move()
        if e.checkCollision():
            enemies.remove(e)
    
    for s in shotsEnemies:
        if s.checkCollisionPlayer():
            life -= 1
    for s in shotsEnemies:
        if s.checkCollisionWall():
            shotsEnemies.remove(s)
    for s in shots:
        if s.checkCollisionWall():
            shots.remove(s)

    if pygame.time.get_ticks()%20 == 0:
        r = random.randint(0,len(enemies)-1)
        shotsEnemies.append(ShotEnemy(enemies[r].x+ENEMY_WIDTH/2,enemies[r].y+ENEMY_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shots.append(Shot(playerX + player.get_width()/2, playerY))

        if event.type == pygame.QUIT:
            pygame.quit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= UNIT_SIZE*2
    if keys[pygame.K_RIGHT]:
        playerX += UNIT_SIZE*2