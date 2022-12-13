class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
        
class CircularQueue:
    def __init__(self):
        self.front = self.rear = None
        
    def enqueue(self,ele):
        temp = Node(ele)
        if self.front == None:
            self.rear = self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.rear.next = self.front
        
    def dequeue(self):
        if self.front == None:
            print("Queue Empty")
            return -1
        temp = self.front
        if self.front==self.rear:
            self.front = self.rear = None
        else:
            self.front = temp.next
            self.rear.next = self.front
        return temp.info
    
    def display(self):
        current = self.front
        while current.next != self.front:
            print(current.info)
            current = current.next
        print(current.info)
        
c = CircularQueue()
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.display()
print("******")
val = c.dequeue()
if val == -1:
    print("Queue is alreadt empty")
else:
    print("Deleted element from the queue is = {}".format(val))
c.display()
            