class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bin_count = []
        for i in range(0, num + 1):
            count = 0
            while i != 0:
                s = i % 2
                if s == 1:
                    count += 1
                # 记得使用地板除法
                i = i // 2
            bin_count.append(count)
        return bin_count


solution = Solution()
print(solution.countBits(5))
