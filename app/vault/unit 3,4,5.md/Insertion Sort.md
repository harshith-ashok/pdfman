---
title: Insertion Sort
---

## Insertion Sort

### Detailed Explanation

#### Introduction
Insertion sort is an intuitive sorting algorithm that builds the final sorted array one element at a time, mimicking how humans might sort playing cards. The process involves dividing the array into a "sorted" portion (initially just the first element) and an "unsorted" portion.

#### Algorithmic Process

1. **Initialization:** Start with the second element of the array.
2. **Iteration:** For each subsequent element, compare it to elements in the sorted portion from right to left.
3. **Shift Elements:** Shift all elements greater than the key one position to the right to make space for the insertion.
4. **Insert Key:** Insert the key into its correct position within the sorted portion.

#### [[Complexity Analysis]]

- **Time Complexity:**
  - **Best Case:** $O(N)$ occurs when the array is already sorted. The inner loop makes only one comparison per element.
  - **Worst and Average Case:** $O(N^2)$. When the array is sorted in reverse order, every new element must be compared to all previously sorted elements.
- **Space Complexity:** $O(1)$ as it is an in-place sorting algorithm requiring only a constant amount of extra memory for the key variable.
- **Characteristics:** It is stable and highly efficient for small data sets or nearly sorted arrays.

## [[Asymptotic Notation]]

### Detailed Explanation

#### Introduction
Asymptotic notation is used to describe the limiting behavior of functions as input size approaches infinity. The primary notations are Big-O (upper bound), Big-Omega (lower bound), and Big-Theta (tight bound).

#### Primary Notations

1. **Big-O Notation ($O$) - Upper Bound**
   - $f(n) = O(g(n))$: If there exist positive constants $c$ and $n_0$, such that for all $n \ge n_0$, $0 \le f(n) \le c \cdot g(n)$.
2. **Big-Omega Notation ($\Omega$) - Lower Bound**
   - $f(n) = \Omega(g(n))$: If there exist positive constants $c$ and $n_0$, such that for all $n \ge n_0$, $0 \le c \cdot g(n) \le f(n)$.
3. **Big-Theta Notation ($\Theta$) - Tight Bound**
   - $f(n) = \Theta(g(n))$: If there exist positive constants $c_1, c_2,$ and $n_0$, such that for all $n \ge n_0$, $0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n)$.

#### Strict Bounds

- **Little-o ($o$):** Strict upper bound. $f(n)$ grows strictly slower than $g(n)$.
- **Little-omega ($\omega$):** Strict lower bound. $f(n)$ grows strictly faster than $g(n)$.

## [[Closest Pair of Points Problem]]

### Detailed Explanation

#### Introduction
The Closest Pair of Points problem requires finding the two points in a set that are closest to each other based on Euclidean distance. A brute-force approach is inefficient, but the divide-and-conquer method can solve it efficiently with an overall time complexity of $O(N \log N)$.

#### Algorithmic Process

1. **Sort:** Sort the points by their X-coordinates.
2. **Divide and Conquer:**
   - Draw a vertical line to divide the set into two equal halves ($S_L$ and $S_R$).
   - Recursively find the closest pair in each half, let distance be $d_L$ for $S_L$ and $d_R$ for $S_R$. Let $d = \min(d_L, d_R)$.
   - Combine: The overall closest pair is either entirely in one of the halves or spans across the dividing line. Only points within a vertical strip of width $2d$ need to be checked.
3. **Strip Processing:** Sort the points in the strip by their Y-coordinates and check distances against at most 7 subsequent points.

#### [[Complexity Analysis]]

- **Time Complexity:** Sorting initially takes $O(N \log N)$. The recurrence for the divide-and-conquer step is $T(n) = 2T(n/2) + O(N)$, which resolves to $O(N \log N)$. Overall time complexity is $O(N \log N)$.
- **Space Complexity:** $O(N)$ to store sub-arrays and the strip array during recursion.

## [[Quick Hull Algorithm]]

### Detailed Explanation

#### Introduction
The Quick Hull algorithm finds the Convex Hull of a set of points in 2D space. It recursively divides and conquers by identifying key points that form the convex hull.
```

## Connected Notes

- [[Merge Sort]]
- [[Quick Sort]]
- [[Sequential Sort]]
- [[Binary Search Time Complexities]]
- [[Complexity Analysis]]
- [[Dynamic Programming]]
- [[Graph Theory Applications]]
- [[Hiring Problem]]
- [[Pattern Matching]]
- [[Searching Techniques]]
