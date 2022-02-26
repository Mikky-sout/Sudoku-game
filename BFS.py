import queue as q
import Sudoku as sk
import Board as board
class State:
  def __init__(self, current, parent):
    self.parent = parent
    self.current = current


class BFS:
  def __init__(self,win):
    self.win=win
  def search(start):

    explored = []
    frontier = q.Queue()
    createdState = State(start, None)
    frontier.enqueue(createdState)
    while len(frontier) > 0:
      node = frontier.dequeue()
      row, col = node.current.lastEmptyIndex()
      if not row == -1 and not col == -1:
        for i, action in enumerate(node.current.checkAction(row, col)):
          newState = sk.Sudoku(node.current.table)
          newState.insert(action)
          for x in explored:
            if x.current.table == newState.table:
              continue
          createdState = State(newState, node)
          frontier.enqueue(createdState)
      explored.append(node)
      if node.current.isFinish():
        return explored
    explored.append(State(None,None))
    return explored
