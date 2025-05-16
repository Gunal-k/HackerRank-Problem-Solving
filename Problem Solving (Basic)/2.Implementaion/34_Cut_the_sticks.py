def cutTheSticks(arr):
    result = []
    while arr:
        result.append(len(arr))
        min_len = min(arr)
        arr = [x - min_len for x in arr]
        arr = [x for x in arr if x > 0]
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    print('\n'.join(map(str, result)))