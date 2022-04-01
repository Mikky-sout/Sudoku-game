class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if len(self.queue) == 0:
      return None
    else:
      return self.queue.pop(0)

  def first(self):
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) <= 0

  def __len__(self):
    return len(self.queue)

  def __str__(self):
    return str(self.queue)

