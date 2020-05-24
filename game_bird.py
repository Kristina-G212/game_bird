import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Bird')  # заголовок окна

x = 50
y = 50
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
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    pygame.draw.rect(win, (0, 0, 225), (x, y, wight, height))  # при запуске ничего не будет отображено на экране
    # окно нужно постоянно обновлять
    pygame.display.update()

pygame.quit()
