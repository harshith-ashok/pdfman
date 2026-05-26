---
title: Pattern Matching
tags:
  - DAA NOTES UNIT 5
  - Hiring Problem
  - Sorting Algorithms
  - Pattern Matching
---

## [[Overview]]

This section provides an overview of the various algorithms and problems discussed, including deterministic and randomized approaches. It covers topics such as hiring problems, sorting algorithms like QuickSort, and pattern matching in strings.

### [[Hiring Problem]]

#### Deterministic Approach
- **Algorithm**: The deterministic approach involves interviewing candidates sequentially until a suitable candidate is found.
  - **Advantages**:
    - Simple and straightforward.
    - Fast with high probability of producing an optimal output.
  - **Disadvantages**:
    - More costly than interviews, as each interview is expensive.

#### [[Hiring Problem]]: Hire Assistant
- **Algorithm**: The Hire Assistant algorithm randomly selects candidates for evaluation without considering their order. After viewing a candidate, the system ranks them based on qualifications and decides which one to hire.
  - **Advantages**:
    - Simple and easy to implement.
    - Provides a ranked list of candidates.

### [[Sorting Algorithms]]

#### QuickSort
- **Algorithm**: QuickSort is a divide-and-conquer algorithm that recursively partitions an array into two subarrays around a pivot element. The process continues until the base case (an empty or single-element array) is reached.
  - **Best Case Complexity**:
    - \(O(n \log n)\)
  - **Worst Case Complexity**:
    - \(O(n^2)\)

#### Randomized QuickSort
- **Algorithm**: To improve performance, QuickSort can be randomized by selecting a random pivot element. This helps in avoiding the worst-case scenario where the array is already sorted or nearly sorted.
  - **Advantages**:
    - Can handle data that is not perfectly sorted efficiently.

### Pattern Matching

#### Brute Force Approach
- **Algorithm**: The brute force approach involves checking each substring of a given text to see if it matches the pattern. This method has an \(O(m \times n)\) time complexity, where \(m\) and \(n\) are the lengths of the pattern and text respectively.
  - **Example**:
    ```plaintext
    Pattern: "abc"
    Text:     "abracadabra"
    ```
    In this example, the algorithm would check each substring of length 3 in the text to see if it matches "abc".

#### Efficient Approach (Naive)
- **Algorithm**: An efficient approach involves using a two-pointer technique where one pointer traverses the pattern and another traverses the text. This method has an \(O(m + n)\) time complexity.
  - **Example**:
    ```plaintext
    Pattern: "abc"
    Text:     "abracadabra"
    ```
    In this example, the algorithm would compare each character of the pattern with the corresponding characters in the text.

### Full Approach: Rabin-Karp String Matching

The Rabin-Karp algorithm is designed for efficiently searching patterns within strings. This section will detail how it works by comparing a sliding window approach with the more efficient pattern matching method used in the Rabin-Karp algorithm.

#### Detailed Explanation of Pattern Matching Approaches
- **Naive Approach**
  - **Step-by-step comparison**: For every position in the main string, compare a window of characters with the pattern.
  - **Mismatch handling**: If there's a mismatch at any point, shift the window one character to the right and continue comparing until either a match is found or the end of the string is reached.

- **Rabin-Karp Approach**
  - **Hash Calculation**: Compute a hash value for both the main string and the pattern.
  - **Window Sliding**: Slide a window across the main string, computing the hash of each window.
  - **Comparison**: Compare the hash values of the current window with the pattern's hash value.
  - **Mismatches Handling**: If there’s a mismatch, adjust the window by sliding it one character to the right and recalculating the hash.

#### Rabin-Karp [[Algorithm Implementation]]
- **Hash Calculation**
  - Use a prime number for hashing to ensure collisions are minimized.

## Connected Notes

- [[Hiring Problem]]
- [[Sorting Algorithms]]
- [[Binary Search Time Complexities]]
- [[Complexity Analysis]]
- [[Dynamic Programming]]
- [[Graph Theory Applications]]
- [[Insertion Sort]]
- [[Merge Sort]]
- [[Quick Sort]]
- [[Searching Techniques]]
- [[Algorithm Implementation]]
- [[Overview]]
