
class Solution(object):
    @classmethod
    def print_pyramid(cls, size: int):
        for i in range(size + 1):
            print(' ' * (size - i), end='')
            print('* ' * (i * 2 - i))
        for i in range(size - 1, 0, -1):
            print(' ' * (size - i), end='')
            print('* ' * (i * 2 - i))


if __name__ == '__main__':
    Solution.print_pyramid(size=5)