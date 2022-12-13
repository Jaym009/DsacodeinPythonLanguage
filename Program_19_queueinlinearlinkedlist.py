class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
        
class Queue:
    def __init__(self):
        self.rear = self.front = None
    
    def isEmpty(self):
        return self.front == None
        
    def Enqueue(self,ele):
        temp = Node(ele)
        if self.rear == None:
            self.rear = self.front = temp
            return
        else:
            self.rear.next = temp 
            self.rear = temp
            
    def Dequeue(self):
        if self.isEmpty():
            print("Queue Empty")
            return
        else:
            temp = self.front
            self.front = temp.next
            if self.front == None:
                self.rear = None
            
    def display(self):
           p = self.front
           if p!= None:
               print(p.info)
               p = p.next
q = Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.display()
q.Dequeue()
q.display()
