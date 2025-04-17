def diagonalDifference(arr):
    primary = sum(arr[i][i] for i in range(len(arr)))
    secondary = sum(arr[i][len(arr) - i - 1] for i in range(len(arr)))
    return abs(primary - secondary)

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(diagonalDifference(arr))
