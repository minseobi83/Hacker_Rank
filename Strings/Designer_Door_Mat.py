n, m = input().split()
n=int(n)
m=int(m)

# upper
for i in range(int((n-1)/2)):
    print((".|."*(i*2+1)).center(m, "-"))
# center
print("WELCOME".center(m, "-"))
# lower
for i in range(int((n-1)/2), 0, -1):
    print((".|."*(i*2-1)).center(m, "-"))
