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
    
    def countNodes(self, root):
        if root is None:
            return 0
        return 1+ self.countNodes(root.left) + self.countNodes(root.right)
    
    def leafcount(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return self.leafcount(root.left) + self.leafcount(root.right)
    
    def maxdepth(self, root):
        if root is None:
            return 0
        else:
            ldepth = self.maxdepth(root.left)
            rdepth = self.maxdepth(root.right)
            return max(ldepth, rdepth) + 1
        
    def iterativeMaxDepth(self, root):
        stack = []
        if root:
            stack.append((1,root))
        depth = 0
        while stack:
            current_depth , root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, root.left))
                stack.append((current_depth+1, root.right))
        return depth
    
root = None
b = BST()
for ele in [2, 1, 33, 0, 25, 40, 11, 34, 7, 12, 36, 13]:
    root = b.buildbst(root,ele)
total = b.countNodes(root)
print(total)
print("Total number of leaf nodes in a given binary tree")
leafcount = b.leafcount(root)
print(leafcount)
print("Maximum depth of a binary tree is")
height = b.maxdepth(root)
print(height)
height1 = b.iterativeMaxDepth(root)
print(height1)