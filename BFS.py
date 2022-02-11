import queue as q
def BFS(start,goal):
  explored = []
  frontier = q.Queue()
  frontier.enqueue(start)
  while len(frontier) > 0:
    node = frontier.dequeue()
    for i,child in enumerate(map[node]):
      if not child in explored:
        frontier.enqueue(child)
    explored.append(node)
    if node == goal:
      return explored
