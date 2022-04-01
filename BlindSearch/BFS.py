import queue as q
import Sudoku as sk
import State as state
import pygame
import time
import tracemalloc
class BFS:
  def __init__(self, win, board, clock, isDFS,fps,isSlow):
    self.explored = []
    self.win = win
    self.board = board
    self.clock = clock
    self.isDfs = isDFS
    self.fps = fps
    self.isSlow = isSlow

  def search(self,start):
    tracemalloc.start()
    time_start = time.perf_counter()
    explored = []
    frontier = q.Queue()
    createdState = state.State(start, None)
    frontier.enqueue(createdState)
    while len(frontier) > 0:
      node = frontier.dequeue()
      row, col = node.current.lastEmptyIndex()
      if not row == -1 and not col == -1:
        for i, action in enumerate(node.current.checkAction(row, col)):
          newState = sk.Sudoku(node.current.table)
          newState.insert(action)
          exploredList = [x for x in explored]
          if not newState in exploredList:
            createdState = state.State(newState, node)
            frontier.enqueue(createdState)
      explored.append(node)
      if node.current.isFinish() and node.current.isValidate():
        time_end = time.perf_counter()
        mem = tracemalloc.get_tracemalloc_memory()
        tracemalloc.stop()
        return explored,time_end-time_start,str(mem)
      self.update(node.current.table)
    explored.append(state.State(None,None))
    time_end = time.perf_counter()
    mem = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    return explored,time_end-time_start,str(mem)

  def update(self,updateTable):
    self.clock.tick(self.fps)
    self.board.draw_cubes(self.win)
    self.board.randomButton(self.win)
    self.board.fill_number(self.win, updateTable)
    self.board.startButton(self.win)
    self.board.resetButton(self.win)
    self.board.showText(self.win, 'Searching...')
    self.board.dfsChoice(self.win, self.isDfs)
    self.board.bfsChoice(self.win, self.isDfs)
    self.board.slowChoice(self.win, self.isSlow)
    self.board.fastChoice(self.win, self.isSlow)
    pygame.display.update()
