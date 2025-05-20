from collections import Counter

def equalizeArray(arr):
    freq = Counter(arr)
    max_freq = max(freq.values())
    return len(arr) - max_freq

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)