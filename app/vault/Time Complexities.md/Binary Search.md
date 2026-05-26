---
title: Binary Search Time Complexities
tags:
  - Sorting Algorithms
  - Searching Algorithms
  - Time Complexity
---

## Chunk [[Overview]]
This section outlines the time complexities of various sorting and searching algorithms, categorizing them into their best case, worst case, and average case scenarios. The focus is on understanding how these different types of algorithms perform under varying conditions.

### Algorithms Time Complexity Table

| Algorithm          | Best Case    | Worst Case     | Average Case                  |
| ------------------ | ------------ | --------------- | ----------------------------- |
| Binary Search      | $O(1)$       | $O(\log_{2}n)$  | $O(\log_{2}n)$                |
| [[Sequential Sort]]    | $O(1)$       | $O(n)$          | $O\left( \frac{n}{2} \right)$ |
| **[[Quick Sort]]**     | $O(n\log n)$ | $O(n^2)$        | $O(n\log n)$                  |
| [[Merge Sort]]         | $O(n\log n)$ | $O(n\log n)$    | $O(n\log n)$                  |
| **[[Insertion Sort]]** | $O(n)$       | $O(n^2)$        | $O(n^2)$                      |
| Bubble Sort        | $O(n^2)$     | $O(n^2)$        | $O(n^2)$                      |
| Heap Sort          | $O(n\log n)$ | $O(n\log n)$    | $O(n\log n)$                  |
| Selection Sort     | $O(n^2)$     | $O(n^2)$        | $O(n^2)$                      |
| Huffman Coding     | $O(n\log n)$ | $O(n\log n)$    | $O(n\log n)$                  |
| Quick Hull          | $O(n\log n)$ | $O(n^2)$        | $O(n\log n)$                  |
| Shortest Pair      | $O(n\log n)$ | $O(n^2)$        | $O(n\log n)$                  |

### Detailed Analysis of Algorithms

#### Binary Search
- **Best Case**: The search is performed in a sorted array where the target value is at the middle index. This results in a constant time complexity, denoted as $O(1)$. 
- **Worst Case**: Occurs when the target value is not present in the array or is located at one of the ends. In this scenario, the search must traverse through all elements until it finds the target or reaches the end.
- **Average Case**: Similar to the worst case, as binary search repeatedly divides the search interval in half. The average time complexity remains $O(\log_{2}n)$.

#### [[Sequential Sort]]
- **Best Case**: When the input array is already sorted, sequential sort (also known as insertion sort) performs optimally with a time complexity of $O(1)$. This occurs when no swaps are needed during the sorting process.
- **Worst Case**: The worst case happens when the input array is in reverse order. In this scenario, each element must be compared and swapped with its predecessor, resulting in a quadratic time complexity, denoted as $O(n^2)$.
- **Average Case**: For an average sorted sequence, sequential sort has a time complexity of $O\left( \frac{n}{2} \right)$. This is because the algorithm iterates through each element and performs comparisons and swaps.

#### [[Quick Sort]]
- **Best Case**: Occurs when the array to be sorted is already sorted. In this scenario, quicksort can perform in linear time complexity, $O(n\log n)$.
- **Worst Case**: The worst case happens when the pivot chosen is either the smallest or largest element of the array. This results in a quadratic time complexity, denoted as $O(n^2)$. 
- **Average Case**: Quick sort has an average time complexity of $O(n\log n)$ due to its efficient partitioning and recursive nature.

#### [[Merge Sort]]
- **Best Case**: Similar to quicksort, merge sort also performs optimally when the input array is already sorted. In this scenario, it achieves a linearithmic time complexity, denoted as $O(n\log n)$.
- **Worst Case**: Like quicksort and insertion sort, merge sort has a worst-case time complexity of $O(n\log n)$. This occurs regardless of the initial order of elements in the array.
- **Average Case**: Merge sort consistently performs with a linearithmic time complexity, denoted as $O(n\log n)$.

#### [[Insertion Sort]]
- **Best Case**: When the input array is already sorted. In this scenario, insertion sort achieves its optimal performance with a constant time complexity of $O(1)$.
- **Worst Case**: The worst case happens when the input array is in reverse order. Here, each element must be compared and swapped with its predecessor, resulting in a quadratic time complexity, denoted as $O(n^2)$.
- **Average Case**: Insertion sort has an average time complexity of $O(n^2)$. This occurs because it iterates through the array and performs comparisons and swaps.

#### Bubble Sort
- **Best Case**: Similar to insertion sort, bubble sort achieves its optimal performance when the input array is already sorted. In this scenario, it performs with a constant time complexity of $O(1)$.
- **Worst Case**: The worst case happens when the input array is in reverse order. Here, each element must be compared and swapped with its predecessor, resulting in a quadratic time complexity, denoted as $O(n^2)$.
- **Average Case**: Bubble sort has an average time complexity of $O(n^2)$. This occurs because it iterates through the array multiple times until no more swaps are needed.

#### Heap Sort
- **Best Case**: Similar 
```

## Connected Notes

- [[Complexity Analysis]]
- [[Dynamic Programming]]
- [[Graph Theory Applications]]
- [[Hiring Problem]]
- [[Insertion Sort]]
- [[Merge Sort]]
- [[Pattern Matching]]
- [[Quick Sort]]
- [[Searching Techniques]]
- [[Sequential Sort]]
- [[Time Complexity Analysis]]
- [[Overview]]
