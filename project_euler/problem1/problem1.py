import sys

__author__ = 'carterdelloro'

def solve(n):
    return sum(set(range(3,n,3)+range(5,n,5)))
    
def solve2(n):
    tot = 0
    for j in range(1, n):
        if j % 3 == 0 or j % 5 == 0:
            tot += j
    return tot

def solve3(n):
    return sum(j for j in range(1, n) if j % 3 == 0 or j % 5 == 0)

def __main():
    print(solve(1000))

if __name__ == '__main__':
    sys.exit(__main())
