class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        def trans_to_binary(num):
            bin_list = []
            while num != 0:
                bin_list.append(0) if num % 2 == 0 else bin_list.append(1)
                num //= 2
            return bin_list

        x_list = trans_to_binary(x)
        y_list = trans_to_binary(y)
        len_x = len(x_list)
        len_y = len(y_list)
        hamming_distance = 0
        if len_x >= len_y:
            for i in range(0, len_x - len_y):
                y_list.append(0)
        else:
            for i in range(0, len_y - len_x):
                x_list.append(0)
        if len_x >= len_y:
            for i in range(0, len_x):
                if x_list[i] != y_list[i]:
                    hamming_distance += 1
        else:
            for i in range(0, len_y):
                if x_list[i] != y_list[i]:
                    hamming_distance += 1
        return hamming_distance


if __name__ == '__main__':
    solution = Solution()
    solution.hammingDistance(1, 4)
