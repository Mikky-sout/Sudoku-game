import random

import Constant
import Sudoku as sk
import BFS
import Stack as stack
import DFS
import Textfile as tf
import Constant as ct
import pygame
from Board import Board
# s2 = sk.Sudoku(sk.randomClearTable(Textfile.randomArr(),random.randint(10,60)))
# sk.showResult(DFS.search(s2))


WIN = pygame.display.set_mode((ct.MENU_WIDTH+ct.WIDTH,ct.MENU_HEIGHT+ct.HEIGHT))
pygame.display.set_caption('SUDOKU')
currentTable = Constant.blankTable


def update(board,searchingText):
    board.draw_cubes(WIN)
    board.randomButton(WIN)
    board.fill_number(WIN, currentTable)
    startButton = board.startButton(WIN)
    board.showText(WIN, searchingText)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    showAns = False
    startButton = board.startButton(WIN)
    randomButton = board.randomButton(WIN)

    table = ct.blankTable
    # table = sk.randomClearTable(tf.randomArr(), 40)
    ans = None
    bestPathAns = None
    exploreAns = None
    currentTable = table
    searchingText = ''

    while run:
        clock.tick(ct.FPS)
        for event in pygame.event.get():

            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(pos):
                    dfs = DFS.DFS(WIN,board,clock)
                    ans = dfs.search(sk.Sudoku(table))

                    bestPathAns = sk.bestPath(ans)
                    exploreAns = sk.explore(ans)
                    board.showText(WIN, '')
                    currentTable = ans[-1].current.table
                        # showAns = True
                if randomButton.collidepoint(pos):
                    currentTable = table = sk.randomClearTable(tf.randomArr(),random.randint(10,50))

            if startButton.collidepoint(pos) or randomButton.collidepoint(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



        board.draw_cubes(WIN)
        board.randomButton(WIN)
        board.fill_number(WIN, currentTable)
        startButton = board.startButton(WIN)
        board.showText(WIN, searchingText)
        pygame.display.update()

    pygame.quit()

main()
