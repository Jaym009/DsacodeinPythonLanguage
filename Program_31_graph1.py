class Node:
    def __init__(self, v):
        self.vertex = v
        self.next = None
        
class Graph:
    def __init__(self, size):
        self.V = size
        self.graph = [None]*size
        
    def add_edge(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node
        
        node  = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node
    
    def print_graph(self):
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                print(temp.vertex)
                temp = temp.next
            print("\n")
            
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()