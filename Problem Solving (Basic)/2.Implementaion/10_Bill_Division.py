import sys

def bonAppetit(bill, k, b):
    actual_share = (sum(bill) - bill[k]) // 2
    print("Bon Appetit" if b == actual_share else b - actual_share)

if __name__ == '__main__':
    _, k = map(int, input().split())
    bill = list(map(int, input().split()))
    b = int(input())
    bonAppetit(bill, k, b)