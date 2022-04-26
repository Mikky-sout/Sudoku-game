import Sudoku as sk
import pygame
import time
import tracemalloc
import math

import numpy as np
class SimulatedAnnealing:

  def __init__(self,win,board,clock):
    self.TMax = 0
    self.blockStart = 1
    self.blockEnd = 10
    self.currentCost = 100
    self.increase = 1
    self.explored = []
    self.win = win
    self.board = board
    self.clock = clock
    self.fps = 300

  def update(self,updateTable,T,t,h):
    self.clock.tick(self.fps)
    self.board.draw_cubes(self.win)
    self.board.randomButton(self.win)
    self.board.fill_number(self.win, updateTable)
    self.board.startButton(self.win)
    self.board.resetButton(self.win)
    self.board.showText(self.win, 'Searching...')
    self.board.showSADetail(self.win,T,t,h)
    pygame.display.update()

  def schedhle(self,time):
    if time == 0:
      return self.TMax
    return self.TMax * math.pow(0.98,time)


  def search(self,start,TMax=1000):
    time_start = time.perf_counter()
    self.TMax = TMax
    tracemalloc.start()
    current = start
    current.fillRandomly()
    t = 0
    block = self.blockStart
    while True:
      T = self.schedhle(t)
      h = current.calCost()

      if h == 0 or t == 1000 or T == 0:
        mem = tracemalloc.get_tracemalloc_memory()
        tracemalloc.stop()
        time_end = time.perf_counter()
        return  current,time_end-time_start,str(mem),T,t,h

      nextState = sk.Sudoku(current.filp(block))
      E = nextState.calCost() - h
      pos = np.exp(-E / T)
      if np.random.uniform(1, 0, 1) < pos or nextState.calCost() < h:
        current = sk.Sudoku(nextState.table)


      t+=1
      block+=self.increase
      newH = current.calCost()
      if newH <= 12 and not newH == 0:
        error = current.find2Error()
        self.blockStart,self.blockEnd,self.increase = self.findSearchLimit(error)
      self.update(current.table,T,t,newH)
      if block >= self.blockEnd+1:
        block = self.blockStart
      # current.display()


  def findSearchLimit(self,error):
    if error[0][0] == 'r':
      if 0 <= error[0][1] < 3:
        return 1,3,1
      elif 3 <= error[0][1] < 6:
        return 4,6,1
      elif 6 <= error[0][1] < 9:
        return 7,9,1
    elif error[0][0] == 'c':
      if 0 <= error[0][1] < 3:
        return 1,7,3
      elif 3 <= error[0][1] < 6:
        return 2,8,3
      elif 6 <= error[0][1] < 9:
        return 3,9,3







