import random
def array2str(arr):
    s = ""
    for row in range(9):
        for col in range(9):
            s += arr[row][col]
    s+="\n"
    return s

def readFile():
    file = open("sudoku_ans.txt","r")

    listS = []
    for i in file:
        if not i[:-2] == "":
            listS.append(i[:-1])
    return listS

def isDuplicate(s):
    arr = readFile()
    if s[:-1] in arr:
        return True
    return False

def write(arr):
    s = array2str(arr)
    if not isDuplicate(s):
        file = open("sudoku_ans.txt", "a")
        file.write(s)
        file.close()

def str2arr(s):
    arr = [['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0']]
    count = 0
    for i in range(9):
        for x in range(9):
            arr[i][x] = s[count]
            count +=1
    return arr

def randomArr():
    listS = readFile()
    s = listS[random.randint(0, len(listS)-1)]
    arr = str2arr(s)
    return arr