## 1. Huffman Coding Using Greedy Approach

### 1.1 Introduction

Huffman coding is a lossless data compression algorithm. The core idea is to assign variable-length codes to input characters, with lengths based on the frequencies of the corresponding characters. The most frequent character gets the smallest code and the least frequent character gets the largest code, optimizing overall storage.

### 1.2 The Greedy Principle

The algorithm employs a greedy strategy by continually merging the two least frequent elements. By making the locally optimal choice (combining the two lowest frequencies) at each step, it builds a strictly binary tree (Huffman Tree) that guarantees a globally optimal prefix-free code. A prefix-free code ensures that no code is a prefix of another, preventing ambiguity during decoding.

### 1.3 Algorithm Steps

1. Create a leaf node for each unique character and build a min-heap of all leaf nodes based on their frequencies.
    
2. Extract the two nodes with the minimum frequency from the min-heap.
    
3. Create a new internal node with a frequency equal to the sum of the two extracted nodes. Make the first extracted node the left child and the second extracted node the right child.
    
4. Insert this new node back into the min-heap.
    
5. Repeat steps 2-4 until the heap contains only one node. The remaining node is the root of the Huffman tree.
    
6. Traverse the tree to generate codes: assign '0' for a left branch and '1' for a right branch.
    

### 1.4 Complexity Analysis

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of unique characters. Building the initial min-heap takes $O(N)$ time. The extract-min operation takes $O(\log N)$ time, and it is performed $2(N-1)$ times.
    
- **Space Complexity:** $O(N)$ to store the Huffman tree and the min-heap.
    

---

## 2. Minimum Spanning Tree (MST)

### 2.1 Introduction

Given a connected, undirected graph with weighted edges, a Spanning Tree is a subgraph that includes all vertices of the original graph without any cycles. A Minimum Spanning Tree (MST) is the spanning tree where the sum of the edge weights is minimized.

### 2.2 Standard Algorithms

The two primary greedy algorithms for finding an MST are Kruskal's Algorithm and Prim's Algorithm.

#### 2.2.1 Kruskal's Algorithm

Kruskal's algorithm builds the MST by sorting all edges in ascending order of their weight and adding them one by one to the growing forest, provided they do not form a cycle. It utilizes a Disjoint-Set (Union-Find) data structure to detect cycles.

- **Time Complexity:** $O(E \log E)$ or $O(E \log V)$, where $E$ is the number of edges and $V$ is the number of vertices. Sorting the edges dominates the runtime. The Union-Find operations take practically $O(1)$ time with path compression.
    
- **Space Complexity:** $O(V + E)$ to store the graph and disjoint sets.
    

#### 2.2.2 Prim's Algorithm

Prim's algorithm builds the MST by starting with a single arbitrary vertex and greedily growing the tree. At each step, it selects the edge with the minimum weight that connects a vertex in the tree to a vertex outside the tree. It typically uses a Priority Queue (Min-Heap).

- **Time Complexity:** $O(E \log V)$ using a binary heap, or $O(E + V \log V)$ using a Fibonacci heap.
    
- **Space Complexity:** $O(V)$ for the priority queue and auxiliary arrays.
    

---

## 3. Matrix Chain Multiplication

### 3.1 Introduction

Matrix multiplication is associative, meaning $(A \times B) \times C = A \times (B \times C)$. However, the order in which matrices are multiplied drastically affects the number of scalar multiplications required. The Matrix Chain Multiplication problem seeks the most efficient parenthesis arrangement to multiply a sequence of matrices.

### 3.2 Dynamic Programming Approach

This problem cannot be solved with a greedy approach; it requires Dynamic Programming because it exhibits optimal substructure and overlapping subproblems.

Let the matrix chain be $A_1, A_2, \dots, A_n$, where matrix $A_i$ has dimensions $p_{i-1} \times p_i$.

### 3.3 Recurrence Relation

