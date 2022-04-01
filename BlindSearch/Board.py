import pygame
from Constant import WHITE,BLACK,ROWS,SQUARE_SIZE,FONT_SIZE,WIDTH,HEIGHT,MENU_HEIGHT,MENU_WIDTH
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

    def showLog(self,win,log,size):
        font = pygame.font.Font(None, 26)
        win.blit(font.render('# Allocated block : '+log, True, BLACK), (self.menu_X_index + 62, HEIGHT-150))
        win.blit(font.render('# Explored : ' + str(size), True, BLACK), (self.menu_X_index + 62, HEIGHT - 100))

    def dfsChoice(self,win,isDFS):
        font = pygame.font.Font(None, 46)
        win.blit(font.render('DFS', True, BLACK), (self.menu_X_index + 60, 445))
        if isDFS:
            choiceDFS = pygame.Rect((self.menu_X_index , 435), (50, 50))
            pygame.draw.rect(win, BLACK, choiceDFS)
        else:
            choiceDFS = pygame.Rect((self.menu_X_index, 435), (50, 50))
            pygame.draw.rect(win, BLACK, choiceDFS, 8)
        return choiceDFS

    def bfsChoice(self,win,isDFS):
        font = pygame.font.Font(None, 46)
        win.blit(font.render('BFS', True, BLACK), (self.menu_X_index + 185 + 55, 445))
        if not isDFS:
            choiceBFS = pygame.Rect((self.menu_X_index + 180, 435), (50, 50))
            pygame.draw.rect(win, BLACK, choiceBFS)
        else:
            choiceBFS = pygame.Rect((self.menu_X_index + 180, 435), (50, 50))
            pygame.draw.rect(win, BLACK, choiceBFS, 8)
        return choiceBFS

    def slowChoice(self,win,isSlow):
        font = pygame.font.Font(None, 46)
        win.blit(font.render('SLOW', True, BLACK), (self.menu_X_index + 60, 520))
        if isSlow:
            choiceSlow = pygame.Rect((self.menu_X_index ,510), (50, 50))
            pygame.draw.rect(win, BLACK, choiceSlow)
        else:
            choiceSlow = pygame.Rect((self.menu_X_index,510), (50, 50))
            pygame.draw.rect(win, BLACK, choiceSlow, 8)
        return choiceSlow

    def fastChoice(self,win,isSlow):
        font = pygame.font.Font(None, 46)
        win.blit(font.render('FAST', True, BLACK), (self.menu_X_index + 185 + 55, 520))
        if not isSlow:
            choiceFast = pygame.Rect((self.menu_X_index + 180, 510), (50, 50))
            pygame.draw.rect(win, BLACK, choiceFast)
        else:
            choiceFast = pygame.Rect((self.menu_X_index + 180, 510), (50, 50))
            pygame.draw.rect(win, BLACK, choiceFast, 8)
        return choiceFast
