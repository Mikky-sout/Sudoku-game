import Sudoku as sk
import BFS
import Stack as stack
test = [['1','2','3','4','5','6','7','8','9'],
        ['0','5','0','0','8','0','2','3','0'],
        ['0','8','0','2','3','7','0','4','0'],
        ['0','0','5','3','6','2','9','7','0'],
        ['0','7','0','0','9','0','6','5','0'],
        ['0','0','6','0','0','4','0','0','0'],
        ['0','4','0','0','0','8','3','9','0'],
        ['0','6','1','0','4','0','5','2','0'],
        ['0','0','0','0','0','0','0','0','0']]
s0 = sk.Sudoku(test)

ans = BFS.search(s0)
st = stack.Stack()
node = ans[-1]
if not node.current == None:
        st.push(node.current)
        while not node.parent == None:
                node = node.parent
                st.push(node.current)

else:
        print("Can't solve")

while len(st) > 0:
        st.pop().display()
