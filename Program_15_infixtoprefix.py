from __future__ import print_function
import sys
class converstion:
    def __init__(self):
        self.stack=[None] * 100
        self.top=-1
    def isFull(self):
        if self.top==100:
            return True
        return False
    
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
        
    def push(self,data):
        if self.isFull():
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]=data
        
    def pop(self):
        print
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.stack[self.top]
        self.top-=1
        return d
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.stack[self.top]
        return d
    
def priority(val):
    if val=='(':
        return 0
    elif val=='+' or val=='-':
        return 1
    elif val=='*' or val=='/' or val=='%':
        return 2
    elif val=='^':
        return 3
    else:
        return 0
    
    
def infixtoprefix(val):
    prefix=[]
    s=converstion()
    n=len(val)-1
    for i in range(n,-1,-1):
        if val[i]==')':
            s.push(val[i])
        elif(val[i]=='('):
            value=s.pop()
            while(value is not ')'):
                prefix.append(value)
                value=s.pop()
        elif(val[i]=='+' or val[i]=='-' or val[i]=='*' or val[i]=='/' or val[i]=='%' or val[i]=='^'):
            while((s.isEmpty() is False)and  (priority(s.peek())> priority(val[i]))):
                prefix.append(s.pop())
            s.push(val[i])
        else:
            prefix.append(val[i])
    
    while(s.isEmpty() is not True):
        prefix.append(s.pop())
    i=0
    j=len(prefix)-1
    while(i<=j):
        temp=prefix[i]
        prefix[i]=prefix[j]
        prefix[j]=temp
        i+=1
        j-=1
    return prefix
    
c = converstion()
print("enter the infix expresion")
infix_val=input()
prefix=infixtoprefix(infix_val)
print("prefix expression:",end='')
for i in prefix:
    print(i,end="")