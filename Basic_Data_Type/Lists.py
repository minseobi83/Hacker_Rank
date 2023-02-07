# https://www.hackerrank.com/challenges/python-lists

N = int(input())
arr = []

for i in range(N):
    command = list(input().split())
    if command[0].startswith('insert'):
        arr.insert(int(command[1]), int(command[2]))
        # To use 'arr.insert(*command)', it should be seperated by command and parameter
    elif command[0].startswith('remove'):
        arr.remove(int(command[1]))
    elif command[0].startswith('append'):
        arr.append(int(command[1]))
    elif command[0].startswith('print'):
        print(arr)
    elif command[0].startswith('sort'):
        arr.sort()
    elif command[0].startswith('pop'):
        arr.pop()
    elif command[0].startswith('reverse'):
        arr.reverse()

# arr = []
# commad, *value = input().split()
# value = map (int, value)

# if commad == 'insert': arr.insert(*value)
