def miniMaxSum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMaxSum(arr)