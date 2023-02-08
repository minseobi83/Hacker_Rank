student = []
second_name = []

for i in range(int(input())):
    name = input()
    score = float(input())
    #student.insert(i, [name, score])
    student.append([name, score])

# The example sorts the nested tuples initally by their first elements, then by their second.
# vals.sort(key=lambda e: e[1])
student.sort(key=lambda e:e[1], reverse=False)

lowest = student[0][1]
second = 0

for i in range(1, len(student)):
    if student[i][1] > lowest:
        # if you find second lowest, break.
        second = student[i][1]
        break
# second lowest name append to list (second_name)
for i in range(1, len(student)):
    if student[i][1] == second:
        second_name.append(student[i][0])

for i in sorted(second_name):
    print(i)