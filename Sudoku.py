import random


class Sudoku:
    def __init__(self,initTable=[],shuffle=None):
        if shuffle == None:
            self.action = ['1','2','3','4','5','6','7','8','9']
        else:
            self.action = []
            for i in range(9):
                randomNum = random.randint(1,9)
                while randomNum in self.action:
                    randomNum = random.randint(1,9)
                self.action.append(randomNum)
            print(self.action)
        if initTable == []:

            self.table = []
            for i in range(9):
                newRow = []
                for x in range(9):
                    newRow.append('0')
                self.table.append(newRow)
        else:
            self.table = []
            for i in range(9):
                newRow = []
                for x in range(9):
                    newRow.append('0')
                self.table.append(newRow)
            for i in range(9):
                for x in range(9):
                    self.table[i][x] = initTable[i][x]

    def display(self):
        for i,row in enumerate(self.table):
            for x,col in enumerate(row):
                if col == '0':
                    print('| ',end='')
                else:
                    print('|'+col, end='')
            print('|')
        print()

    def insert(self,num):
        for i,row in enumerate(self.table):
            for x,col in enumerate(row):
                if col == '0':
                    self.table[i][x] = str(num)
                    return

    def isFinish(self):
        for i,row in enumerate(self.table):
            for x,col in enumerate(row):
                if col == '0':
                    return False
        return True

    def lastEmptyIndex(self):
        for i,row in enumerate(self.table):
            for x,col in enumerate(row):
                if col == '0':
                    return i,x
        return -1,-1

    def checkAction(self,row,col):
        checkCol = self.table[row]
        startRow = 0
        startCol = 0
        if (row >=0 and row < 3) and (col>=0 and col < 3):
            startRow = 0
            startCol = 0
        elif (row >=0 and row < 3) and (col>=3 and col < 6):
            startRow = 0
            startCol = 3
        elif (row >=0 and row < 3) and (col>=6 and col < 9):
            startRow = 0
            startCol = 6
        elif (row >=3 and row < 6) and (col>=0 and col < 3):
            startRow = 3
            startCol = 0
        elif (row >=3 and row < 6) and (col>=3 and col < 6):
            startRow = 3
            startCol = 3
        elif (row >=3 and row < 6) and (col>=6 and col < 9):
            startRow = 3
            startCol = 6
        elif (row >=6 and row < 9) and (col>=0 and col < 3):
            startRow = 6
            startCol = 0
        elif (row >=6 and row < 9) and (col>=3 and col < 6):
            startRow = 6
            startCol = 3
        elif (row >=6 and row < 9) and (col>=6 and col < 9):
            startRow = 6
            startCol = 6
        for i in checkCol:
            if i in self.action:
                self.action.remove(i)
        for i in self.table:
            if i[col] in self.action:
                self.action.remove(i[col])

        for r in range(3):
            for c in range(3):
                if self.table[startRow+r][startCol+c] in self.action:
                    self.action.remove(self.table[startRow+r][startCol+c])
        return self.action









