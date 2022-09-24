from typing import List


class Solution(object):

    @classmethod
    def get_max(cls, numbers: List[int]):
        biggest: int = numbers[0]
        for num in numbers:
            if num > biggest:
                biggest = num
        print(biggest)


if __name__ == '__main__':
    Solution.get_max([1, 2, 3, 4])