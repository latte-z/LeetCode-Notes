class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 首先水平翻转
        for i in range(0, len(A)):
            tmp = []
            # range (i,j) => [i,j) => 如果是倒着的需要制定步进为-1
            for j in range(len(A[0]) - 1, -1, -1):
                tmp.append(A[i][j])
            A[i] = tmp

        # 再进行图片反转
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A


solution = Solution()
print(solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
