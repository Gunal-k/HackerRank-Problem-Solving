def pickingNumbers(a):
    freq = [0] * 101
    for num in a:
        freq[num] += 1

    max_count = 0
    for i in range(100):
        max_count = max(max_count, freq[i] + freq[i+1])

    return max_count

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)