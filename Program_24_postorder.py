class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def buildbst(self, root, ele):
        if root == None:
            return Node(ele)
        if ele<root.data:
            root.left = self.buildbst(root.left, ele)
        else:
            root.right = self.buildbst(root.right, ele)
        return root
    
    def postorder(self, root):
        if root is None:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
        
    def iterativepostorder(self, root):
        if root is None:
            return
        recursiveStack, resultStack = [], []
        recursiveStack.append(root)
        while recursiveStack:
            current = recursiveStack.pop()
            resultStack.append(current)
            if current.left:
                recursiveStack.append(current.left)
            if current.right:
                recursiveStack.append(current.right)
        while resultStack:
            current = resultStack.pop()
            print(current.data)
        
    def iterativepostordersinglestack(self,root):
        if root is None:
            return
        stack = []
        prev = None
        stack.append(root)
        while stack:
            current = stack[-1]
            if prev == None or prev.left == current or prev.right == current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    current = stack.pop()
                    print(current.data)
                    
            elif prev == current.left:
                if current.right:
                    stack.append(current.right)
            else:
                current = stack.pop()
                print(current.data)
                
            prev = current
                                
root = None
b = BST()
for ele in [10, 5, 25, 2, 7, 30]:
    root = b.buildbst(root,ele)
b.postorder(root)
print("*****")
b.iterativepostorder(root)
print("****")
b.iterativepostordersinglestack(root)