n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

top = arr[0]
result = 0
for i in arr:
    if i < top:
        result = i
        break
print(result)