---
title: Sorting Algorithms
tags:
  - DAA
  - Hiring Problem
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

### Sorting Algorithms

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

### [[Pattern Matching]]

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

### Conclusion

This section provides a comprehensive overview of various algorithms and problems. It covers deterministic and randomized approaches to solving hiring problems, sorting algorithms like QuickSort, and efficient pattern matching techniques such as the brute force approach and an optimized naive method. Understanding these concepts is crucial for developing robust solutions to real-world computational challenges.
```

## Connected Notes

- [[Pattern Matching]]
- [[Hiring Problem]]
- [[Overview]]
