import pygame
from random import randrange

RES = 500
SIZE = 50
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {"W":True,"S":True,"D":True,"A":True}
lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5

pygame.init()
screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26,bold=True)
font_end = pygame.font.SysFont("Arial", 66,bold=True)
image = pygame.image.load("image.jpg").convert()

while True :
    screen.blit(image, (0,0))
    # drawing snake
    [(pygame.draw.rect(screen, pygame.Color("pink"), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color("purple"), (*apple, SIZE, SIZE))
    #show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color("white"))
    screen.blit(render_score, (5,5))
    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-lenght :]
    # eating apple
    if snake[-1] == apple :
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        score += 1
        lenght += 1
        fps += 1

    # game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1,pygame.Color("white"))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit()

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs["W"] :
        dx, dy = 0, -1
        dirs = {"W" : True, "S" :False , "D" : True, "A" : True}
    if key[pygame.K_s] and dirs["S"]:
        dx, dy = 0, 1
        dirs = {"W" : False, "S" : True, "D" : True, "A" : True}
    if key[pygame.K_a] and dirs["A"]:
        dx, dy = -1, 0
        dirs = {"W" : True, "S" : True, "D" : False, "A" : True}
    if key[pygame.K_d] and dirs["D"]:
        dx, dy = 1, 0
        dirs = {"W" : True, "S" : True, "D" : True, "A" : False}
