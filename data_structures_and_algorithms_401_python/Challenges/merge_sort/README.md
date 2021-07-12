# Challenge Summary
Create function take an array as argument than sort it in Merge Sort.

## Whiteboard Process

![0](./merge_sort.png)

## Approach & Efficiency
1. Ceate  function take array of numbers as arg
2. declear n equal the length of array
3. let mid half of n
4. let left the first half and right the seconde half
5. clal the function again with left and right
6. after that create new function called merge take three argument left, right and the orgnal array
7. call merge with the left, right and array

### Big O :
* Time--> O(log(n))
* space--> O(1)
## Solution
```
input = [8,4,23,42,16,15]
Expected output = [4,8,15,16,23,42]

InsertionSort(arr):

  n=6

  if 6>1: True

     mid =3

     left = [4,8,15]

     right = [16,23,42]
     
     mergesort(left)
      mergesort(right)
      merge(left, rigth,arr)
     
....

return [4,8,15,16,23,42]

```
