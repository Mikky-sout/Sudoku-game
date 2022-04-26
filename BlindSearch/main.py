import random
import Constant
import Sudoku as sk
import BFS
import DFS
import Textfile as tf
import Constant as ct
import pygame
from Board import Board

WIN = pygame.display.set_mode((ct.MENU_WIDTH+ct.WIDTH,ct.MENU_HEIGHT+ct.HEIGHT))
pygame.display.set_caption('YESEO')
currentTable = Constant.blankTable

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    startButton = board.startButton(WIN)
    randomButton = board.randomButton(WIN)
    resetButton = board.resetButton(WIN)
    isDFS = True
    table = ct.blankTable
    fps = 10
    isSlow = True

    # ans = None
    # bestPathAns = None
    # exploreAns = None
    currentTable = table
    searchingText = ''
    log = ""
    size = 0
    dfsChoice = board.dfsChoice(WIN,isDFS)
    bfsChoice = board.bfsChoice(WIN,isDFS)
    slowChoice = board.slowChoice(WIN,isSlow)
    fastChoice = board.fastChoice(WIN,isSlow)
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
                    if isDFS:

                        dfs = DFS.DFS(WIN,board,clock,isDFS,fps,isSlow)
                        ans,time,log = dfs.search(sk.Sudoku(table))
                        size = len(ans)
                        print(time,log,len(ans))
                    else:
                        bfs = BFS.BFS(WIN, board, clock, isDFS,fps,isSlow)
                        ans,time,log = bfs.search(sk.Sudoku(table))
                        size = len(ans)
                    bestPathAns = sk.bestPath(ans)
                    # exploreAns = sk.explore(ans)
                    if ans[-1].current == None:
                        currentTable = table
                        searchingText = "Can't solve!!! (%.4f sec)"%time
                    else:
                        currentTable = ans[-1].current.table
                        searchingText ='Solve within %.4f sec'%time

                if randomButton.collidepoint(pos) and allowClick:
                    searchingText = ""
                    currentTable = table = sk.randomClearTable(tf.randomArr(),random.randint(30,30))
                    size = 0
                    log=''

                if resetButton.collidepoint(pos) and allowClick:
                    searchingText = ""
                    currentTable = table
                    size = 0
                    log = ''

                if dfsChoice.collidepoint(pos):
                    if not isDFS:
                        isDFS = True
                if bfsChoice.collidepoint(pos):
                    if isDFS:
                        isDFS = False

                if slowChoice.collidepoint(pos):
                    if not isSlow:
                        isSlow = True
                        fps = 10
                if fastChoice.collidepoint(pos):
                    if isSlow:
                        isSlow = False
                        fps = 120

            if startButton.collidepoint(pos) or randomButton.collidepoint(pos) or dfsChoice.collidepoint(pos) or bfsChoice.collidepoint(pos) or resetButton.collidepoint(pos) or slowChoice.collidepoint(pos) or fastChoice.collidepoint(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        board.draw_cubes(WIN)
        board.randomButton(WIN)
        board.fill_number(WIN, currentTable)
        startButton = board.startButton(WIN)
        resetButton = board.resetButton(WIN)
        board.showText(WIN, searchingText)
        dfsChoice=board.dfsChoice(WIN,isDFS)
        bfsChoice=board.bfsChoice(WIN,isDFS)
        slowChoice=board.slowChoice(WIN,isSlow)
        fastChoice=board.fastChoice(WIN,isSlow)
        if not (log == '' or size == 0):
            board.showLog(WIN, log,size)
        pygame.display.update()
    pygame.quit()

main()
