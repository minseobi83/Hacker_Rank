#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    result = ""
    
    for i in range(len(s)):
        if i == 0 or str(s)[i-1] == ' ':
            result += str(s)[i].upper()
        else:
             result += str(s)[i]

    return result

# Use capitalize() : String class
# n=input()
# list1=n.split(' ') => split method makes List type
# for i in list1:
#     print(i.capitalize(),end=' ')