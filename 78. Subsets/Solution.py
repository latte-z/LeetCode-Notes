class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        subsets = []
        first_elt = nums[0]
        rest_list = nums[1:]

        for partial_subset in self.subsets(rest_list):
            # 切分成原始partial的subset和包含first_elt的subset
            subsets.append(partial_subset)
            # =partial_subset和=partial_subset[:]的区别是：
            # 前者是指向同一个内存地址，后一个是复制内容指向新地址
            # Python没有赋值，只有名字到对象的绑定
            next_subset = partial_subset[:] + [first_elt]
            subsets.append(next_subset)
        return subsets


solution = Solution()
print(solution.subsets([1, 2, 3]))
