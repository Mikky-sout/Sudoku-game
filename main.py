import Sudoku as sk
import BFS
import Stack as stack
import DFS
test = [['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0']]


s0 = sk.Sudoku(test,True)
# |1|2|3|4|5|6|7|8|9|
# |7|5|4|1|8|9|2|3|6|
# |6|8|9|2|3|7|1|4|5|
# |8|1|5|3|6|2|9|7|4|
# |4|7|2|8|9|1|6|5|3|
# |3|9|6|5|7|4|8|1|2|
# |5|4|7|6|2|8|3|9|1|
# |9|6|1|7|4|3|5|2|8|
# |2|3|8|9|1|5|4|6|7|
# ans1 = BFS.search(s0)
# node = ans1[-1]

ans2 = DFS.search_re(s0)

node = ans2[-1]

# for x in ans2:
#         if x.current.isFinish():
#                 ans2 = x
# st = stack.Stack()
# node = ans2
# node.current.display()
# ans2.current.display()





#
st = stack.Stack()

if not node.current == None:
        st.push(node.current)
        while not node.parent == None:
                node = node.parent
                st.push(node.current)
else:
        print("Can't solve")
print('Num',len(st))
while len(st) > 0:
        st.pop().display()


