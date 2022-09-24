from typing import Dict
from collections import Counter


class Solution(object):

    @classmethod
    def get_most_seen_char(cls, word: str) -> Dict:
        # Building Map of counters
        char_to_times: Dict[str, int] = {}
        for char in word:
            if char not in char_to_times:
                char_to_times[char] = 1
            else:
                char_to_times[char] += 1
        return char_to_times

    @classmethod
    def get_most_seen_char_one(cls, word: str):
        char_to_times: Dict[str, int] = {}
        for char in word:
            char_to_times[char] = char_to_times.get(char, 0) + 1
        return char_to_times

    @classmethod
    def get_most_seen_char_two(cls, word: str) -> Dict:
        char_to_times = Counter(word)
        return char_to_times

    @classmethod
    def get_most_seen_char_third(cls, word: str):
        # Getting the most frequency char
        char_to_times: Dict[str, int] = {}
        result: str = word[0]
        max_time: int = char_to_times[result]
        for char, time in char_to_times.items():
            if time > max_time:
                max_time = time
                result = char
        return result


if __name__ == '__main__':
    print(Solution.get_most_seen_char('aaacfvfvfvfdsdfvfb'))
    print(Solution.get_most_seen_char_one('aaacfvfvfvfdsdfvfb'))
    print(Solution.get_most_seen_char_two('aaacfvfvfvfdsdfvfb'))
# BUG    print(Solution.get_most_seen_char_third('aaacfvfvfvfdsdfvfb'))