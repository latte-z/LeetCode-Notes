class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start_x = 0
    start_y = 0

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cur_x = self.start_x
        cur_y = self.start_y
        move_list = list(moves)
        for move in move_list:
            if move == 'U':
                cur_x += self.dx[0]
                cur_y += self.dy[0]
            elif move == 'D':
                cur_x += self.dx[1]
                cur_y += self.dy[1]
            elif move == 'L':
                cur_x += self.dx[2]
                cur_y += self.dy[2]
            else:
                cur_x += self.dx[3]
                cur_y += self.dy[3]
        if cur_x == self.start_x and cur_y == self.start_y:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeCircle("UD"))
