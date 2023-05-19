import pygame, sys
pygame.init()
# Установка заголовка окна
pygame.display.set_caption("Drive")
index = 0

#музыка
pygame.mixer.music.load('zastavka/sound.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

#иконка
pygame.display.set_icon(pygame.image.load("icon.ico"))

def zastavka():
    screen = pygame.display.set_mode([640, 443])
    clock = pygame.time.Clock()


    ## Загрузка изображений для анимации
    gif = [pygame.image.load('zastavka/zastavkadrive1.jpg'), pygame.image.load('zastavka/zastavkadrive2.jpg'),
           pygame.image.load('zastavka/zastavkadrive3.jpg'), pygame.image.load('zastavka/zastavkadrive4.jpg'),
           pygame.image.load('zastavka/zastavkadrive5.jpg'), pygame.image.load('zastavka/zastavkadrive6.jpg'),
           pygame.image.load('zastavka/zastavkadrive7.jpg'), pygame.image.load('zastavka/zastavkadrive8.jpg'),
           pygame.image.load('zastavka/zastavkadrive9.jpg'), pygame.image.load('zastavka/zastavkadrive10.jpg'),
           pygame.image.load('zastavka/zastavkadrive11.jpg'), pygame.image.load('zastavka/zastavkadrive12.jpg'),
           pygame.image.load('zastavka/zastavkadrive13.jpg'), pygame.image.load('zastavka/zastavkadrive14.jpg'),
           pygame.image.load('zastavka/zastavkadrive15.jpg'), pygame.image.load('zastavka/zastavkadrive16.jpg'),
           pygame.image.load('zastavka/zastavkadrive17.jpg'), pygame.image.load('zastavka/zastavkadrive18.jpg')]

    #анимация
    def zastavochka():
        global index
        if index == 36:
            index = 0
    # Отображение текущего изображения на экране
        screen.blit(gif[index//2], (0, 0))
        index += 1



    running = True
    while running:
        zastavochka()
        pygame.display.update()
        # Установка ограничения FPS
        clock.tick(7)
         # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                running = False
                

