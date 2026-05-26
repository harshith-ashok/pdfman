---
title: Graph Theory Applications
tags:
- Sorting Algorithms
- Searching Techniques
- Dynamic Programming
- Complexity Analysis
---


## Detailed Notes

### Huffman Coding using Greedy Approach
- **Key Concepts:**
  - Huffman coding is an optimal prefix code generated from the frequency of occurrence of symbols.
  - It uses a greedy approach to minimize the weighted path length in a binary tree structure.
  - The algorithm constructs a binary tree where each leaf node represents a symbol and its frequency, with non-leaf nodes representing the sum of their child nodes' frequencies.

### Minimum Spanning Tree with Complexity
- **Key Concepts:**
  - A minimum spanning tree (MST) is a subset of edges that forms a tree including all vertices.
  - Prim's algorithm and Kruskal's algorithm are commonly used to find MSTs.
  - The complexity of Prim's algorithm is \(O(E + V \log V)\), where \(E\) is the number of edges, and \(V\) is the number of vertices. For Kruskal’s algorithm, it is \(O((E + V) \log V)\).

### [[Matrix Chain Multiplication]] & Its Complexity
- **Key Concepts:**
  - Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices.
  - The optimal parenthesization problem can be solved using dynamic programming.
  - The complexity of this algorithm is \(O(n^3)\), where \(n\) is the number of matrices.

### Longest Common Subsequence
- **Key Concepts:**
  - This problem involves finding the longest subsequence common to two sequences.
  - It can be solved using a recursive approach with memoization or dynamic programming.
  - The time complexity of this algorithm is \(O(m \times n)\), where \(m\) and \(n\) are the lengths of the two sequences.

### N Queen’s Problem Using Backtracking
- **Key Concepts:**
  - This problem involves placing `N` queens on an `N x N` chessboard such that no two queens threaten each other.
  - It is solved using backtracking, where we place a queen in one row and then recursively try to place the next queen.
  - The time complexity of this algorithm can be exponential.

### Travelling Salesman Problem & Time Complexity
- **Key Concepts:**
  - This problem involves finding the shortest possible route that visits each city exactly once and returns to the origin city.
  - It is NP-hard, meaning no known polynomial-time solution exists for large instances.
  - Various heuristic algorithms like nearest neighbor or genetic algorithms are used to find approximate solutions.

### Floyd-Warshall Algorithm (or) All Pair Shortest Path Algorithm
- **Key Concepts:**
  - This algorithm finds the shortest paths between all pairs of vertices in a weighted graph.
  - It is particularly useful for dense graphs where many edges exist.
  - The time complexity of this algorithm is \(O(V^3)\), where \(V\) is the number of vertices.

### Randomized [[Quick Sort]] [[Complexity Analysis]]
- **Key Concepts:**
  - Quick sort is an efficient sorting algorithm based on divide-and-conquer strategy.
  - It uses a pivot element to partition the array into two subarrays, one with elements less than the pivot and another with elements greater than or equal to the pivot.
  - The average time complexity of randomized quicksort is \(O(n \log n)\), but in the worst case it can degrade to \(O(n^2)\).

### Depth First Search
- **Key Concepts:**
  - DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking.
  - It uses recursion and stack data structures for implementation.
  - The time complexity of DFS is \(O(V + E)\), where \(V\) is the number of vertices and \(E\) is the number of edges.

### String Matching Algorithm
- **Key Concepts:**
  - This problem involves finding all occurrences of a pattern within a text string.
  - Various algorithms like Knuth-Morris-Pratt (KMP) or Boyer-Moore can be used for efficient matching.
  - The time complexity of KMP algorithm is \(O(m + n)\), where \(m\) and \(n\) are the lengths of the pattern and text, respectively.

### [[Insertion Sort]]
- **Key Concepts:**
  - Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
  - It works by iterating through the list and inserting each element into its correct position in the already sorted part of the list.
  - The average and worst-case time complexity of insertion sort is \(O(n^2)\).

### [[Asymptotic Notation]]
- **Key Concepts:**
  - Asymptotic notation provides a way to describe the performance or running time of an algorithm as the input size grows.
  - Common notations include Big O (upper bound), Omega (\(\Omega\)) (lower bound), and Theta (\(\Theta\)) (tight bound).

### Closest Pair Point
- **Key Concepts:**
  - This problem involves finding two points in a set of given points that are closest to each other.
  - It can be solved using various algorithms like the divide-and-conquer approach or brute-force method.

```

## Connected Notes

- [[Complexity Analysis]]
- [[Dynamic Programming]]
- [[Searching Techniques]]
- [[Binary Search Time Complexities]]
- [[Hiring Problem]]
- [[Insertion Sort]]
- [[Merge Sort]]
- [[Pattern Matching]]
- [[Quick Sort]]
- [[Sequential Sort]]
- [[Asymptotic Notation]]
- [[Matrix Chain Multiplication]]
