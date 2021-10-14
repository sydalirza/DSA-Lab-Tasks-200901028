
check = []
check1 =[]
from collections import deque

stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        self.container.pop()
    def is_balanced(self,val):
        closed = 0
        for num in range(0,len(val)):
            if val[num] == '(':
                check.append(val[num])
            elif val[num] == '[':
                check.append(val[num])
            elif val[num] == '{':
                check.append(val[num])  
            elif val[num] == ')':
                if len(check) > 0:
                    if check[len(check)-1] == '(':
                        check.pop()
                    else:
                        check1.append(val[num])
                
            elif val[num] == ']':
                if len(check) > 0:
                    if check[len(check)-1] == '[':
                        check.pop()
                    else:
                        check1.append(val[num])
                  
            elif val[num] == '}':
                if len(check) > 0:
                    if check[len(check)-1] == '{':
                        check.pop()
                    else:
                        check1.append(val[num])
        if len(check) == 0 and len(check1) == 0:
            print('Balanced Expression')
        else:
            print('Unbalanced Expression')      


s = Stack()
s.is_balanced("[a+b]*{3+3}-(a+b)")


