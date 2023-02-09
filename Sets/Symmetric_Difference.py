# https://www.hackerrank.com/challenges/symmetric-difference

# Input Format
# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

m_size = int(input())
m = set(map(int, input().split()))
n_size = int(input())
n = set(map(int, input().split()))

for i in sorted(list(m.difference(n).union(n.difference(m)))): print(i)