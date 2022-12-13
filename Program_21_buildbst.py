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
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
    
    def search(self, root, ele):
        if root is None or root.data == ele:
            return root
        if ele < root.data:
            return self.search(root.left, ele)
        return self.search(root.right, ele)
    
    def minvalue(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.data
    
    def maxvalue(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.data
    
root = None
b = BST()
for ele in [10, 5, 25, 2, 7, 30]:
    root = b.buildbst(root,ele)
b.inorder(root)
search_ele = b.search(root,40)
if search_ele == None:
    print("Element is not found")
else:
    print("Element is found in the bst {}".foramt(search_ele.data))
b.minvalue(root)
b.maxvalue(root)
