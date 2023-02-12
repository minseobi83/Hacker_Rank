# https://www.hackerrank.com/challenges/py-set-difference-operation

s1_size = int(input())
s1 = set(map(int, input().split()))
s2_size = int(input())
s2 = set(map(int, input().split()))

print(len(s1.difference(s2)))