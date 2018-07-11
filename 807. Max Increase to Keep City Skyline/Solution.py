class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_length = len(grid[0])
        grid_height = len(grid)
        horizon_max = [0] * grid_length
        vertical_max = [0] * grid_height

        # 遍历找每行中最大的
        for i in range(0, grid_height):
            for j in range(0, grid_length):
                if grid[i][j] > horizon_max[i]:
                    horizon_max[i] = grid[i][j]

        # 转制矩阵后找列最大的
        trans_grid = list(map(list, zip(*grid)))
        for i in range(0, grid_length):
            for j in range(0, grid_height):
                if trans_grid[i][j] > vertical_max[i]:
                    vertical_max[i] = trans_grid[i][j]

        # 对建筑进行增高并计算总和
        count = 0
        for i in range(0, grid_height):
            for j in range(0, grid_length):
                if grid[i][j] != horizon_max[j] or grid[i][j] != vertical_max[i]:
                    tmp_max = vertical_max[i] if vertical_max[i] < horizon_max[j] else horizon_max[j]
                    count += (tmp_max - grid[i][j])
                    grid[i][j] = tmp_max

        return count


solution = Solution()
print(solution.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
