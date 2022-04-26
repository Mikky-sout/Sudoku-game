import random
import Constant
import Sudoku as sk
import SimulatedAnnealing
import Textfile as tf
import Constant as ct
import pygame
from Board import Board

WIN = pygame.display.set_mode((ct.MENU_WIDTH+ct.WIDTH,ct.MENU_HEIGHT+ct.HEIGHT))
pygame.display.set_caption('MARSHIRO')
currentTable = Constant.blankTable

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    startButton = board.startButton(WIN)
    randomButton = board.randomButton(WIN)
    resetButton = board.resetButton(WIN)

    table = ct.blankTable
    fps = 300
    currentTable = table
    searchingText = ''
    log = ""
    t=0
    T=0
    h=0

    while run:
        allowClick = True
        clock.tick(fps)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(pos) and allowClick:
                    allowClick = False

                    sa = SimulatedAnnealing.SimulatedAnnealing(WIN, board, clock)
                    ans, time, log, T , t, h = sa.search(sk.Sudoku(table))
                    currentTable = ans.table
                    searchingText = 'Solve within %.4f sec' % time

                if randomButton.collidepoint(pos) and allowClick:
                    searchingText = ""
                    currentTable = table = sk.randomClearTable(tf.randomArr(), random.randint(25, 25))
                    log = ''

                if resetButton.collidepoint(pos) and allowClick:
                    searchingText = ""
                    currentTable = table
                    log = ''

            if startButton.collidepoint(pos) or randomButton.collidepoint(pos) or resetButton.collidepoint(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        board.draw_cubes(WIN)
        board.randomButton(WIN)
        board.fill_number(WIN, currentTable)
        startButton = board.startButton(WIN)
        resetButton = board.resetButton(WIN)
        board.showText(WIN, searchingText)
        board.showSADetail(WIN,T,t,h)
        if not (log == ''):
            board.showLog(WIN, log)
        pygame.display.update()
    pygame.quit()


    #
    # for i in range(100000):
    #     sudoku.fillRandomly()
    #
    #     if sudoku.calCost() <2:
    #
    #         sudoku.display()
    #         print(sudoku.calCost())




main()
