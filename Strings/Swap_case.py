# https://www.hackerrank.com/challenges/swap-case

def swap_case(s):
    str = ""
    for i in s: 
        if i.islower():
            str+=i.upper()
        elif i.isupper():
            str+=i.lower()
        else: str+=i
    return str

s = input()
result = swap_case(s)
print(result)

# Use swapcase() : String class
# string_input = input()
# print(string_input.swapcase())