class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        # 转制矩阵后找列最大的
        trans_grid = list(map(list, zip(*A)))
        return trans_grid


solution = Solution()
print(solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