Let $m[i, j]$ be the minimum number of scalar multiplications needed to compute the matrix $A_{i..j}$.

- If $i = j$, $m[i, j] = 0$ (a single matrix requires no multiplication).
    
- If $i < j$, we test all possible split points $k$ (where $i \le k < j$).
    
    The cost is the cost of multiplying the left subchain, plus the right subchain, plus the cost of multiplying the two resulting matrices:
    
    $$m[i, j] = \min_{i \le k < j} (m[i, k] + m[k+1, j] + p_{i-1}p_k p_j)$$
    

### 3.4 Complexity Analysis

- **Time Complexity:** $O(N^3)$. There are $O(N^2)$ entries in the DP table to fill, and computing each entry requires $O(N)$ time to test all possible values of $k$.
    
- **Space Complexity:** $O(N^2)$ to store the DP table $m[i, j]$ and a secondary table $s[i, j]$ to reconstruct the optimal parenthesization.
    

---

## 4. Longest Common Subsequence (LCS)

### 4.1 Introduction

A subsequence is a sequence that appears in the same relative order, but not necessarily contiguously. The Longest Common Subsequence problem involves finding the longest sequence which is a subsequence of all sequences in a set (usually two strings).

### 4.2 Dynamic Programming Principle

Given two sequences $X$ of length $M$ and $Y$ of length $N$, we build a 2D table $L[0..M][0..N]$ where $L[i][j]$ contains the length of the LCS of $X[0..i-1]$ and $Y[0..j-1]$.

### 4.3 Recurrence Relation

- If $i = 0$ or $j = 0$, $L[i][j] = 0$ (base case: empty string).
    
- If $X[i-1] == Y[j-1]$, then the characters match, and we add 1 to the result of the remaining strings:
    
    $$L[i][j] = L[i-1][j-1] + 1$$
    
- If $X[i-1] \neq Y[j-1]$, we take the maximum of the LCS formed by excluding the current character of $X$ or the current character of $Y$:
    
    $$L[i][j] = \max(L[i-1][j], L[i][j-1])$$
    

### 4.4 Complexity Analysis

- **Time Complexity:** $O(M \times N)$, as we populate a table of size $M \times N$ and each entry takes $O(1)$ time to compute.
    
- **Space Complexity:** $O(M \times N)$ to store the DP table. This can be optimized to $O(\min(M, N))$ if only the length of the LCS is required, by storing only the previous row.
    

---

## 5. N-Queen's Problem Using Backtracking

### 5.1 Introduction

The N-Queen problem requires placing $N$ chess queens on an $N \times N$ chessboard such that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

### 5.2 Backtracking Approach

Backtracking is a systematic way to iterate through all the possible configurations of a search space.

1. Start in the leftmost column.
    
2. If all queens are placed, return true.
    
3. Try all rows in the current column. For each row:
    
    - Check if the queen can be placed safely (no queens in the same row, upper-left diagonal, or lower-left diagonal).
        
    - If safe, place the queen and recursively check if this leads to a solution.
        
    - If placing the queen leads to a solution, return true.
        
    - If it does not lead to a solution, unmark the cell (backtrack) and try the next row.
        
4. If all rows have been tried and nothing worked, return false to trigger backtracking in the previous column.
    

### 5.3 Complexity Analysis

- **Time Complexity:** $O(N!)$. In the worst case, we are placing queens row by row. For the first row, we have $N$ choices, for the second $N-1$, and so on. Bounding operations reduce practical time, but the upper bound remains factorial.
    
- **Space Complexity:** $O(N)$ for the recursion stack and the arrays used to keep track of the board state (rows, columns, and diagonals).
    

---

## 6. Travelling Salesman Problem (TSP)

### 6.1 Introduction

Given a list of cities and the distances between each pair of cities, the Travelling Salesman Problem asks: "What is the shortest possible route that visits each city exactly once and returns to the origin city?" It is an NP-Hard problem.

