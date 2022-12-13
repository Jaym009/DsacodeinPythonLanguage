class Stack:
    
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self,ele):
        self.stack.append(ele)
        
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1
        
s = Stack()
while True:
    print("push")
    print("pop")
    print("peek")
    do = input("What exactly want to do it? =")
    if do == 'push':
        ele = int(input("enter element insert in to the stack :"))
        s.push(ele)
    elif do == 'pop':
        ele = s.pop()
        if ele == -1:
            print("stack is empty")
        else:
            print("Deleted element from the stack is = {0}".format(ele))
    elif do == 'peek':
        ele = s.peek()
        if ele == -1:
            print("Stack is empty")
        else:
            print("Top of the stack element is = {0}".format(ele))
    else:
        break