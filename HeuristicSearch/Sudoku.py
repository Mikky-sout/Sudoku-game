import random
import Textfile as txt
import numpy as np

class Sudoku:
    def __init__(self,initTable=[],action=None):
        if action == None:
            self.action = ['1','2','3','4','5','6','7','8','9']
        else:
            self.action = action
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
        for i, row in enumerate(self.table):
            for x, col in enumerate(row):
                if col == '0':
                    print('|   ', end='')
                else:
                    if not col[1:] == "*":

                        print('| ' + col + ' ', end='')
                    else:
                        print('| ' + col, end='')
            print('|')
        print()

    def displayFrom(self,table):
        for i, row in enumerate(table):
            for x, col in enumerate(row):
                if col == '0':
                    print('|   ', end='')
                else:
                    if not col[1:] == "*":

                        print('| ' + col + ' ', end='')
                    else:
                        print('| ' + col, end='')
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

    def isValidate(self):
        for i,row in enumerate(self.table):
            leftAction = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for n,col in enumerate(row):
                if col in leftAction:
                    leftAction.remove(col)
            if len(leftAction) > 0:
                return False
        return True

    def checkAction(self,row,col):
        action = ['1','2','3','4','5','6','7','8','9']
        checkCol = self.table[row]
        startRow,startCol = self.findBlock(row,col)
        for i in checkCol:
            if i in action:
                action.remove(str(i))
        for i in self.table:
            if i[col] in action:
                action.remove(str(i[col]))

        for r in range(3):
            for c in range(3):
                if str(self.table[startRow+r][startCol+c]) in action:
                    action.remove(str(self.table[startRow+r][startCol+c]))
        return action

    def find2Error(self):
        error = []
        for x,row in enumerate(self.table):
            default = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            found = []
            for y, col in enumerate(row):
                found.append(int(col[0:1]))
            found.sort()
            if not found == default:
                error.append(['r',x])

        for y,col in enumerate(self.table):
            default = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            found = []
            for x, row in enumerate(col):
                found.append(int(self.table[x][y][0:1]))
            found.sort()
            if not found == default:
                error.append(['c', y])
        return error

    def filp(self,block):
        # block = random.randint(1,9)
        posToFilp = self.findPosEmptyBlock(self.table, block)
        # print(posToFilp)
        if len(posToFilp) < 2:
            # block = random.randint(1, 9)
            return np.copy(self.table)
        n1 = random.choice(posToFilp)
        n2 = random.choice(posToFilp)
        while n1 == n2:
            n2 = random.choice(posToFilp)
        tempTable = np.copy(self.table)
        # posToFlip = self.findPosEmpty()
        # print('Filp',n1,n2)
        tempTable[n1[0]][n1[1]],tempTable[n2[0]][n2[1]] = tempTable[n2[0]][n2[1]],tempTable[n1[0]][n1[1]]
        return tempTable


    # def filpAll(self):
    #     tempTable = np.copy(self.table)
    #     posToFlip = self.findPosEmpty()
    #
    #     for i in posToFlip:
    #         for n in posToFlip:
    #             if not i == n:
    #                 tempTable[i[0]][i[1]], tempTable[n[0]][n[1]] = tempTable[n[0]][n[1]], tempTable[i[0]][i[1]]
    #                 if calCost(tempTable) < 2:
    #                     return tempTable
    #                 tempTable = np.copy(self.table)
    #     return None

    def findPosEmpty(self):
        posEmp = []
        for row in range(9):
            for col in range(9):
                if self.table[row][col][1:] == "*":
                    posEmp.append([row,col])

        return posEmp

    def findPosEmptyBlock(self,table,block):
        posEmp = []
        startRow, startCol = self.findBlock(10, 10, block)
        for row in range(3):
            for col in range(3):
                if table[row+startRow][col+startCol][1:] == "*":
                    posEmp.append([row+startRow,col+startCol])
        return posEmp


    def findBlock(self,row,col,nBlock=0):
        startRow = 0
        startCol = 0
        if ((row >=0 and row < 3) and (col>=0 and col < 3)) or nBlock == 1:
            startRow = 0
            startCol = 0
        elif ((row >=0 and row < 3) and (col>=3 and col < 6)) or nBlock == 2:
            startRow = 0
            startCol = 3
        elif ((row >=0 and row < 3) and (col>=6 and col < 9)) or nBlock == 3:
            startRow = 0
            startCol = 6
        elif ((row >=3 and row < 6) and (col>=0 and col < 3)) or nBlock == 4:
            startRow = 3
            startCol = 0
        elif ((row >=3 and row < 6) and (col>=3 and col < 6)) or nBlock == 5:
            startRow = 3
            startCol = 3
        elif ((row >=3 and row < 6) and (col>=6 and col < 9)) or nBlock == 6:
            startRow = 3
            startCol = 6
        elif ((row >=6 and row < 9) and (col>=0 and col < 3)) or nBlock == 7:
            startRow = 6
            startCol = 0
        elif ((row >=6 and row < 9) and (col>=3 and col < 6)) or nBlock == 8:
            startRow = 6
            startCol = 3
        elif ((row >=6 and row < 9) and (col>=6 and col < 9)) or nBlock == 9:
            startRow = 6
            startCol = 6
        return startRow,startCol

    def fillRandomly(self):
        self.clear()
        for n in range(9):
            startRow,startCol = self.findBlock(10,10,n+1)
            action = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for r in range(3):
                for c in range(3):
                    if str(self.table[startRow + r][startCol + c]) in action:
                        action.remove(str(self.table[startRow + r][startCol + c]))
            for i in range(len(action)):
                for r in range(3):
                    for c in range(3):
                        if str(self.table[startRow + r][startCol + c]) == '0':
                            ranNum = random.choice(action)
                            action.remove(ranNum)
                            self.table[startRow + r][startCol + c] = ranNum+'*'

    def fillRandomlyWithBlock(self,block):
        tempTable = np.copy(self.table)
        tempTable = self.clearTableWihtBlock(tempTable,block)
        startRow,startCol = self.findBlock(10,10,block)
        action = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for r in range(3):
            for c in range(3):
                if str(tempTable[startRow + r][startCol + c]) in action:
                    action.remove(str(tempTable[startRow + r][startCol + c]))
        random.shuffle(action)
        for r in range(3):
            for c in range(3):
                if str(tempTable[startRow + r][startCol + c]) == '0':
                    num=action.pop(0)
                    tempTable[startRow + r][startCol + c] = num+'*'
        return tempTable

    def clear(self):
        for row in range(9):
            for col in range(9):
                if self.table[row][col][1:] == "*":
                    self.table[row][col] = "0"

    def clearTableWihtBlock(self,table,block):
        tempTable = np.copy(table)
        startRow, startCol = self.findBlock(10, 10, block)
        for row in range(3):
            for col in range(3):
                if tempTable[row+startRow][startCol+col][1:] == "*":
                    tempTable[row+startRow][startCol+col] = "0"
        return tempTable

    def calCost(self):
        cost = 0
        for row in range(9):
            foundList = []
            for col in range(9):
                if self.table[row][col][1:] == "*" and self.table[row][col][0:1] not in foundList:
                    cost += int(self.calCostRow(self.table[row],self.table[row][col][0:1],col))
                    foundList.append(self.table[row][col][0:1])
        for col in range(9):
            foundList = []
            for row in range(9):
                if self.table[row][col][1:] == "*" and self.table[row][col][0:1] not in foundList:
                    cost += int(self.calCostRow(self.getCol(col),self.table[row][col][0:1],row))
                    foundList.append(self.table[row][col][0:1])
        return cost


    def getCol(self,col):
        l = []
        for row in range(9):
            l.append(self.table[row][col])
        return l


    def calCostRow(self,checkList,num,col):
        count = 0
        for i,val in enumerate(checkList):
            if (str(val[0:1])[0:1] == str(num)) and not (i == col):
                count+=1
        return count




