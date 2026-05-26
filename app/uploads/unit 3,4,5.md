## 1. Insertion Sort

### 1.1 Introduction

Insertion Sort is a simple, intuitive sorting algorithm that builds the final sorted array one item at a time. It mimics the way a human might sort a hand of playing cards: taking one card at a time and inserting it into its correct position relative to the already sorted cards.

### 1.2 Algorithmic Process

The algorithm divides the array into a "sorted" portion (initially just the first element) and an "unsorted" portion.

1. Iterate from the second element to the end of the array.
    
2. For each element (the "key"), compare it to the elements in the sorted portion from right to left.
    
3. Shift all elements in the sorted portion that are greater than the key one position to the right to make space.
    
4. Insert the key into the vacated position.
    

### 1.3 Complexity Analysis

- **Time Complexity:**
    
    - **Best Case:** $O(N)$ occurs when the array is already sorted. The inner loop makes only one comparison per element.
        
    - **Worst and Average Case:** $O(N^2)$ occurs when the array is sorted in reverse order. Every new element must be compared to all previously sorted elements.
        
- **Space Complexity:** $O(1)$. It is an in-place sorting algorithm requiring only a constant amount of extra memory for the key variable.
    
- **Characteristics:** It is a **stable** sort (preserves the relative order of equal elements) and is highly efficient for small data sets or nearly sorted arrays.
    

---

## 2. Asymptotic Notation

### 2.1 Introduction

Asymptotic notation is a mathematical tool used in computer science to describe the limiting behavior of a function when the argument tends towards a particular value or infinity. It is primarily used to analyze the time and space complexity of algorithms independent of machine-specific constants.

### 2.2 Primary Notations

#### 2.2.1 Big-O Notation ($O$) - Upper Bound

Big-O notation defines an asymptotic upper bound. It describes the worst-case scenario or the maximum time required by an algorithm.

Formally, $f(n) = O(g(n))$ if there exist positive constants $c$ and $n_0$ such that:

$$0 \le f(n) \le c \cdot g(n) \text{ for all } n \ge n_0$$

#### 2.2.2 Big-Omega Notation ($\Omega$) - Lower Bound

Big-Omega notation defines an asymptotic lower bound. It describes the best-case scenario.

Formally, $f(n) = \Omega(g(n))$ if there exist positive constants $c$ and $n_0$ such that:

$$0 \le c \cdot g(n) \le f(n) \text{ for all } n \ge n_0$$

#### 2.2.3 Big-Theta Notation ($\Theta$) - Tight Bound

Big-Theta bounds a function from above and below, providing an exact asymptotic behavior.

Formally, $f(n) = \Theta(g(n))$ if there exist positive constants $c_1, c_2,$ and $n_0$ such that:

$$0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \text{ for all } n \ge n_0$$

### 2.3 Strict Bounds

- **Little-o ($o$):** Strict upper bound. $f(n)$ grows strictly slower than $g(n)$.
    
- **Little-omega ($\omega$):** Strict lower bound. $f(n)$ grows strictly faster than $g(n)$.
    

---

## 3. Closest Pair of Points

### 3.1 Introduction

Given a set of $N$ points in a 2D plane, the Closest Pair of Points problem requires finding the two points that are closest to each other according to the Euclidean distance metric. A brute-force approach of checking every pair takes $O(N^2)$ time.

### 3.2 Divide and Conquer Approach

1. **Sort:** Sort the points based on their X-coordinates.
    
2. **Divide:** Draw a vertical line to divide the set of points into two equal halves: a left subset ($S_L$) and a right subset ($S_R$).
    
3. **Conquer:** Recursively find the closest pair in $S_L$ (let distance be $d_L$) and $S_R$ (let distance be $d_R$). Let $d = \min(d_L, d_R)$.
    
4. **Combine:** The overall closest pair is either entirely in $S_L$, entirely in $S_R$, or spans across the dividing line. We only need to check points within a vertical "strip" of width $2d$ centered on the dividing line.
    
5. **Strip Processing:** Sort the points in the strip by their Y-coordinates. For each point in the strip, we only need to check its distance against a constant number of subsequent points (at most 7) to see if a distance smaller than $d$ exists.
    

### 3.3 Complexity Analysis

- **Time Complexity:** Sorting initially takes $O(N \log N)$. The recurrence for the divide and conquer step is $T(n) = 2T(n/2) + O(N)$, which resolves to $O(N \log N)$. Overall time is **$O(N \log N)$**.
    
- **Space Complexity:** $O(N)$ to store the sub-arrays and the strip array during recursion.
    

---

## 4. Quick Hull

### 4.1 Introduction

Quick Hull is a divide-and-conquer algorithm used to find the Convex Hull of a finite set of points in a 2D plane. The convex hull is the smallest convex polygon that encloses all the points in the set. The algorithm draws parallels to the Quicksort sorting algorithm.

