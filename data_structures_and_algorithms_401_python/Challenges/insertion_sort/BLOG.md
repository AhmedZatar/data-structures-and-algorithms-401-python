# Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. 


## Pseudocode

```
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

```
## Trace

Sample Array: [8,4,23,42,16,15]



### Pass 1:
when i=1

![1](./blog/1.png)

### Pass 2:
when i=2

![2](./blog/2.png)

### Pass 3:
when i=3

![3](./blog/3.png)



### Pass 4:
when i=4

![4](./blog/4.png)

### Pass 5:
when i=5


![4](./blog/5.png)



## Efficency

Time: O(n^2)

The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times concluding the algorithm to be n squared.

Space: O(1)

No additional space is being created. This array is being sorted in place keeping the space at constant O(1).