from re import escape


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):

        output = ''
        if not self.root:
            return 'The Tree is empty'


        def traverse(node):
            nonlocal output 
            output += str(node.value) 

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)
                  
        traverse(self.root)

        return output
    
    def post_order(self):
        output = ''
        if not self.root:
            return 'The Tree is empty'
        
        def traverse(node):
            nonlocal output 

            if node.left:
                
                traverse(node.left)
                
            if node.right:
                traverse(node.right)

            output += str(node.value)       

        
        traverse(self.root)
         
        return output

    def in_order(self):
        output = ''
        if not self.root:
            return 'The Tree is empty'
        
        def traverse(node):
            nonlocal output 

            if node.left:
                
                traverse(node.left)

            output += str(node.value)
                
            if node.right:
                traverse(node.right)

        traverse(self.root)
         
        return output



class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None
    def add(self,value):

        if self.root ==None:
            self.root=Node(value)
        else:
            node = Node(value)
            x=None

            def traverse(root):
                
                if root.value==node.value:
                    nonlocal x
                    x= 'duplicates value'
                    return

                if node.value < root.value:

                    if root.left:
                        root=root.left
                        traverse(root)
                    else:
                        root.left=node
                else:

                    if root.right:
                        root=root.right
                        traverse(root)
                    else:
                        root.right=node

            traverse(self.root)
            return x
    
    def contains(self,value):
        x=False
        if self.root ==None:
            return 'The Tree is empty'
        else:
            def traverse(root):
                
                if root.value==value:
                    nonlocal x
                    x=True
                if root.value>value:
                    if not root.left:
                        return

                    if root.left.value==value:
                        x= True
                    else:
                        traverse(root.left)
                if root.value<value:
                    if not root.right:
                        return
                    if root.right.value==value:
                        x= True
                    else:
                        traverse(root.right)


            traverse(self.root)

            return x



          
if __name__ == "__main__":
    tree= BinarySearchTree()
    tree.add(8)
    tree.add(4)
    tree.add(7)
    tree.add(3)

    print(tree.root.left.left.value)
    print(tree.contains(12))
