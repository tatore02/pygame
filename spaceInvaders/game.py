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
shotEnemy = pygame.image.load(PATH + "shot.png")
shotEnemy.fill(color='RED')
enemyRed = pygame.image.load(PATH + "red.png")
enemyGreen = pygame.image.load(PATH + "green.png")
enemyYellow = pygame.image.load(PATH + "yellow.png")
heart = pygame.image.load(PATH + "heart.png")
gameover = pygame.image.load(PATH + "gameover.png")
gameover = pygame.transform.scale(gameover,(688,420))

#COSTANTI
WIDTH = 1228
HEIGHT = 670
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
UNIT_SIZE = 3
WALL_SIZE = 15
FPS = 45
ENEMY_WIDTH = enemyRed.get_width()
ENEMY_HEIGHT = enemyRed.get_height()
SHOT_WIDTH = shot.get_width()
SHOT_HEIGHT = shot.get_height()
FONT = pygame.font.SysFont('Comic Sans MS', 30, bold=True)

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
    def checkCollisionShotEnemy(self):
        for s in shotsEnemies:
            if self.x >= s.x-UNIT_SIZE and self.x+UNIT_SIZE <= s.x+SHOT_WIDTH and self.y >= s.y and self.y <= s.y+SHOT_HEIGHT:
                shots.remove(self)
                shotsEnemies.remove(s)

class ShotEnemy(Shot):
    def drawShot(self):
        if self.y < 670:
            self.y += UNIT_SIZE*2
            DISPLAY.blit(shotEnemy, (self.x,self.y))
        else:
            shotsEnemies.remove(self)
    def checkCollisionPlayer(self):
        if self.x > playerX and self.x < playerX+player.get_width() and self.y > playerY:
            shotsEnemies.remove(self)
            return True

class Enemy:
    vel = UNIT_SIZE/2
    def __init__(self,x,y,color):
        self.xPart = x  #coordinate di partenza
        self.yPart = y
        self.x = x  #coordinate mobili
        self.y = y
        self.color = color
        self.direction = 'r'
        self.nTurn = 0
    def drawEnemy(self):
        if self.color == 'red':
            DISPLAY.blit(enemyRed, (self.x,self.y))
        elif self.color == 'green':
            DISPLAY.blit(enemyGreen, (self.x,self.y))
        elif self.color == 'yellow':
            DISPLAY.blit(enemyYellow, (self.x,self.y))

    def move(self):
        #cambia direzione
        if self.x == self.xPart + (UNIT_SIZE*25):
            self.direction = 'l'
        elif self.x == self.xPart - (UNIT_SIZE*25):
            self.direction = 'r'
            self.nTurn += 1
        #debug out of the screen
        if self.x < 10:
            self.direction = 'r'
        if self.x > WIDTH-10:
            self.direction = 'l'
        #muovi a destra o sinistra
        if len(enemies) == 16:
            Enemy.vel = (UNIT_SIZE *2)/3
        if len(enemies) == 11:
            Enemy.vel = UNIT_SIZE
        if self.direction == 'r':
            self.x += Enemy.vel
        elif self.direction == 'l':
            self.x -= Enemy.vel
        #muovi i nemici verso il basso
        if (self.y + ENEMY_HEIGHT) < (HEIGHT-200):
            if self.nTurn == 1:
                self.y += UNIT_SIZE*4
                self.nTurn = 0

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

def start(punteggio=0):
    global shots,enemies,shotsEnemies,life,walls,points,clock,fps,probabilitaSparo
    shots = []
    enemies = []
    shotsEnemies = []
    life = 3
    walls = []
    points = punteggio
    clock = pygame.time.Clock()
    fps = 0
    probabilitaSparo = 20
    
    global playerX, playerY
    playerX = WIDTH/2 - player.get_width()/2
    playerY = HEIGHT-20 - player.get_height()
    #creazione nemici
    for j in range(50,351,100):
        for i in range(100,1101,200):
            if j==50:
                enemies.append(Enemy(i,j,"yellow"))
            elif j==150:
                enemies.append(Enemy(i,j,"green"))
            else:
                enemies.append(Enemy(i,j,"red"))
    #creazione muri
    createWall(108,HEIGHT-100)
    createWall(415,HEIGHT-100)
    createWall(722,HEIGHT-100)
    createWall(1029,HEIGHT-100)

def draw():
    DISPLAY.blit(background, (0,0))
    DISPLAY.blit(player, (playerX,playerY))
    puntiRender = FONT.render(str(points), False, (255,255,255))
    DISPLAY.blit(puntiRender, (100,0))
    pygame.display.set_caption(f"FPS: {fps:.2f}")
    
    i=0
    x=1180 #coordinata x del cuore
    while i<life:
        DISPLAY.blit(heart,(x,0))
        x-=40
        i+=1

    for e in enemies:
        e.drawEnemy()
    for w in walls:
        pygame.draw.rect(DISPLAY,'green',w)
    for s in shots:
        s.drawShot()
    for s in shotsEnemies:
        s.drawShot()

def update():
    pygame.display.update()
    clock.tick(FPS)

def gameOver():
    DISPLAY.blit(gameover, (270,0))
    restartRender = FONT.render("press SPACE to restart game", False, (255,255,255))
    DISPLAY.blit(restartRender,(400,HEIGHT-250))
    update()
    #intrappoliamo il giocatore in nuovo ciclo finchè non preme SPAZIO
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                restart = True
                start()
            if event.type == pygame.QUIT:
                pygame.quit()

def pause():
    pauseRender = FONT.render("PAUSE", False, 'white')
    pauseRenderHide = FONT.render("PAUSE", False, 'black')
    restart = False
    while not restart:
        DISPLAY.blit(pauseRender,(550,0))
        update()
        pygame.time.delay(100)
        DISPLAY.blit(pauseRenderHide,(550,0))
        update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                restart = True
            if event.type == pygame.QUIT:
                pygame.quit()

start()

while True:
    draw()
    update()

    fps = clock.get_fps()

    for e in enemies:
        e.move()
        if e.checkCollision():
            points += 1
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
    for s in shots:
        s.checkCollisionShotEnemy()

    if len(enemies) < 15:
        probabilitaSparo = 18
    if len(enemies) < 10:
        probabilitaSparo = 15
    if len(enemies) == 3:
        probabilitaSparo = 18

    if pygame.time.get_ticks()%probabilitaSparo == 0: #probabilità sparo nemico
        r = random.randint(0,len(enemies)-1)    #scelgo nemico casuale
        shotsEnemies.append(ShotEnemy(enemies[r].x+ENEMY_WIDTH/2,enemies[r].y+ENEMY_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shots.append(Shot(playerX + player.get_width()/2, playerY))

        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            pause()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= UNIT_SIZE*2
    if keys[pygame.K_RIGHT]:
        playerX += UNIT_SIZE*2

    if len(enemies) <= 0:
        start(points)
    
    if life <= 0:
        draw()
        gameOver()

#da quando ho aggiunto il punteggio, il gioco lagga su MAC