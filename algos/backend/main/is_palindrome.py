class Solution(object):

    @classmethod
    def is_num_pali(cls, num: int):
        # num = int(input("Enter side number:"))
        temp = num
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
        if temp == rev:
            print("The number is palindrome!")
        else:
            print("The number isn't palindrome!")

    @classmethod
    def is_str_pali(cls, word: str) -> bool:
        if word == word[::-1]:
            return True
        return False

    @classmethod
    def short(cls, x: int):
        return False if x < 0 else x == int(str(x)[::-1])


if __name__ == '__main__':
    Solution.is_num_pali(num=13195)
    print(Solution.is_str_pali('aaaad'))
    print(Solution.short(x=123421))
