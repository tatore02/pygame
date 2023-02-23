#AGGIUNGERE SUONI e schermata gameOver con record
import pygame
import random

pygame.init()

#IMMAGINI
PATH = "game/flappyBird/immagini/"
sfondo = pygame.image.load(PATH + "sfondo.png")
uccello = pygame.image.load(PATH + 'uccello.png')
base = pygame.image.load(PATH + 'base.png')
gameover = pygame.image.load(PATH + 'gameover.png')
tuboGiu = pygame.image.load(PATH + 'tubo.png')
tuboSu = pygame.transform.flip(tuboGiu,False,True)

#COSTANTI
SCHERMO = pygame.display.set_mode((288,512))
FPS = 50
VEL_AVANZ = 3
FONT = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

class Tubo:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)
    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(tuboGiu, (self.x,self.y+210))
        SCHERMO.blit(tuboSu, (self.x,self.y-210))
    def collisione(self,uccello,uccellox,uccelloy):
        tolleranza = 5
        uccello_lato_dx = uccellox + uccello.get_width() - tolleranza
        uccello_lato_sx = uccellox + tolleranza
        tubi_lato_dx = self.x + tuboGiu.get_width()
        tubi_lato_sx = self.x
        uccello_lato_su = uccelloy + tolleranza
        uccello_lato_giu = uccelloy + uccello.get_height() - tolleranza
        tubi_lato_su = self.y + 110
        tubi_lato_giu = self.y + 210

        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()

    def fra_i_tubi(self, uccello, uccellox):
        tolleranza = 5
        uccello_lato_dx = uccellox + uccello.get_width() - tolleranza
        uccello_lato_sx = uccellox + tolleranza
        tubi_lato_dx = self.x + tuboGiu.get_width()
        tubi_lato_sx = self.x
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            return True

def inizializza():
    global uccellox, uccelloy, uccelloVely, basex
    global tubi
    global punti
    global neiTubi
    uccellox = 60
    uccelloy = 150
    uccelloVely = 0
    basex = 0
    punti = 0
    neiTubi = False
    tubi = list()
    tubi.append(Tubo())
    

def disegna_oggetti():
    SCHERMO.blit(sfondo,(0,0))
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox,uccelloy))
    SCHERMO.blit(base,(basex,400))
    puntiRender = FONT.render(str(punti), 1, (255,255,255))
    SCHERMO.blit(puntiRender, (100,0))
 
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def hai_perso():
    SCHERMO.blit(gameover, (50,180))
    aggiorna()
    #intrappoliamo il giocatore in nuovo ciclo finchè non preme SPAZIO
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()


inizializza()

while True:
    #movimento base
    basex -= VEL_AVANZ
    if basex < -45:
        basex = 0
    #GRAVITA'
    uccelloVely += 0.5
    uccelloy += uccelloVely

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            uccelloVely = -7
        
        if event.type == pygame.QUIT:
            pygame.quit()

    #aggiungo nuovo tubo alla lista
    if tubi[-1].x < 150:
        tubi.append(Tubo())
    #elimina tubi fuori schermo dalla lista
    if len(tubi) > 5:
        tubi = tubi[3:]

    #collisione uccello-tubo
    for t in tubi:
        t.collisione(uccello,uccellox,uccelloy)
    #controllo fra i tubi
    if neiTubi == False:
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox) == True:
                neiTubi = True
                break
    if neiTubi == True:
        neiTubi = False
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox) == True:
                neiTubi = True
                break
        if neiTubi == False:     #se neiTubi è FALSE -> l'uccello è uscito dai tubi
            punti += 1

    if uccelloy > 380:
        hai_perso()
    disegna_oggetti()
    aggiorna()
