class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return None
        cur_pos = 0
        while cur_pos < length:
            if A[cur_pos] < A[cur_pos + 1]:
                cur_pos += 1
            elif A[cur_pos] > A[cur_pos + 1]:
                peak_point = cur_pos
                for i in range(cur_pos, len(A) - 1):
                    if A[i + 1] > A[i]:
                        return None
                if A[len(A) - 1] > A[len(A) - 2]:
                    return None
                return peak_point


if __name__ == '__main__':
    solution = Solution()
    solution.peakIndexInMountainArray([0, 2, 1, 0])
