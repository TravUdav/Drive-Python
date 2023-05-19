import pygame, sys, zastavka

pygame.init()
zastavka.zastavka()
index2 = 0

class GameState: ##хранит состояние игры
    def __init__(self):
        self.index2 = 0


def menu():
    pygame.display.set_caption("Drive")
    screen = pygame.display.set_mode([640, 443])
    clock = pygame.time.Clock()
    game_state = GameState()
    #фон изображения
    fon = [pygame.image.load('menu/menuzas1.jpg'), pygame.image.load('menu/menuzas2.jpg'),
            pygame.image.load('menu/menuzas3.jpg'), pygame.image.load('menu/menuzas4.jpg'),
            pygame.image.load('menu/menuzas5.jpg'), pygame.image.load('menu/menuzas6.jpg'),
            pygame.image.load('menu/menuzas7.jpg'), pygame.image.load('menu/menuzas8.jpg'),
            pygame.image.load('menu/menuzas9.jpg'), pygame.image.load('menu/menuzas10.jpg'),
            pygame.image.load('menu/menuzas11.jpg'), pygame.image.load('menu/menuzas12.jpg'),
            pygame.image.load('menu/menuzas13.jpg'), pygame.image.load('menu/menuzas14.jpg'),
            pygame.image.load('menu/menuzas15.jpg'), pygame.image.load('menu/menuzas16.jpg'),
            pygame.image.load('menu/menuzas17.jpg'), pygame.image.load('menu/menuzas1.jpg')]

    #кнопки
    buttons = [pygame.image.load('menu/play1.png'),pygame.image.load('menu/help1.png'),
               pygame.image.load('menu/about1.png'),pygame.image.load('menu/exit1.png')]

    def knopki():
        y = 172
        for x in buttons:
            o = x
            screen.blit(o, [221, y])
            y += 66

    shir = 215
    vis = 59
            
    #подсветка кнопок
    play2 = pygame.image.load('menu/play2.png')
    help2 = pygame.image.load('menu/help2.png')
    about2 = pygame.image.load('menu/about2.png')
    exit2 = pygame.image.load('menu/exit2.png')

    #курсор
    (mouse_x, mouse_y) = pygame.mouse.get_pos()

    key = pygame.key.get_pressed()

    
    #анимация
    def zasmenu():
        if game_state.index2 == 36:
            game_state.index2 = 0

        screen.blit(fon[game_state.index2 // 2], (0, 0))
        game_state.index2 += 1


    running = True
    while running:
        zasmenu()
        clock.tick(7)
        knopki()


        mouse = pygame.mouse.get_pos()
        # Подсветка кнопок при наведении курсора
        if (221+shir) >= mouse[0] >= 221 and (172+vis) >= mouse[1] >= 172:
             screen.blit(play2, (221, 172))
        else:
            screen.blit(buttons[0], (221, 172))

        if (221+shir) >= mouse[0] >= 221 and (238+vis) >= mouse[1] >= 238:
             screen.blit(help2, (221, 238))
        else:
            screen.blit(buttons[1], (221, 238))

        if (221+shir) >= mouse[0] >= 221 and (304+vis) >= mouse[1] >= 304:
             screen.blit(about2, (221, 304))
        else:
            screen.blit(buttons[2], (221, 304))

        if (221+shir) >= mouse[0] >= 221 and (370+vis) >= mouse[1] >= 370:
             screen.blit(exit2, (221, 370))
        else:
            screen.blit(buttons[3], (221, 370))
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Обработка нажатия на кнопки
                if (221+shir) >= mouse[0] >= 221 and (172+vis) >= mouse[1] >= 172:
                    import game
                    game.game() #играть
                if (221+shir) >= mouse[0] >= 221 and (238+vis) >= mouse[1] >= 238:
                    import help1
                    help1.help1() #помощь
                if (221+shir) >= mouse[0] >= 221 and (304+vis) >= mouse[1] >= 304:
                    import about
                    about.about() #об игре
                if (221+shir) >= mouse[0] >= 221 and (370+vis) >= mouse[1] >= 370:
                    running = False #выход

    pygame.quit()
    sys.exit()
    quit()