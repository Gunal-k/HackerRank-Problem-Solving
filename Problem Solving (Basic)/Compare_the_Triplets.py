def compareTriplets(a, b):
    x, y = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            y += 1
    return [x, y]

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))
