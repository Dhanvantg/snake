import random
import pygame

canvas = []
n = 50

# Creating Canvas and base variables

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIN = pygame.display.set_mode((1020, 1020))
pygame.display.set_caption("Snake")
#pygame.mouse.set_visible(False)
width, height = WIN.get_size()
run = True
clock = pygame.time.Clock()


for i in range(n):
    canvas.append([0 for i in range(n)])
canvas[0][0] = 1
print(canvas)
snake = [[0,0]]
side = 'r'
food = [random.randint(1, n), random.randint(1, n)]

def move(side):
    global snake
    if side == 'l':
        if len(snake) > 1 and snake[0][0] - 1 == snake[1][0]:
            return 
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    elif side == 'r':
        if len(snake) > 1 and snake[0][0] + 1 == snake[1][0]:
            return
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    elif side == 'u':
        if len(snake) > 1 and snake[0][1] - 1 == snake[1][1]:
            return
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    elif side == 'd':
        if len(snake) > 1 and snake[0][1] + 1 == snake[1][1]:
            return
        snake.insert(0, [snake[0][0], snake[0][1] + 1])
    else:
        return
    
    if snake[0][0] < 0:
        snake[0][0] = n
    elif snake[0][0] > n:
        snake[0][0] = 0
    if snake[0][1] < 0:
        snake[0][1] = n
    elif snake[0][1] > n:
        snake[0][1] = 0
    snake.pop()

def eat():
    global food, snake
    snake.insert(0, snake[0])
    food = [random.randint(0, n), random.randint(0, n)]
    while food in snake:
        food = [random.randint(0, n), random.randint(0, n)]

pixel = width // (n+1)
frame = 0
while run:
    frame += 1
    WIN.fill((0, 0, 0))
    clock.tick(60)
    for i in snake:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(pixel*i[0], pixel*i[1], pixel, pixel))
    pygame.draw.rect(WIN, RED, pygame.Rect(pixel*food[0], pixel*food[1], pixel, pixel))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_a:
                if side != 'r':
                    side = 'l'
            elif event.key == pygame.K_s:
                if side != 'u':
                    side = 'd'
            elif event.key == pygame.K_d:
                if side != 'l':
                    side = 'r'
            elif event.key == pygame.K_w:
                if side != 'd':
                    side = 'u'
    if snake[0] == food:
        eat()
    if frame % 4 == 0:
        move(side)
        if snake[0] in snake[2:]:
            run = False
            print("GAME OVER! Score:", len(snake)-1)
    pygame.display.update()






