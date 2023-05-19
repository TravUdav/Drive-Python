import pygame, sys, game, menu

pygame.init()
pygame.display.set_caption("Drive")

def over(score):
    screenx = 640
    screeny = 443
    screen = pygame.display.set_mode([screenx, screeny])
    # Загрузка шрифта
    fontgame = pygame.font.Font('Thintel.ttf', 48)

    #изображения
    gameover = pygame.image.load('game/gameover.png')

    #кнопки и их подсветка
    retry1 = pygame.image.load('game/retry1.png')
    retry2 = pygame.image.load('game/retry2.png') 
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
        screen.blit(gameover, (0,0))

        #результат
        ##score_over = fontgame.render(str(game.score//10),1,(255,255,255))
        score_over = fontgame.render(str(score), 1, (255, 255, 255))
        screen.blit(score_over,(299,352))
        
        #кнопки
        screen.blit(retry1, (87,199))
        screen.blit(menu1, (335,199))
        screen.blit(exit1, (212,277))
        # Получение позиции курсора
        mouse = pygame.mouse.get_pos()
        # Подсветка кнопок при наведении курсора
        if (87+shir) >= mouse[0] >= 87 and (199+vis) >= mouse[1] >= 199:
             screen.blit(retry2, (87,199))
        else:
            screen.blit(retry1, (87,199))

        if (335+shir) >= mouse[0] >= 335 and (199+vis) >= mouse[1] >= 199:
             screen.blit(menu2, (335,199))
        else:
            screen.blit(menu1, (335,199))

        if (212+shir) >= mouse[0] >= 212 and (277+vis) >= mouse[1] >= 277:
             screen.blit(exit2, (212,277))
        else:
            screen.blit(exit1, (212,277))

        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Обработка нажатия на кнопки
                if (87+shir) >= mouse[0] >= 87 and (199+vis) >= mouse[1] >= 199:
                    game.score = 0
                    game.game()
                if (335+shir) >= mouse[0] >= 335 and (199+vis) >= mouse[1] >= 199:
                    menu.menu()
                if (212+shir) >= mouse[0] >= 212 and (277+vis) >= mouse[1] >= 277:
                    pygame.quit()
                    sys.exit()
            


    pygame.quit()
    sys.exit()
    quit()
