import pygame, time, random, math, sys, menu, over

pygame.init()
pygame.display.set_caption("Drive")

import pygame, time, random, math, sys, menu, over

pygame.init()
pygame.display.set_caption("Drive")


def game():
    
    score = 0
    screenx = 640
    screeny = 443
    screen = pygame.display.set_mode([screenx, screeny]) # Создание игрового окна

    roady = 0 # Позиция дороги по вертикали
    roadyo = -443 # Дополнительная позиция дороги по вертикали
    position = 340 # Позиция автомобиля по горизонтали

    clock = pygame.time.Clock() # Создание объекта для отслеживания времени
    fpsuvel = 0
    fps = 30

    #звуки
    musicover = pygame.mixer.Sound('game/over.wav')
    stolknovenie = pygame.mixer.Sound('game/stolknovenie.wav')
    
    #все изображения
    clock = pygame.time.Clock()
    road = pygame.image.load('game/roadd.jpg')
    car1 = pygame.image.load('game/car1.png')
    car2 = pygame.image.load('game/car2.png')
    car3 = pygame.image.load('game/car3.png')
    car4 = pygame.image.load('game/car4.png')
    car5 = pygame.image.load('game/car5.png')
    car6 = pygame.image.load('game/car6.png')
    car7 = pygame.image.load('game/car7.png')
    car8 = pygame.image.load('game/car8.png')
    car9 = pygame.image.load('game/car9.png')
    heart = pygame.image.load('game/heart.png')
    gameover = pygame.image.load('game/gameover.png')

    #шрифт
    fontgame = pygame.font.Font('Thintel.ttf', 48)


    hearts = [heart, heart, heart] # Инициализация жизней
    cars = [car2,car3,car4,car5,car6,car7,car8,car9]
    random_car = random.choice(cars)
    mesto = [340, 255] # Доступные позиции по горизонтали для других автомобилей
    random_mesto = random.choice(mesto)
    shir = 61 # Ширина другого автомобиля
    vis = 115 # Высота другого автомобиля
    y = -115 # Позиция другого автомобиля по вертикали
    dy = random.randint(13,17) # Скорость другого автомобиля

    i = 3

    def hearts2():
        # Отображение жизней в верхнем левом углу
        x = 14
        for i in hearts:
            screen.blit(i, [x, 24])
            x += 45


    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if position == 255:
                        position = 340
                if event.key == pygame.K_LEFT:
                    if position == 340:
                        position = 255
                if event.key == pygame.K_d:
                    if position == 255:
                        position = 340
                if event.key == pygame.K_a:
                    if position == 340:
                        position = 255
                if event.key == pygame.K_ESCAPE:
                    score = 0
                    menu.menu()

        roady += 7 # Перемещение дороги вниз
        if roady > 443:
            roady = 0
            roadyo = -443
        if roady > 0:
            screen.blit(road, (0, roady))
            roadyo += 7
            screen.blit(road, (0, roadyo))

        screen.blit(car1,(position,317)) # Отображение игрового автомобиля

        hearts2()  # Отображение жизней
 

        screen.blit(random_car, (random_mesto, y)) # Отображение другого автомобиля
        y = y+dy # Перемещение другого автомобиля по вертикали
        if y > 443:
            y = -115
            dy = random.randint(13,17)
            random_car = random.choice(cars)
            random_mesto = random.choice(mesto)
            screen.blit(random_car, (random_mesto, y))
            y = y+dy


        if position == random_mesto and y > 207:
            y = 444
            hearts.remove(heart)
            stolknovenie.play()
        if len(hearts) <= 0 :
            musicover.play() # Воспроизведение звука завершения игры
            over.over(score // 10) # Переход на экран завершения игры

        score += 0.3
        scorevalue = fontgame.render("Score: "+str(score//10),1,(255,255,255)) # Отображение счета
        screen.blit(scorevalue,(451,10))
        pygame.display.update()
        fpsuvel += 1
        if fpsuvel%100 == 0:
            fps += 1 
        clock.tick(fps)
    pygame.quit()
    sys.exit()
    quit()