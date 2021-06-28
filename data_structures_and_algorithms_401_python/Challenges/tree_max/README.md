# Challenge Summary
Write method for the Binary Tree class find maximum value :
* Arguments: none
* Returns: number

Find the maximum value stored in the tree. 

## Whiteboard Process
![0](./tree_max.png)


## Approach & Efficiency

Ceate  method called max, declear varible maxvalue = 0 Create function call traverse take a node as argument inside it i will check if there is left node and check if there is right node inside every check i will call the function again and check if the value of the node more than the max value if it is the value of the node will be the new max, for firt time we will call the function with the root, at end check if the vlaue of the root more than max if it is the max will be the root value

### Big O :
* Time--> O(n)
* space--> O(1)

## Solution
```
input = tree in the pic
Expected output = 11

self.max=0
traverse(Node(2))

if Node(7): True
   traverse(Node(7))
...
if Node(5): True
   traverse(Node(5))
...

if 2>11 #False

return 11
```
