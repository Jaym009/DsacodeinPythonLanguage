class Evaluation:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self,op):
        self.stack.append(op)
        
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return '$'
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return '$'
        
    def evaluateprefix(self,exp):
        for c in exp[::-1]:
            if c.isdigit():
                self.push(c)
            else:
                o1 = self.pop()
                o2 = self.pop()
                self.push(str(eval(o1+c+o2)))
                
        return int(self.pop())
    
    def centralfunc(self,ab):
        for i in ab[::-1]:
            try:
                self.push(int(i))
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()
                if i == '/':
                  self.push(val2 / val1)
                else:
                    switcher ={'+':val2 + val1, '-':val2-val1, '*':val2 * val1, '^':val2**val1}
                    self.push(switcher.get(i))
        return self.pop()

e = Evaluation()
print(e.evaluateprefix('+9*26'))
str = '+ 9 * 12 6'
strconv = str.split(' ')
print(e.centralfunc(strconv))