### 4.2 Algorithmic Process

1. Find the points with the minimum and maximum X-coordinates. These two points are guaranteed to be on the convex hull.
    
2. Draw a line joining these two points, dividing the remaining set of points into two subsets (one on each side of the line).
    
3. For one of the subsets, find the point farthest from the dividing line. This point is also on the convex hull.
    
4. The two initial points and the newly found farthest point form a triangle. Any points inside this triangle cannot be on the convex hull and are discarded.
    
5. The triangle leaves two new lines on the "outside" boundary. Recursively apply steps 3 and 4 to the points outside these two new lines.
    
6. Repeat for the other subset from step 2.
    

### 4.3 Complexity Analysis

- **Time Complexity:**
    
    - **Average Case:** $O(N \log N)$, assuming the points are distributed such that the subsets are divided relatively evenly.
        
    - **Worst Case:** $O(N^2)$, occurring when the points form a highly skewed shape, such as lying on the perimeter of a circle, requiring all points to be processed at each recursive step.
        
- **Space Complexity:** $O(N)$ for the recursion stack in the worst case.
    

---

## 5. Recurrence Tree

### 5.1 Introduction

The Recurrence Tree (or Recursion Tree) is a visual and mathematical method used to solve recurrence relations, particularly those arising from divide-and-conquer algorithms. It helps in formulating an educated guess for the Master Theorem or solving recurrences that the Master Theorem cannot handle.

### 5.2 Methodological Steps

1. **Construct the Tree:** Each node represents the non-recursive cost of a single subproblem. The root represents the original problem. The children of a node represent the recursive calls made by that subproblem.
    
2. **Determine Costs Per Level:** Calculate the sum of the costs of all nodes at each depth level of the tree.
    
3. **Determine Tree Depth:** Identify the longest path from the root to a leaf to find the height or depth of the tree.
    
4. **Sum Total Cost:** The total execution time is the sum of the costs across all levels of the tree.
    

### 5.3 Example Application

Consider Merge Sort: $T(n) = 2T(n/2) + cn$.

- Level 0 (Root): Cost is $cn$.
    
- Level 1: Two nodes, each size $n/2$, cost is $c(n/2) + c(n/2) = cn$.
    
- Level $i$: $2^i$ nodes, each size $n/2^i$, total cost is $2^i \cdot c(n/2^i) = cn$.
    
- The tree depth is $\log_2 n$.
    
- Total Cost = $\sum_{i=0}^{\log_2 n} cn = cn \log_2 n + cn = O(N \log N)$.
    

---

## 6. Linear Search

### 6.1 Introduction

Linear search, also known as sequential search, is the simplest method for finding a target value within a list. It checks each element of the list consecutively until a match is found or the whole list has been searched.

### 6.2 Applicability

Unlike more advanced search algorithms, linear search does not require the underlying data to be sorted. It is universally applicable to any array or linked list.

### 6.3 Complexity Analysis

- **Time Complexity:**
    
    - **Best Case:** $O(1)$ if the target element is the very first element.
        
    - **Worst Case:** $O(N)$ if the target is the last element or is not present in the array at all.
        
    - **Average Case:** $O(N/2)$ which simplifies to $O(N)$.
        
- **Space Complexity:** $O(1)$ as it operates completely in place, utilizing only a single iterator variable.
    

---

## 7. Master Theorem

### 7.1 Introduction

The Master Theorem provides a direct, formulaic recipe for solving recurrence relations that frequently arise in divide-and-conquer algorithms. It applies to recurrences of the form:

$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$

Where:

- $n$ is the size of the problem.
    
- $a \ge 1$ is the number of subproblems in the recursion.
    
- $b > 1$ is the factor by which the subproblem size is reduced.
    
- $f(n)$ is the cost of the work done outside the recursive calls (dividing and merging).
    

### 7.2 The Three Cases

The theorem compares the function $f(n)$ to the critical polynomial $n^{\log_b a}$.

- **Case 1: Heavy Leaves**
    
    If $f(n) = O(n^{\log_b a - \epsilon})$ for some constant $\epsilon > 0$, then the leaves of the recursion tree dominate the cost.
    
    **Solution:** $T(n) = \Theta(n^{\log_b a})$
    
- **Case 2: Balanced Tree**
    
    If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for some $k \ge 0$, the cost is evenly distributed across the tree levels.
    
    **Solution:** $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$
    
- **Case 3: Heavy Root**
    
    If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some constant $\epsilon > 0$, AND if $f(n)$ satisfies the regularity condition $a \cdot f(n/b) \le c \cdot f(n)$ for some constant $c < 1$ and all sufficiently large $n$, then the root dominates the cost.
    
    **Solution:** $T(n) = \Theta(f(n))$
    

