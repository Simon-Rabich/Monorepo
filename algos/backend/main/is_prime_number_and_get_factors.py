
class Solution(object):
    @classmethod
    def is_prime_number(cls, number: int) -> int:
        for num in range(2, number):
            if number % num == 0:
                return False
            return True

    @classmethod
    def get_prime_factors(cls, number: int) -> int:
        for num in range(2, number):
            if number % num == 0:
                if cls.is_prime_number(num):
                    print(num)


if __name__ == '__main__':
    print(Solution.is_prime_number(number=1015))
    print(Solution.get_prime_factors(number=13195))