def randomClearTable(table,clearNum=30):
    newTable = []
    for i in range(9):
        newRow = []
        for x in range(9):
            newRow.append('0')
        newTable.append(newRow)
    for i in range(9):
        for x in range(9):
            newTable[i][x] = table[i][x]

    if clearNum > 81:
        clearNum = 81
    while clearNum > 0:
        row = random.randint(0,8)
        col = random.randint(0,8)
        if newTable[row][col]=="0":
            continue
        newTable[row][col] = "0"
        clearNum-=1
    return newTable

def calCost(table):
    cost = 0
    for row in range(9):
        foundList = []
        for col in range(9):
            if table[row][col][1:] == "*" and table[row][col][0:1] not in foundList:
                cost += int(calCostRow(table[row],table[row][col][0:1],col))
                foundList.append(table[row][col][0:1])
    for col in range(9):
        foundList = []
        for row in range(9):
            if table[row][col][1:] == "*" and table[row][col][0:1] not in foundList:
                cost += int(calCostRow(getCol(col,table),table[row][col][0:1],row))
                foundList.append(table[row][col][0:1])
    return cost

def getCol(col,table):
    l = []
    for row in range(9):
        l.append(table[row][col])
    return l

def calCostRow(checkList,num,col):
    count = 0
    for i,val in enumerate(checkList):
        if (str(val[0:1])[0:1] == str(num)) and not (i == col):
            count+=1
    return count













