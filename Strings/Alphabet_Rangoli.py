# https://www.hackerrank.com/challenges/alphabet-rangoli


def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    # length count
    middle = ""
    
    for i in range(size-1, -1, -1):
        if i==0: middle+=alpha[0]
        else: middle+=(alpha[i]+"-")
    
    for i in range(1, size):
        middle+=("-" + alpha[i])

    # draw Alphabet Rangoli
    for i in range(2*size-1):
        # upper body
        if i < size-1:
            for k in range()

        # center body
        elif i == size-1:
            print(middle)

        # lower body
        else:
            print('-'*len(middle))

if __name__ == '__main__':
    n = int(input())
    
    print_rangoli(n)