---

## 8. Binary Search

### 8.1 Introduction

Binary search is a highly efficient search algorithm used to find the position of a target value within a **sorted** array. It utilizes a divide-and-conquer strategy, drastically reducing the search space at each step.

### 8.2 Algorithmic Process

1. Define a search interval spanning the entire array (using `low` and `high` pointers).
    
2. Calculate the middle index: `mid = low + (high - low) / 2`.
    
3. Compare the target value to the element at the `mid` index.
    
    - If they are equal, the target is found; return the index.
        
    - If the target is less than the middle element, it must lie in the left half. Update `high = mid - 1`.
        
    - If the target is greater than the middle element, it must lie in the right half. Update `low = mid + 1`.
        
4. Repeat steps 2-3 until the target is found or the interval is empty (`low > high`).
    

### 8.3 Complexity Analysis

- **Time Complexity:**
    
    - **Best Case:** $O(1)$ if the middle element is the target on the first check.
        
    - **Worst/Average Case:** $O(\log N)$. Because the search space is halved at every iteration, the maximum number of steps is bounded by the base-2 logarithm of $N$.
        
- **Space Complexity:** $O(1)$ for the iterative implementation. The recursive implementation requires $O(\log N)$ space for the function call stack.
    

---

## 9. Towers of Hanoi

### 9.1 Introduction

The Towers of Hanoi is a classic mathematical puzzle consisting of three vertical pegs (Source, Auxiliary, Destination) and a number of disks of varying sizes. The objective is to move the entire stack of disks from the Source peg to the Destination peg.

### 9.2 The Rules

1. Only one disk may be moved at a time.
    
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty peg.
    
3. No larger disk may be placed on top of a smaller disk.
    

### 9.3 Recursive Solution

The problem exhibits perfect overlapping subproblems suitable for recursion. To move $n$ disks:

1. Move the top $n-1$ disks from the Source peg to the Auxiliary peg, using the Destination peg as temporary storage.
    
2. Move the $n$th (largest) disk directly from the Source peg to the Destination peg.
    
3. Move the $n-1$ disks from the Auxiliary peg to the Destination peg, using the Source peg as temporary storage.
    

### 9.4 Complexity Analysis

- **Recurrence Relation:** $T(n) = 2T(n-1) + 1$, with base case $T(1) = 1$.
    
- **Time Complexity:** Solving the recurrence yields $T(n) = 2^n - 1$. Thus, the time complexity is strictly **$O(2^n)$**, making it an exponential time algorithm.
    
- **Space Complexity:** $O(n)$ to maintain the recursive call stack.
    

---

## 10. Quicksort

_(Note: Addressed based on the common curriculum context for "quickset")_

### 10.1 Introduction

Quicksort is a highly efficient, general-purpose sorting algorithm utilizing the divide-and-conquer paradigm. Developed by Tony Hoare, it is widely used in practice due to its excellent average-case performance and in-place sorting capabilities.

### 10.2 The Partitioning Process

The core of Quicksort is the partition function:

1. Select an element from the array to act as the "pivot" (commonly the last element, the first element, or a random element).
    
2. Rearrange the array such that all elements smaller than the pivot are placed before it, and all elements greater than the pivot are placed after it.
    
3. The pivot is now in its final, sorted position.
    
4. Recursively apply the same process to the sub-array of elements smaller than the pivot and the sub-array of elements greater than the pivot.
    

### 10.3 Complexity Analysis

- **Time Complexity:**
    
    - **Best and Average Case:** $O(N \log N)$. This occurs when the pivot consistently divides the array into two roughly equal halves.
        
    - **Worst Case:** $O(N^2)$. This occurs when the array is already sorted (or reverse sorted) and the algorithm consistently picks the largest or smallest element as the pivot, leading to completely unbalanced partitions (sizes 0 and $N-1$).
        
- **Space Complexity:** $O(\log N)$ on average for the recursive call stack. In the worst case, it degrades to $O(N)$.
    
- **Characteristics:** It is an **unstable** sort.
    

---

## 11. Transpose of a Matrix

### 11.1 Introduction

In linear algebra, the transpose of a matrix is an operator that flips a matrix over its main diagonal. It switches the row and column indices of the matrix by producing a new matrix.

### 11.2 Definition and Algorithm

Given an $M \times N$ matrix $A$, its transpose is an $N \times M$ matrix $A^T$.

The mathematical definition is: $A^T[i][j] = A[j][i]$ for all $1 \le i \le N$ and $1 \le j \le M$.

**Algorithm (In-place for an $N \times N$ square matrix):**

Iterate through the upper triangle of the matrix (where row index < column index) and swap the elements across the diagonal: `swap(A[i][j], A[j][i])`.

