# https://www.hackerrank.com/challenges/py-set-discard-remove-pop

# Print the sum of the elements of set s on a single line.

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    # it should be memorized.!!
    command, *num = input().split()
    num = map(int, num)
    
    if command == 'remove':
        s.remove(*num)

    elif command == 'discard':
        s.discard(*num)

    elif command == 'pop':
        s.pop()

# it should be memorized.!!
print(sum(i for i in list(s)))