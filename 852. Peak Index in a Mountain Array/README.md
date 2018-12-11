### [852\. Peak Index in a Mountain Array](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/description/)

题目难度： **简单**



Let's call an array `A` a _mountain_ if the following properties hold:

*   `A.length >= 3`
*   There exists some `0 < i < A.length - 1` such that `A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`

Given an array that is definitely a mountain, return any `i` such that `A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`.

**Example 1:**

```
**Input:** <span id="example-input-1-1" style="display: inline;">[0,1,0]</span>
**Output:** <span id="example-output-1" style="display: inline;">1</span>
```



**Example 2:**

```
**Input:** <span id="example-input-2-1" style="display: inline;">[0,2,1,0]</span>
**Output:** <span id="example-output-2" style="display: inline;">1</span>```



**Note:**

1.  `3 <= A.length <= 10000`
2.  <font face="monospace" style="display: inline;">0 <= A[i] <= 10^6</font>
3.  A is a mountain, as defined above.