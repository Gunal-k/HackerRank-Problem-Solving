def plusMinus(arr):
    p = n = z = 0
    for a in arr:
        if a > 0:
            p += 1
        elif a < 0:
            n += 1
        else:
            z += 1
    l = len(arr)
    print(f"{p/l:.6f}")
    print(f"{n/l:.6f}")
    print(f"{z/l:.6f}")

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    plusMinus(arr)