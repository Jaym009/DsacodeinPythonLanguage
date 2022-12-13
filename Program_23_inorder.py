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
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
        
    def iterativeinorder(self, root):
        current = root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data)
                current = current.right
            else:
                break
        
        
root = None
b = BST()
for ele in [10, 5, 25, 2, 7, 30]:
    root = b.buildbst(root,ele)
b.inorder(root)
print("*****")
b.iterativeinorder(root)