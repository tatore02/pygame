from index import *
import random

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
    for s in shots:
        s.drawShot()
    for s in shotsEnemies:
        s.drawShot()

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    

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