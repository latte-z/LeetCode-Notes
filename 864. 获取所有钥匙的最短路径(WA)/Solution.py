import sys

sys.setrecursionlimit(5000)


class Solution:
    house_map = []
    key_num = 0
    key_list = []
    # 定义上下左右行进
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    result_list = []

    def init_grid(self, grid):
        for i in range(0, len(grid)):
            temp_list = list(grid[i])
            self.house_map.append([])
            for j in range(0, len(temp_list)):
                # 记录key数量和list
                if str(temp_list[j]).islower():
                    self.key_num += 1
                    self.key_list.append(temp_list[j])
                self.house_map[i].append(temp_list[j])

    def get_key(self, cur_key_num, step_num, cur_x, cur_y, found_key_list, last_x, last_y):
        if cur_key_num == self.key_num:
            temp_step_num = step_num
            self.result_list.append(temp_step_num)
            print(self.result_list)
        else:
            for i in range(0, 4):
                next_x = cur_x + self.move_x[i]
                next_y = cur_y + self.move_y[i]
                if 0 <= next_x <= 2 and 0 <= next_y <= 4:
                    next_step = self.house_map[next_x][next_y]
                    if next_step != '#' and not (next_x == last_x and next_y == last_y):
                        last_x = cur_x
                        last_y = cur_y
                        if str(next_step).islower() and next_step not in found_key_list:
                            found_key_list.append(str(next_step))
                            self.get_key(cur_key_num + 1, step_num + 1, next_x, next_y, found_key_list, last_x, last_y)
                        elif str(next_step).isupper() and str(next_step).lower() in found_key_list:
                            self.get_key(cur_key_num, step_num + 1, next_x, next_y, found_key_list, last_x, last_y)
                        else:
                            self.get_key(cur_key_num, step_num + 1, next_x, next_y, found_key_list, last_x, last_y)
        return

    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        self.init_grid(grid)
        start_x = 0
        start_y = 0
        found_list = []
        self.get_key(0, 0, start_x, start_y, found_list, -1, -1)
        sorted(self.result_list)
        return self.result_list[0] if len(self.result_list) > 0 else -1


if __name__ == '__main__':
    solution = Solution()
    solution.shortestPathAllKeys(grid=["@.a.#", "###.#", "b.A.B"])
