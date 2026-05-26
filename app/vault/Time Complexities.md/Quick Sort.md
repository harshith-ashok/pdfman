---
title: Quick Sort
tags:
- Sorting Algorithms
- Time Complexities
---

## Quick Sort

### Algorithms Time Complexity Table

| Algorithm          | Best Case    | Worst Case     | Average Case                  |
| ------------------ | ------------ | --------------- | ----------------------------- |
| Binary Search      | $O(1)$       | $O(\log_{2}n)$  | $O(\log_{2}n)$                |
| [[Sequential Sort]]    | $O(1)$       | $O(n)$          | $O\left( \frac{n}{2} \right)$ |
| **Quick Sort**     | $O(n\log n)$ | $O(n^2)$        | $O(n\log n)$                  |
| [[Merge Sort]]         | $O(n\log n)$ | $O(n\log n)$    | $O(n\log n)$                  |
| **[[Insertion Sort]]** | $O(n)$       | $O(n^2)$        | $O(n^2)$                      |
| Bubble Sort        | $O(n^2)$     | $O(n^2)$        | $O(n^2)$                      |
| Heap Sort          | $O(n\log n)$ | $O(n\log n)$    | $O(n\log n)$                  |
| Selection Sort     | $O(n^2)$     | $O(n^2)$        | $O(n^2)$                      |
| Huffman Coding     | $O(n\log n)$ | $O(n\log n)$    | $O(n\log n)$                  |
| Quick Hull          | $O(n\log n)$ | $O(n^2)$        | $O(n\log n)$                  |
| Shortest Pair      | $O(n\log n)$ | $O(n^2)$        | $O(n\log n)$                  |

### Detailed Analysis of Algorithms

#### Quick Sort
- **Best Case**: Occurs when the array to be sorted is already sorted. In this scenario, quicksort can perform in linear time complexity, $O(n\log n)$.
- **Worst Case**: The worst case happens when the pivot chosen is either the smallest or largest element of the array. This results in a quadratic time complexity, denoted as $O(n^2)$. 
- **Average Case**: Quick sort has an average time complexity of $O(n\log n)$ due to its efficient partitioning and recursive nature.
```

## Connected Notes

- [[Insertion Sort]]
- [[Merge Sort]]
- [[Sequential Sort]]
- [[Binary Search Time Complexities]]
- [[Complexity Analysis]]
- [[Dynamic Programming]]
- [[Graph Theory Applications]]
- [[Hiring Problem]]
- [[Pattern Matching]]
- [[Searching Techniques]]
- [[Quick Hull Algorithm]]
