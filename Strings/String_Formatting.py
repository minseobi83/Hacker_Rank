# https://www.hackerrank.com/challenges/python-string-formatting

# Given an integer, N, print the following values for each integer  from  to :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary


def print_formatted(number):
    # your code goes here
    wid = len(f'{number:b}')
    for i in range(1, number+1):
        # x -> lower, X -> upper
        print(f'{i:>{wid}d} {i:{wid}o} {i:{wid}X} {i:{wid}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)