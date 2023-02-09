# https://www.hackerrank.com/challenges/py-set-add

# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. 
# She decided to count the total number of distinct country stamps in her collection. 
# She asked for your help. You pick the stamps one by one from a stack of N country stamps.

country = set()

for i in range(int(input())):
    country.add(input())

print(len(country))