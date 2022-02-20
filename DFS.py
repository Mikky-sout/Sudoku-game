import Stack as st
import Sudoku as sk
class State:
  def __init__(self, current, parent):
    self.parent = parent
    self.current = current


# Recursive DFS

explored = []
def search_re(start,parent=None):
  initState = State(start,parent)
  visitedState = [x.current.table for x in explored]

  if not initState.current.table in visitedState:
    explored.append(initState)
  if start.isFinish():
    return True
  row, col = start.lastEmptyIndex()
  for i, action in enumerate(initState.current.checkAction(row, col)):
    newState = sk.Sudoku(initState.current.table)
    newState.insert(action)
    createdState = State(newState, initState)
    found = search_re(createdState.current,initState)
    if found:
      return explored



# Non-recursive DFS
def search(start):
  explored = []
  frontier = st.Stack()
  createdState = State(start, None)
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
        createdState = State(newState, node)
        frontier.push(createdState)
    explored.append(node)
    if node.current.isFinish():
      return explored
  explored.append(State(None, None))
  return explored

