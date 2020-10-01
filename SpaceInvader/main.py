''' 
post link :- https://www.facebook.com/vtusolution/posts/923367628154366 (Shared on a my page for larger reach)
subscribed by Sumit Raj

Download the whole folder and open it as a project in Pycharm and play

'''
import pygame
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerXChange = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXChange.append(3)
    enemyYChange.append(16)

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
    # ready state means bullet is invisible and fire means bullet is moving
bulletYChange = 10
bulletState = "ready"

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 0

# Game over text
game_over_font = pygame.font.Font('freesansbold.ttf', 100)
game_overX = 200
game_overY = 250


def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(score_value, (x, y))


def game_over_text(x, y):
    game_overText = game_over_font.render("GAME OVER !!!", True, (255, 255, 255))
    screen.blit(game_overText, (game_overX, game_overY))


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def enemy(x, y, j):
    screen.blit(enemyImg[j], (x, y))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is presses check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left key pressed")
                playerXChange = -5
            if event.key == pygame.K_RIGHT:
                print("Right key pressed")
                playerXChange = 5
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    # copy the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released")
                playerXChange = 0

    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    playerX += playerXChange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyXChange[i]
        if enemyX[i] <= 0:
            enemyXChange[i] = 3
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >= 736:
            enemyXChange[i] = -3
            enemyY[i] += enemyYChange[i]

        # collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound('explosion.wav')
            explosionSound.play()
            bulletY = 480
            bulletState = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        # Game over
        if enemyY[i] >= 440:
            game_over_text(game_overX,game_overY)
            break


    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYChange

    show_score(scoreX, scoreY)

    pygame.display.update()
