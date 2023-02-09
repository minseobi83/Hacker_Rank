# https://www.hackerrank.com/challenges/py-introduction-to-sets

def average(array):
    # your code goes here
    return sum(i for i in array) / len(array)

n = int(input())
arr = set(list(map(int, input().split())))
result = average(arr)
print(result)
