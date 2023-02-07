# https://www.hackerrank.com/challenges/finding-the-percentage

n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sum = 0
for i in student_marks[query_name]:
    sum += i
print(f'{sum/3:.2f}')
