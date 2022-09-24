
class Solution(object):
    @classmethod
    def laziness(cls, n):
        yield n
        yield from cls.laziness(n + 1)

    @classmethod
    def sieve(cls, ss: int):
        n = next(ss)
        yield n
        yield from cls.sieve(i for i in ss if i % n == 0)


if __name__ == '__main__':
    print(next(Solution.laziness(2)))
    s = Solution.laziness(n=3)
    print(next(s))
    print(next(s))
    print(next(s))
    p = Solution.sieve(ss=2)
    print(next(p))
