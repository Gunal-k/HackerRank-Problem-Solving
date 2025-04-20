import math
from functools import reduce

def getTotalX(a, b):
    lcm_a = reduce(math.lcm, a)
    gcd_b = reduce(math.gcd, b)
    return sum(1 for i in range(lcm_a, gcd_b + 1, lcm_a) if gcd_b % i == 0)

if __name__ == '__main__':
    input()  # skip n and m
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(getTotalX(a, b))