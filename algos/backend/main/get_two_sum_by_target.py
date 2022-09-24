from typing import List


class Solution(object):

    @classmethod
    def two_sum(cls, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    @classmethod
    def two_sum_brute_force(cls, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    @classmethod
    def two_sum_one_pass(cls, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

    @classmethod
    def two_sum_enumerate(cls, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining not in seen:
                seen[num] = i
            else:
                return [seen[remaining], i]


if __name__ == '__main__':
    print(Solution.two_sum(nums=[3, 4, 5, 6, 7, 8], target=10))
    print(Solution.two_sum_brute_force(nums=[3, 4, 5, 6], target=10))
    print(Solution.two_sum_one_pass(nums=[3, 4, 5, 6], target=10))
    print(Solution.two_sum_enumerate(nums=[3, 4, 5, 6], target=10))