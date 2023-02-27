import pygame

pygame.init()

#COSTANTI
DISPLAY = pygame.display.set_mode((600,600))
UNIT_SIZE = 200
player1 = 'x'
player2 = 'o'
#IMMAGINI
X = pygame.image.load('ticTacToe/x.webp')
X = pygame.transform.scale(X, (UNIT_SIZE,UNIT_SIZE))
O = pygame.image.load('ticTacToe/o.png')
O = pygame.transform.scale(O, (UNIT_SIZE,UNIT_SIZE))
#VARIABILI GLOBALI
cellList = []
player = player1

def start():
    for x in range(0,600,UNIT_SIZE):
        for y in range(0,600,UNIT_SIZE):
            c = Cell(x,y)
            cellList.append(c)

def draw():
    #line
    for i in range(UNIT_SIZE,600,UNIT_SIZE):
        pygame.draw.line(DISPLAY,'white',(i,0),(i,600))
        pygame.draw.line(DISPLAY,'white',(0,i),(600,i))
    #segni
    for i in cellList:
        if i.segno == 'x':
            DISPLAY.blit(X,(i.x,i.y))
        elif i.segno == 'o':
            DISPLAY.blit(O,(i.x,i.y))
      
def update():
    pygame.display.update()
    pygame.time.Clock()

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.segno = None
    def assegna(self,player):
        if self.segno != None:
            self.segno = player
    def checkCollision(self,mX,mY):
        if mX > self.x and mX < self.x+UNIT_SIZE and mY > self.y and mY < self.y+UNIT_SIZE:
            return True
        else:
            return False

start()

run = True
while run:
    update()
    draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for c in cellList:
                if c.segno != None:
                    if c.checkCollision(pos[0],pos[1]):
                        print('OK')
                        c.assegna(player)


        if event.type == pygame.QUIT:
            run = False

    #change player
    if player == player1:
        player = player2
    else:
        player = player1
pygame.quit()