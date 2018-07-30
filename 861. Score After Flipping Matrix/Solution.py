class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 首先判断行列是否要转换
        # 按行首必须为1，列中1的个数要大于等于0的个数

        # 行
        for i in range(0, len(A)):
            if A[i][0] == 0:
                for j in range(0, len(A[0])):
                    if A[i][j] == 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0

        # 列
        for i in range(0, len(A[0])):
            count0 = 0
            count1 = 0
            for j in range(0, len(A)):
                if A[j][i] == 0:
                    count0 += 1
                else:
                    count1 += 1
            if count0 > count1:
                for k in range(0, len(A)):
                    if A[k][i] == 0:
                        A[k][i] = 1
                    else:
                        A[k][i] = 0

        # 计算
        sum_count = 0
        for i in range(0, len(A)):
            A[i].reverse()
            for j in range(0, len(A[0])):
                sum_count += A[i][j] * pow(2, j)

        return sum_count


solution = Solution()
print(solution.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
