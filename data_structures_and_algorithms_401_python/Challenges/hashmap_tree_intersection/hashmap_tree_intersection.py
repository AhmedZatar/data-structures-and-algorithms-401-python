class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'

class Hash_table:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size 
    
    def hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 19
        hashed_key = temp_value % self.size
        return hashed_key
    
    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key,value))

    def contains(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.data[0]
            current=self.map[hashed_key].head
            while current:
                if current.data[0]==key:
                    return True
                else:
                    current=current.next
        return False

    def get(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.data[0]
            current=self.map[hashed_key].head
            while current:
                if current.data[0]==key:
                    return current.data[1]
                else:
                    current=current.next
        return None


class Nodet:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

           

class BinaryTree:
    def __init__(self):
        self.root = None


def intersection(tree1,tree2):
    arr=[]
    hashtable=Hash_table(1024)

    if tree1.root==None or tree2.root==None:
        return 'one of the tree is empty'

    def travers(node):
        if hashtable.contains(str(node.value)):
            nonlocal arr
            arr+=[node.value]
        else:
            hashtable.add(str(node.value),True)
        
        if node.left:
            travers(node.left)
        if node.right:
            travers(node.right)
    travers(tree1.root)
    travers(tree2.root)

    return arr



if __name__ == "__main__":
    tree1=BinaryTree()
    tree1.root=Nodet(150)
    tree1.root.left=Nodet(100)
    tree1.root.right=Nodet(250)
    tree1.root.left.left=Nodet(75)
    tree1.root.left.right=Nodet(160)
    tree1.root.right.left=Nodet(200)
    tree1.root.right.right=Nodet(350)
    tree1.root.left.right.left=Nodet(125)
    tree1.root.left.right.right=Nodet(175)
    tree1.root.right.right.left=Nodet(300)
    tree1.root.right.right.right=Nodet(500)

    tree2=BinaryTree()
    tree2.root=Nodet(42)
    tree2.root.left=Nodet(100)
    tree2.root.right=Nodet(600)
    tree2.root.left.left=Nodet(15)
    tree2.root.left.right=Nodet(160)
    tree2.root.right.left=Nodet(200)
    tree2.root.right.right=Nodet(350)
    tree2.root.left.right.left=Nodet(125)
    tree2.root.left.right.right=Nodet(175)
    tree2.root.right.right.left=Nodet(4)
    tree2.root.right.right.right=Nodet(500)

    print(intersection(tree1,tree2))









