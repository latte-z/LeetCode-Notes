class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_list = list(J)
        count = 0
        for jewel in jewel_list:
            count += S.count(jewel)
        return count


solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))
