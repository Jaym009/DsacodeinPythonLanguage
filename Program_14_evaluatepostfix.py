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
        
    def evalutepostfix(self,exp):
        for c in exp:
            if c.isdigit():
                self.push(c)
            else:
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b+c+a)))
        return int(self.pop())
    
    def centralfunc(self, ab):
        for i in ab:
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

print(e.evalutepostfix('234*6*+'))
str ='100 200 + 2 / 5 * 7 +'
strconv = str.split(' ')
print(e.centralfunc(strconv))
