
class Solution(object):

    @classmethod
    def fizz_buzz_game(cls):
        print(*map(lambda i: 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i,
                   range(1, 101)),
              sep='\n')

    @classmethod
    def fizz_buzz_game_one(cls):
        for num in range(1, 101):
            put_txt_instead = ''
            if num % 3 == 0:
                put_txt_instead += 'Fizz'
            if num % 5 == 0:
                put_txt_instead += 'Buzz'
            if num % 5 != 0 and num % 3 != 0:
                put_txt_instead += str(num)
            print(put_txt_instead)
            print(put_txt_instead or num)

    @classmethod
    def fizz_buzz_game_two(cls):
        for num in range(1, 101):
            fizz = 'Fizz' if num % 3 == 0 else ''
            buzz = 'Buzz' if num % 5 == 0 else ''
            print(f'{fizz}{buzz}' or num)


if __name__ == '__main__':
    print(Solution.fizz_buzz_game())
    print(Solution.fizz_buzz_game_one())
    print(Solution.fizz_buzz_game_two())