### 11.3 Complexity Analysis

- **Time Complexity:** $O(M \times N)$ since every element in the matrix must be read and written exactly once.
    
- **Space Complexity:**
    
    - $O(1)$ if the matrix is square ($N \times N$) and transposed in-place.
        
    - $O(M \times N)$ if the matrix is rectangular, as a completely new 2D array of different dimensions must be allocated.
        

---

## 12. Maximum Subarray Sum (Kadane's Algorithm)

### 12.1 Introduction

The Maximum Subarray problem is the task of finding the contiguous subarray within a one-dimensional array of numbers (containing at least one positive number) that has the largest sum.

### 12.2 Dynamic Programming: Kadane’s Algorithm

Kadane's algorithm solves this problem in linear time by utilizing a dynamic programming approach. The core idea is to calculate the maximum subarray sum ending at a specific position by using the maximum subarray sum ending at the previous position.

**Logic:**

For each element, we decide whether to add it to the existing running subarray sum, or to start a new subarray beginning with the current element. We do this by comparing the current element itself to the sum of the current element plus the running total.

Plaintext

```
Initialize:
    max_so_far = INT_MIN
    current_max = 0

Loop for each element x in array:
    current_max = max(x, current_max + x)
    max_so_far = max(max_so_far, current_max)
```

### 12.3 Complexity Analysis

- **Time Complexity:** $O(N)$ because the algorithm requires only a single pass through the array.
    
- **Space Complexity:** $O(1)$ as it only requires a few integer variables to keep track of the running maximums, regardless of the array size.
    

---

## 13. Merge Sort

### 13.1 Introduction

Merge Sort is a robust, comparison-based sorting algorithm based on the divide-and-conquer strategy. It was invented by John von Neumann in 1945. It is known for its predictable $O(N \log N)$ performance and its stability.

### 13.2 Algorithmic Process

1. **Divide:** Recursively divide the unsorted list into $N$ sublists, each containing one element (a list of one element is considered sorted).
    
2. **Conquer/Merge:** Repeatedly merge sublists to produce new sorted sublists until there is only one sorted list remaining. This will be the sorted list.
    
    - Merging involves comparing the first elements of two sublists, taking the smaller one, and placing it into the new list, advancing the pointer of the sublist from which the element was taken.
        

### 13.3 Complexity Analysis

- **Time Complexity:**
    
    - The recurrence relation is $T(n) = 2T(n/2) + O(N)$.
        
    - According to the Master Theorem (Case 2), this strictly evaluates to **$\Theta(N \log N)$** in the Best, Average, and Worst cases. The division process takes $\log N$ steps, and merging at each level takes $O(N)$ time.
        
- **Space Complexity:** $O(N)$. Merge sort is not an in-place sorting algorithm. It requires an auxiliary array equal in size to the original array to hold the elements while merging.
    
- **Characteristics:** It is a **stable** sort.
    

---

## 14. Strassen's Matrix Multiplication

### 14.1 Introduction

Standard matrix multiplication of two $N \times N$ matrices requires $O(N^3)$ operations. Volker Strassen published an algorithm in 1969 that proved that the $O(N^3)$ bound was not tight, offering a divide-and-conquer approach that reduces the number of recursive multiplications required.

### 14.2 Algorithmic Principle

The standard divide-and-conquer matrix multiplication splits the $N \times N$ matrices into four $N/2 \times N/2$ submatrices. Calculating the resulting quadrants requires 8 multiplications of these submatrices, leading to the recurrence $T(n) = 8T(n/2) + O(n^2)$, which yields $O(N^3)$.

Strassen's breakthrough was discovering a set of algebraic formulas that define 7 intermediate matrices (often denoted $M_1$ through $M_7$). These 7 matrices require exactly 7 multiplications of the submatrices, along with a number of additions and subtractions.

### 14.3 Complexity Analysis

By reducing the number of recursive multiplications from 8 to 7, Strassen altered the recurrence relation to:

$$T(n) = 7T\left(\frac{n}{2}\right) + O(n^2)$$

Where $O(n^2)$ represents the time taken for the matrix additions and subtractions.

Applying the Master Theorem:

- $a = 7, b = 2, f(n) = O(n^2)$
    
- Compare $f(n)$ with $n^{\log_b a} = n^{\log_2 7} \approx n^{2.807}$.
    
- Since $n^2 = O(n^{\log_2 7 - \epsilon})$, Case 1 of the Master Theorem applies.
    
- **Time Complexity:** $\Theta(N^{\log_2 7}) \approx O(N^{2.81})$. For significantly large matrices, this is faster than the naive $O(N^3)$ approach.
    
- **Space Complexity:** $O(N^2)$ to store the intermediate submatrices ($M_1$ through $M_7$) at each recursive step.