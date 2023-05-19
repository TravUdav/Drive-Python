import pygame, sys, game, menu

pygame.init()
pygame.display.set_caption("Drive")

def about():

    screenx = 640
    screeny = 443
    screen = pygame.display.set_mode([screenx, screeny])


    #изображения
    aboutt = pygame.image.load('game/aboutt.png')

    #кнопки и их подсветка
    menu1 = pygame.image.load('game/menu1.png')
    menu2 = pygame.image.load('game/menu2.png')
    exit1 = pygame.image.load('game/exit1.png')
    exit2 = pygame.image.load('game/exit2.png')

    #параметры кнопок
    shir = 215
    vis = 59

    #курсор
    (mouse_x, mouse_y) = pygame.mouse.get_pos()

    key = pygame.key.get_pressed()


    running = True
    while running:

        #фон
        screen.blit(aboutt, (0,0))
        
        #кнопки
        screen.blit(menu1, (39,363))
        screen.blit(exit1, (388,363))

        mouse = pygame.mouse.get_pos()
        # Подсветка кнопок при наведении курсора
        if (39+shir) >= mouse[0] >= 39 and (363+vis) >= mouse[1] >= 363:
             screen.blit(menu2, (39,363))
        else:
            screen.blit(menu1, (39,363))

        if (388+shir) >= mouse[0] >= 388 and (363+vis) >= mouse[1] >= 363:
             screen.blit(exit2, (388,363))
        else:
            screen.blit(exit1, (388,363))

        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Обработка нажатия кнопок
                if (39+shir) >= mouse[0] >= 39 and (363+vis) >= mouse[1] >= 363:
                    menu.menu()
                if (388+shir) >= mouse[0] >= 388 and (363+vis) >= mouse[1] >= 363:
                    pygame.quit()
                    sys.exit()

            
        

    pygame.quit()
    sys.exit()
    quit()
