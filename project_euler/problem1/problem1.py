import sys

__author__ = 'carterdelloro'

def solve(n):
    return sum(set(range(3,n,3)+range(5,n,5)))

def __main():
    print(solve(1000))

if __name__ == '__main__':
    sys.exit(__main())
