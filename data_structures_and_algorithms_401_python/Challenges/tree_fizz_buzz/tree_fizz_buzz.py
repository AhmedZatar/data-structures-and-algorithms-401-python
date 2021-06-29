
class Node:
    def __init__(self, value):
        self.value = value
        self.children=[]

class KAryTree:
    def __init__(self):
        self.root = None


def fizz_buzz_tree(kAryTree):
    
    def traverse(node):

        if node.children:
            for i in range(len(node.children)):
                traverse(node.children[i])
                if node.children[i].value%5==0 and node.children[i].value%3==0:
                   
                    node.children[i].value='Fizz Buzz'
                elif node.children[i].value%5==0:
                    
                    node.children[i].value='Buzz'
                elif node.children[i].value%3==0:

                    node.children[i].value='Fizz'     
                else:
                    node.children[i].value=str(node.children[i].value)
    traverse(kAryTree.root)
    if kAryTree.root.value%5==0 and kAryTree.root.value%3==0:
                   
        kAryTree.root.value='Fizz Buzz'
    elif kAryTree.root.value%5==0:
                    
        kAryTree.root.value='Buzz'
    elif kAryTree.root.value%3==0:

        kAryTree.root.value='Fizz'     
    else:
        kAryTree.root.value=str(kAryTree.root.value)

    return kAryTree
    

if __name__ == "__main__":

    kAryTree = KAryTree()
    kAryTree.root=Node(1)
    kAryTree.root.children+=[Node(2)]
    kAryTree.root.children+=[Node(3)]
    kAryTree.root.children+=[Node(4)]
    kAryTree.root.children[0].children+=[Node(5)]
    kAryTree.root.children[0].children+=[Node(6)]
    kAryTree.root.children[0].children+=[Node(7)]
    kAryTree.root.children[1].children+=[Node(8)]
    kAryTree.root.children[2].children+=[Node(9)]
    kAryTree.root.children[2].children+=[Node(10)]
    kAryTree.root.children[0].children[2].children+=[Node(11)]
    kAryTree.root.children[0].children[2].children+=[Node(12)]
    kAryTree.root.children[2].children[1].children+=[Node(13)]
    kAryTree.root.children[2].children[1].children+=[Node(14)]
    kAryTree.root.children[2].children[1].children+=[Node(15)]
    kAryTree.root.children[2].children[1].children+=[Node(16)]
    fizz_buzz_tree(kAryTree)
    print(kAryTree.root.children[1].value)
    print(kAryTree.root.children[2].children[1].children[2].value)













