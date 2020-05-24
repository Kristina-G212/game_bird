import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Bird')  # заголовок окна

x = 50
y = 430
wight = 40
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)  # кол-во милисекунд, через которое будет обратно выполняться цикл

    # отслеживание событий  +  отслеживание единоразового нажатия на клавишу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # отслеживание событий при зажатии клавиши
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - wight - 5:
        x += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height - 5:
        y += speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 225), (x, y, wight, height))  # при запуске ничего не будет отображено на экране
    # окно нужно постоянно обновлять
    pygame.display.update()

pygame.quit()
