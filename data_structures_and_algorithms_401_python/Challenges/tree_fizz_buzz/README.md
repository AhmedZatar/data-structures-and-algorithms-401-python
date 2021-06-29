# Challenge Summary
Write a function called fizz buzz tree
* Arguments: k-ary tree
* Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

* If the value is divisible by 3, replace the value with “Fizz”
* If the value is divisible by 5, replace the value with “Buzz”
* If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
* If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process
![0](./tree_fizz_buzz.png)


## Approach & Efficiency
1. Ceate  function called fizz_buzz_tree take kary_Tree as arg
2. create inside it another function caled traverse take node ass arg
3. check if the node has children if it is 
4. loop around the children call the function again and put the children as arg
5. do all  fizz buzz checks inside the loop and change the value for the node it it is true
6. trutn the kAry_Tree

### Big O :
* Time--> O(n^2)
* space--> O(1)

## Solution
```
input = k_Ary_Tree at input pic
Expected output = k_Ary_Tree at ouput pic

traverse(root):
   if root.children: True
       for i in range(3):
            traverse(Node(2)
            if 2%3 and 2%5: false
            else:
            node(2)=Node(str(2))

...
return the new k_ary_tree
```
