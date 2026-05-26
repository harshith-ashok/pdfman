---
title: Huffman Coding Using Greedy Approach
tags:
- Algorithms
- Data Compression
- Minimum Spanning Tree (MST)
- Matrix Chain Multiplication
---

## [[Overview]]

This chapter provides a comprehensive overview of various greedy algorithms, including Huffman Coding using the Greedy Approach, [[Minimum Spanning Tree (MST)]], [[Matrix Chain Multiplication]], and Longest Common Subsequence (LCS). Each algorithm is explained in detail with its core principles, step-by-step procedures, complexity analysis, and applications. The chapter aims to provide a thorough reference for understanding these fundamental algorithms.

## Huffman Coding Using Greedy Approach

### Introduction

Huffman coding is a lossless data compression technique that assigns variable-length codes to input characters based on their frequencies. The most frequent character receives the smallest code, and the least frequent character gets the largest code. This approach ensures optimal storage by minimizing overall bit usage.

### The Greedy Principle

The Huffman algorithm employs a greedy strategy of merging the two least frequent elements at each step to build an optimal binary tree (Huffman Tree). By making locally optimal choices, it guarantees globally optimal prefix-free codes that prevent ambiguity during decoding.

### Algorithm Steps

1. **Initialization:** Create a leaf node for each unique character and build a min-heap of all these nodes based on their frequencies.
2. **Merging:** Extract the two least frequent nodes from the heap, combine them into an internal node with a frequency equal to the sum of the two extracted nodes, and insert this new node back into the heap.
3. **Repeat:** Continue merging until only one node remains in the heap. This final node is the root of the Huffman tree.
4. **Code Generation:** Traverse the Huffman Tree from the root to each leaf node, assigning '0' for a left branch and '1' for a right branch.

### [[Complexity Analysis]]

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of unique characters. Building the initial min-heap takes $O(N)$ time. The extract-min operation takes $O(\log N)$ time and is performed $2(N-1)$ times.
- **Space Complexity:** $O(N)$ to store the Huffman tree and the min-heap.

## [[Minimum Spanning Tree (MST)]]

### Introduction

Given a connected, undirected graph with weighted edges, a [[Minimum Spanning Tree (MST)]] is a subgraph that includes all vertices without any cycles, and its total edge weight is minimized. Two primary greedy algorithms are Kruskal's Algorithm and Prim's Algorithm.

### Standard Algorithms

#### Kruskal's Algorithm

Kruskal's algorithm builds the MST by sorting all edges in ascending order of their weights and adding them one by one to the growing forest, provided they do not form a cycle. It utilizes a Disjoint-Set (Union-Find) data structure to detect cycles.

- **Time Complexity:** $O(E \log E)$ or $O(E \log V)$, where $E$ is the number of edges and $V$ is the number of vertices. Sorting the edges dominates the runtime. The Union-Find operations take practically $O(1)$ time with path compression.
- **Space Complexity:** $O(V + E)$ to store the graph and disjoint sets.

#### Prim's Algorithm

Prim's algorithm builds the MST by starting with a single arbitrary vertex and greedily growing the tree. At each step, it selects the edge with the minimum weight that connects a vertex in the tree to a vertex outside the tree. It typically uses a Priority Queue (Min-Heap).

- **Time Complexity:** $O(E \log V)$ using a binary heap, or $O(E + V \log V)$ using a Fibonacci heap.
- **Space Complexity:** $O(V)$ for the priority queue and auxiliary arrays.

## [[Matrix Chain Multiplication]]

### Introduction

Matrix multiplication is associative, but the order in which matrices are multiplied significantly affects the number of scalar multiplications required. The [[Matrix Chain Multiplication]] problem seeks the most efficient parenthesis arrangement to minimize the total number of scalar multiplications needed.

### [[Dynamic Programming]] Approach

This problem cannot be solved with a greedy approach; it requires [[Dynamic Programming]] because it exhibits optimal substructure and overlapping subproblems.

Let the matrix chain be $A_1, A_2, \dots, A_n$, where matrix $A_i$ has dimensions $p_{i-1} \times p_i$. The goal is to find the minimum number of scalar multiplications needed to compute the product $A_1 \times A_2 \times \cdots \times A_n$.

### Recurrence Relation

Let $m[i, j]$ be the minimum number of scalar multiplications needed to compute the matrix $A_{i..j}$.

- If $i = j$, $m[i, j] = 0$ (a single matrix requires no multiplication).
- If $i < j$, we test all possible split points $k$ (where $i \le k < j$). The cost is the sum of:
    - The cost of multiplying the left subchain: $m[i][k]$.
    - The cost of multiplying the right subchain: $m[k+1][j]$.
    - The cost of multiplying the two resulting matrices: $p_{i-1} p_k p_j$.

The recurrence relation is:
$$m[i, j] = \min_{i \le k < j} (m[i, k] + m[k+1, j] + p_{i-1}p_k p_j)$$
```

## Connected Notes

- [[Matrix Chain Multiplication]]
- [[Backtracking Approach for Solving Problems]]
- [[Complexity Analysis]]
- [[Dynamic Programming]]
- [[Minimum Spanning Tree (MST)]]
- [[Overview]]
