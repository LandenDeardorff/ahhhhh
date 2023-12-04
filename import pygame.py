import pygame

pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pong")

doExit = False
clock = pygame.time.Clock()

f = pygame.image.load("lllll.png")
f2 = pygame.transform.smoothscale(f,(70,70))


p1x = 20
p1y = 200
p2x = 660
p2y = 200

bx = 350
by = 250
bVx = 5
bVy = 5

p1Score = 0
p2Score = 0
#Game Loop
while not doExit:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

#Input Section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y -= 5
    if keys[pygame.K_s]:
        p1y+=5
    
    if keys[pygame.K_UP]:
        p2y -= 5
    if keys[pygame.K_DOWN]:
        p2y += 5
    
#Game Logic

    if p1y + 100 >= 500:
        p1y = 400
    if p1y <= 0:
        p1y = 0
    
    if p2y + 100 >= 500:
        p2y = 400
    if p2y <= 0:
        p2y = 0


    if bx +20 <= 0 or bx >= 650:
        bVx *= -1
    
    if by < 0 or by + 20 > 460:
        bVy *= -1
    
    if bx - 5 < p1x  and by + 60 > p1y and by < p1y + 100:
        bVx *= -1

    if bx +50  > p2x  and by + 20 > p2y and by < p2y + 100:
        bVx *= -1

    if bx +20 <= 0:
        p2Score += 1

    if bx + 50 >= 700:
        p1Score += 1

    bx+= bVx
    by+= bVy



    #render section
    screen.fill((0,0,0))
    screen.blit(f2, (bx,by))

    pygame.draw.rect(screen, (255,255,255), (p1x, p1y, 20, 100), 1)
    pygame.draw.rect(screen, (255,255,255), (p2x, p2y, 20, 100), 1)
    pygame.draw.line(screen, (255,255,255), [349,0], [349,500], 5)

    #pygame.draw.circle(screen, (255,255,255), (bx, by), 13)
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250, 10))
    text = font.render(str(p2Score) ,1, (255, 255, 255))
    screen.blit(text, (420,10))
    pygame.display.flip()



pygame.quit()