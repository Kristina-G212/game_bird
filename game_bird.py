import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Bird')  # заголовок окна

flyLeft = [pygame.image.load('bird_left_fly_1.png'), pygame.image.load('bird_left_fly_2.png'),
           pygame.image.load('bird_left_fly_3.png'), pygame.image.load('bird_left_fly_4.png')]

flyRight = [pygame.image.load('bird_right_fly_1.png'), pygame.image.load('bird_right_fly_2.png'),
            pygame.image.load('bird_right_fly_3.png'), pygame.image.load('bird_right_fly_4.png')]

flyUp = [pygame.image.load('bird_up_fly_1.png'), pygame.image.load('bird_up_fly_2.png'),
         pygame.image.load('bird_up_fly_3.png'), pygame.image.load('bird_up_fly_4.png')]

flyDown = [pygame.image.load('bird_down_fly_1.png'), pygame.image.load('bird_down_fly_2.png'),
           pygame.image.load('bird_down_fly_3.png'), pygame.image.load('bird_down_fly_4.png')]

birdStand = pygame.image.load('bird_front_1.png')

walkBack = [pygame.image.load('bird_back_1.png'), pygame.image.load('bird_back_2.png'),
            pygame.image.load('bird_back_3.png'), pygame.image.load('bird_back_1.png')]

walkLeft = [pygame.image.load('bird_left_1.png'), pygame.image.load('bird_left_2.png'),
            pygame.image.load('bird_left_3.png'), pygame.image.load('bird_left_1.png')]

walkRight = [pygame.image.load('bird_right_1.png'), pygame.image.load('bird_right_2.png'),
             pygame.image.load('bird_right_3.png'), pygame.image.load('bird_right_1.png')]

bg = pygame.image.load('forest(500x500).jpg')

clock = pygame.time.Clock()

x = 50
y = 400
wight = 30
height = 30
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
up = False
down = False
flyup = False
flyleft = False
flyright = False
flydown = False


animCount = 0


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 15:  # 15 fps
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    elif up:
        win.blit(walkBack[animCount // 5], (x, y))
        animCount += 1
    elif flyright:
        win.blit(flyRight[animCount // 5], (x, y))
        animCount += 1
    elif flyup:
        win.blit(flyUp[animCount // 5], (x, y))
        animCount += 1
    elif flydown:
        win.blit(flyDown[animCount // 5], (x, y))
        animCount += 1
    elif flyleft:
        win.blit(flyLeft[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(birdStand, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        up = False
        down = False
        flyup = False
        flyleft = False
        flyright = False
        flydown = False
    elif keys[pygame.K_RIGHT] and x < 500 - wight - 5:
        x += speed
        left = False
        right = True
        up = False
        down = False
        flyup = False
        flyleft = False
        flyright = False
        flydown = False
    elif keys[pygame.K_UP] and y > 370:
        y -= speed
        left = False
        right = False
        up = True
        down = False
        flyup = False
        flyleft = False
        flyright = False
        flydown = False
    elif keys[pygame.K_DOWN] and y < 500 - height - 5:
        y += speed
        left = False
        right = False
        up = False
        down = True
        flyup = False
        flyleft = False
        flyright = False
        flydown = False
    elif keys[pygame.K_d] and x < 500 - wight - 5:
        x += speed
        left = False
        right = False
        up = False
        down = False
        flyup = False
        flyleft = False
        flyright = True
        flydown = False
    elif keys[pygame.K_w] and y > 5:
        y -= speed
        left = False
        right = False
        up = False
        down = False
        flyup = True
        flyleft = False
        flyright = False
        flydown = False
    elif keys[pygame.K_s] and y < 500 - height - 5:
        y += speed
        left = False
        right = False
        up = False
        down = False
        flyup = False
        flyleft = False
        flyright = False
        flydown = True
    elif keys[pygame.K_a] and x > 5:
        x -= speed
        left = False
        right = False
        up = False
        down = False
        flyup = False
        flyleft = True
        flyright = False
        flydown = False
    else:
        animCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 4
            else:
                y -= (jumpCount ** 2) / 4
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()
