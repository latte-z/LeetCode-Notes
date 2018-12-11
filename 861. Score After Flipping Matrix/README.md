### [861\. Score After Flipping Matrix](https://leetcode-cn.com/problems/score-after-flipping-matrix/description/)

题目难度： **中等**



We have a two dimensional matrix `A` where each value is `0` or `1`.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all `0`s to `1`s, and all `1`s to `0`s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.



**Example 1:**

```
**Input:** <span id="example-input-1-1" style="display: inline;">[[0,0,1,1],[1,0,1,0],[1,1,0,0]]</span>
**Output:** <span id="example-output-1" style="display: inline;">39</span>
**Explanation:** Toggled to <span id="example-input-1-1" style="display: inline;">[[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</span>```

**Note:**

1.  `1 <= A.length <= 20`
2.  `1 <= A[0].length <= 20`
3.  `A[i][j]` is `0` or `1`.