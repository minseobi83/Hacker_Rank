# https://www.hackerrank.com/challenges/python-string-split-and-join

# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

#  a list of string join with "-"
def split_and_join(line):
    # write your code here
    result = "-".join(str(line).split(" "))
    return result
    
# main
line = input()
result = split_and_join(line)
print(result)