import Stack as st
import Sudoku as sk
import State as state
from Constant import FPS
import pygame
class DFS:
# Recursive DFS
  def __init__(self,win,board,clock):
    self.explored = []
    self.win = win
    self.board = board
    self.clock = clock
  def search_re(self,start,parent=None):
    flag = 0

    if self.explored == []:
      flag = 1
    initState = st.State(start,parent)
    visitedState = [x.current.table for x in self.explored]
    if not initState.current.table in visitedState:
      self.explored.append(initState)
    if start.isFinish():
      return True
    row, col = start.lastEmptyIndex()
    for i, action in enumerate(initState.current.checkAction(row, col)):
      newState = sk.Sudoku(initState.current.table)
      newState.insert(action)
      createdState = st.State(newState, initState)
      found = self.search_re(createdState.current,initState)
      if found:
        return self.explored
    if flag == 1:
      return self.explored


  # Non-recursive DFS
  def search(self,start):
    explored = []
    frontier = st.Stack()
    createdState = state.State(start, None)
    frontier.push(createdState)
    while len(frontier) > 0:
      node = frontier.pop()
      row, col = node.current.lastEmptyIndex()
      if not row == -1 and not col == -1:
        for i, action in enumerate(node.current.checkAction(row, col)):
          newState = sk.Sudoku(node.current.table)
          newState.insert(action)
          for x in explored:
            if x.current.table == newState.table:
              continue
          createdState = state.State(newState, node)
          frontier.push(createdState)
      explored.append(node)
      if node.current.isFinish():
        return explored
      self.update(node.current.table)
    explored.append(state.State(None, None))
    return explored


  def update(self,updateTable):
    self.clock.tick(FPS)
    self.board.draw_cubes(self.win)
    self.board.randomButton(self.win)
    self.board.fill_number(self.win, updateTable)
    startButton = self.board.startButton(self.win)
    self.board.showText(self.win, 'Searching...')
    pygame.display.update()

