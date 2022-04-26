import pygame
from Constant import WHITE,BLACK,RED,ROWS,SQUARE_SIZE,FONT_SIZE,WIDTH,HEIGHT,MENU_HEIGHT,MENU_WIDTH
class Board:
    def __init__(self):
        pygame.init()
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.menu_X_index= WIDTH+100
        self.font = pygame.font.Font(None,FONT_SIZE)
    def draw_cubes(self,win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(0, ROWS):
                pygame.draw.rect(win,BLACK,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
                if (row == 0 or row ==3 or row==6) and (col ==0 or col ==3or col==6):
                    pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE*3, SQUARE_SIZE*3), 3)

    def fill_number(self,win,table=None):
        x = 32
        y = 15
        count = 0
        step = 100
        for i in range(9):
            for n in range(9):
                if table[i][n] == '0':
                    text = self.font.render(" ", True, BLACK)
                else:
                    if table[i][n][1:] == '*':
                        text = self.font.render(table[i][n][0], True, RED)
                    else:
                        text = self.font.render(table[i][n], True, BLACK)
                textCenter = (x+(count*step), y+(step*i))
                win.blit(text, textCenter)
                count += 1
            count = 0

    def startButton(self,win):
        font = pygame.font.Font(None, 56)
        button = pygame.Rect((self.menu_X_index, 50), (300, 100))
        win.blit(font.render('SEARCH',True,BLACK),(self.menu_X_index+70, button.centery-17))
        pygame.draw.rect(win, BLACK, button,10)
        return button

    def randomButton(self,win):
        font = pygame.font.Font(None, 56)
        button = pygame.Rect((self.menu_X_index, 175), (300, 100))
        win.blit(font.render('RANDOM',True,BLACK),(self.menu_X_index+62, button.centery-17))
        pygame.draw.rect(win, BLACK, button,10)
        return button

    def resetButton(self,win):
        font = pygame.font.Font(None, 56)
        button = pygame.Rect((self.menu_X_index, 300), (300, 100))
        win.blit(font.render('RESET', True, BLACK), (self.menu_X_index + 87, button.centery - 17))
        pygame.draw.rect(win, BLACK, button, 10)
        return button

    def showText(self,win,text):
        font = pygame.font.Font(None, 26)
        win.blit(font.render(text, True, BLACK), (self.menu_X_index + 62, HEIGHT-50))

    def showLog(self,win,log):
        font = pygame.font.Font(None, 26)
        win.blit(font.render('# Allocated block : '+log, True, BLACK), (self.menu_X_index + 62, HEIGHT-100))


    def showSADetail(self,win,T,t,h):
        font = pygame.font.Font(None, 70)
        win.blit(font.render('t', True, BLACK), (self.menu_X_index-50, HEIGHT-455))
        pygame.draw.rect(win, BLACK, (self.menu_X_index, HEIGHT-470, 350, 75), 0)
        font = pygame.font.Font(None, 46)
        win.blit(font.render(str(t), True, WHITE), (self.menu_X_index+5, HEIGHT - 440))

        font = pygame.font.Font(None, 70)
        win.blit(font.render('T', True, BLACK), (self.menu_X_index - 50, HEIGHT - 355))
        pygame.draw.rect(win, BLACK, (self.menu_X_index, HEIGHT - 370, 350, 75), 0)
        font = pygame.font.Font(None, 46)
        win.blit(font.render(str(T), True, WHITE), (self.menu_X_index + 5, HEIGHT - 340))

        font = pygame.font.Font(None, 70)
        win.blit(font.render('h(x)', True, BLACK), (self.menu_X_index - 90, HEIGHT - 255))
        pygame.draw.rect(win, BLACK, (self.menu_X_index, HEIGHT - 270, 350, 75), 0)
        font = pygame.font.Font(None, 46)
        win.blit(font.render(str(h), True, WHITE), (self.menu_X_index + 5, HEIGHT - 240))