### 6.2 Dynamic Programming (Held-Karp Algorithm)

A naive permutation approach generates all $(N-1)!$ routes, which is computationally infeasible for large $N$. The Held-Karp algorithm uses Dynamic Programming to reduce this complexity.

Let $S$ be a subset of vertices excluding the start vertex (say, vertex 0). Let $cost(i, S)$ be the minimum cost path starting at vertex $i$, visiting all vertices in $S$ exactly once, and ending at vertex 0.

### 6.3 Recurrence Relation

- Base Case: $cost(i, \emptyset) = distance(i, 0)$
    
- Recursive Step:
    
    $$cost(i, S) = \min_{j \in S} \left( distance(i, j) + cost(j, S - \{j\}) \right)$$
    
    To find the optimal tour, we evaluate $cost(0, V - \{0\})$.
    

### 6.4 Complexity Analysis

- **Time Complexity:** $O(N^2 2^N)$. There are $N \cdot 2^N$ subproblems (states defined by the current city and the subset of visited cities), and computing each state takes $O(N)$ time.
    
- **Space Complexity:** $O(N 2^N)$ to store the memoization table mapping subsets to minimum costs.
    

---

## 7. Floyd-Warshall Algorithm

### 7.1 Introduction

The Floyd-Warshall algorithm solves the All-Pairs Shortest Path problem. Given a directed graph with edge weights, it finds the shortest paths between all pairs of vertices. It can handle negative weight edges, provided there are no negative weight cycles.

### 7.2 Dynamic Programming Principle

The algorithm considers all vertices one by one as an intermediate vertex. For every pair of vertices $(i, j)$, it checks if passing through the current intermediate vertex $k$ yields a shorter path than the previously known shortest path.

### 7.3 Recurrence Relation

Let $D^{(k)}[i][j]$ be the shortest path from $i$ to $j$ using only vertices from $\{1, 2, \dots, k\}$ as intermediate vertices.

$$D^{(k)}[i][j] = \min(D^{(k-1)}[i][j], D^{(k-1)}[i][k] + D^{(k-1)}[k][j])$$

The algorithm builds matrices from $D^{(0)}$ (the adjacency matrix) up to $D^{(V)}$.

### 7.4 Complexity Analysis

- **Time Complexity:** $O(V^3)$, where $V$ is the number of vertices. The algorithm utilizes three nested loops: the outermost for the intermediate vertex $k$, and the inner two for the start vertex $i$ and end vertex $j$.
    
- **Space Complexity:** $O(V^2)$ to store the 2D distance matrix. We can do this in-place, overwriting the matrix, so we do not need $V$ different matrices.
    

---

## 8. Randomized Quick Sort Complexity Analysis

### 8.1 Introduction

Standard Quick Sort partitions an array around a pivot element. If the array is already sorted and the pivot is chosen poorly (e.g., always the first or last element), it degenerates to quadratic time. Randomized Quick Sort mitigates this by picking a pivot uniformly at random from the subarray, ensuring that bad splits are extremely rare regardless of the input distribution.

### 8.2 Expected Time Complexity Analysis

To analyze the expected time complexity, we count the expected number of comparisons. Let $z_1, z_2, \dots, z_n$ be the elements of the array in sorted order.

Let $X_{ij}$ be an indicator random variable where $X_{ij} = 1$ if $z_i$ and $z_j$ are compared during execution, and $0$ otherwise.

Total comparisons $X = \sum_{i=1}^{n-1} \sum_{j=i+1}^n X_{ij}$.

Elements $z_i$ and $z_j$ are compared if and only if either $z_i$ or $z_j$ is chosen as a pivot before any element between them. The number of elements in the set $\{z_i, z_{i+1}, \dots, z_j\}$ is $j - i + 1$. Since pivots are chosen randomly, the probability that $z_i$ or $z_j$ is the first pivot chosen from this set is:

