import sys

num_of_case = int(sys.stdin.readline())

for _ in range(num_of_case):
    se = sys.stdin.readline()[::-1].split()
    se.reverse()
    print(' '.join(se))
