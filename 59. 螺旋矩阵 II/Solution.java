//
// Created by Ryan Shen on 2018-12-07.
//

class Solution {
    public int[][] generateMatrix(int n) {
        // n偶数的时候正好n/2个环
        // n为奇数时和下一个偶数一样的环数，单独补一个vector[n/2][n/2]
        int[][] matrix = new int[n][n];
        int num = 1;
        // 按环数量循环
        for (int i=0;i<n/2;i++) {
            // 上边
            for (int j=i;j<n-i-1;j++) {
                matrix[i][j] = num++;
            }
            // 右边
            for (int j=i;j<n-i-1;j++) {
                matrix[j][n-i-1] = num++;
            }
            // 下边
            for (int j=n-i-1;j>i;j--) {
                matrix[n-i-1][j] = num++;
            }
            // 左边
            for (int j=n-i-1;j>i;j--) {
                matrix[j][i] = num++;
            }
        }
        if (n%2==1)
            matrix[n/2][n/2] = num;
        return matrix;
    }
}