$$P(X_{ij} = 1) = \frac{2}{j - i + 1}$$

Taking the expectation:

$$E[X] = \sum_{i=1}^{n-1} \sum_{j=i+1}^n \frac{2}{j - i + 1}$$

Let $k = j - i + 1$. The sum reduces to bounded harmonic series:

$$E[X] \le 2n \sum_{k=1}^n \frac{1}{k} \approx 2n \ln n$$

Thus, the **Expected Time Complexity is $O(N \log N)$**.

### 8.3 Worst-Case Complexity

- **Time Complexity:** $O(N^2)$. This occurs if the random number generator consistently picks the maximum or minimum element as the pivot, leading to partitions of size $1$ and $N-1$. However, the probability of this occurring is infinitesimal for large $N$.
    
- **Space Complexity:** Expected $O(\log N)$ for the recursion stack. Worst-case is $O(N)$.
    

---

## 9. Depth First Search (DFS)

### 9.1 Introduction

Depth First Search is a fundamental algorithm for traversing or searching tree or graph data structures. It starts at a source node and explores as far as possible along each branch before backtracking.

### 9.2 Algorithmic Principle

DFS uses a Stack data structure (either explicitly or implicitly via the call stack in recursion).

1. Mark the current node as visited.
    
2. Explore all adjacent unvisited nodes recursively.
    
3. Once all adjacent nodes are visited, backtrack to the previous node.
    
    DFS is often augmented to record "discovery time" (when a node is first visited) and "finish time" (when all its descendants have been visited), which is vital for applications like Topological Sorting and finding Strongly Connected Components.
    

### 9.3 Complexity Analysis

- **Time Complexity:** $O(V + E)$ for an adjacency list representation. The algorithm visits every vertex exactly once ($O(V)$) and examines every edge exactly once in a directed graph or twice in an undirected graph ($O(E)$). If an adjacency matrix is used, the time complexity is $O(V^2)$.
    
- **Space Complexity:** $O(V)$ in the worst case. This accounts for the visited array and the recursion stack. If the graph is a linear chain, the recursion depth will be $V$.
    

---

## 10. String Matching Algorithm (Knuth-Morris-Pratt)

### 10.1 Introduction

String matching algorithms aim to find occurrences of a "pattern" string within a larger "text" string. While the Naive approach takes $O(N \times M)$ time by shifting the pattern one character at a time upon a mismatch, advanced algorithms like Knuth-Morris-Pratt (KMP) optimize this process.

### 10.2 The KMP Algorithm Principle

The KMP algorithm utilizes the property that when a mismatch occurs, the pattern itself contains enough information to determine where the next match could begin, bypassing redundant character checks.

It pre-processes the pattern to construct a Longest Prefix Suffix (LPS) array of length $M$. The $LPS[i]$ stores the length of the longest proper prefix of $pattern[0..i]$ which is also a suffix of $pattern[0..i]$.

### 10.3 Algorithm Steps

1. **Compute LPS Array:** Traverse the pattern. If characters match, increment the length of the prefix-suffix. If they mismatch, use the previously computed LPS values to fall back without starting over.
    
2. **Search Process:** Iterate through the text.
    
    - If text and pattern characters match, advance both pointers.
        
    - If a mismatch occurs after some matches, do not backtrack the text pointer. Instead, use the LPS array to shift the pattern pointer: $pattern\_index = LPS[pattern\_index - 1]$.
        
    - If an exact match of the entire pattern is found, record the index and shift the pattern using the LPS array to find overlapping occurrences.
        

### 10.4 Complexity Analysis

- **Time Complexity:** $O(N + M)$, where $N$ is the length of the text and $M$ is the length of the pattern. Preprocessing takes $O(M)$ time. The searching phase takes $O(N)$ time because the text pointer never moves backward.
    
- **Space Complexity:** $O(M)$ to store the LPS array based on the pattern length.