# https://www.hackerrank.com/challenges/text-wrap

# You are given a string S and width W.
# Your task is to wrap the string into a paragraph of width W.

import textwrap

def wrap(string, max_width):
    result = "" 
    for i in range(len(string)):
        if i%max_width >= 0 and i%max_width < max_width-1:
            result+=string[i]
        else:
            result+=(string[i]+"\n")

    return result

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

# Use textwrap.fill() : textwrap class

# def wrap(string, max_width):
#     return textwrap.fill(string, 4)