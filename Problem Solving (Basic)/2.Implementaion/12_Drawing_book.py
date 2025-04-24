def pageCount(n, p):
    # Minimum of front flips and back flips
    return min(p // 2, n // 2 - p // 2)

if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())
    print(pageCount(n, p))