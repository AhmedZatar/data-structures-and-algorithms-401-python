# Trees
A tree is a nonlinear data structure, compared to arrays, linked lists, stacks and queues which are linear data structures. A tree can be empty with no nodes or a tree is a structure consisting of one node called the root and zero or one or more subtrees.

![0](https://media.geeksforgeeks.org/wp-content/cdn-uploads/binary-tree-to-DLL.png)


## Challenge
1. Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

2. Create a Binary Tree class with this method :
   * pre order
   * in order
   * post order

3. Create a Binary Search Tree class with this method:
    * Add : add a new node with that value in the correct location in the binary search tree.
    * Contains : Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
### Binary Tree
* pre order :
  time : O(n)
  space : O(n)

* in order :
  time : O(n)
  space : O(n)

* post order :
  time : O(n)
  space : O(n)

### Binary Search Tree
* Add :
  time : O(log(n))
  space : O(1)

* Contains :
  time : O(log(n))
  space : O(1)


## API
### Binary Tree: 
1. **pre_order** returns an array of the values, ordered appropriately = root >> left >> right

2. **post_order** returns an array of the values, ordered appropriately = left >> right >> root

3. **in_order** returns an array of the values, ordered appropriately = left >> root >> right


### Binary Search Tree:
1. **add** add a new node with that value in the correct location in the binary search tree.

2. **contains** Returns boolean indicating whether or not the value is in the tree at least once.


