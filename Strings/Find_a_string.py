# https://www.hackerrank.com/challenges/find-a-string

# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    num = 0
    for i in range(len(string)):
        if (string[i:i+len(sub_string)]) == sub_string:
            num += 1
        if i+len(sub_string) == len(string):
            break
    return num

string = input().strip()
sub_string = input().strip()
   
count = count_substring(string, sub_string)
print(count)

# Use find() function : String class

# string=input()
# substring=input()
# sums=0
# for i in range(0,len(string)):
#     if(string.find(substring,i,i+len(substring)) != -1):
#         sums=sums+1
# print(sums)