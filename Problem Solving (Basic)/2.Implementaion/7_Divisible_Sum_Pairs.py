def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    _, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(divisibleSumPairs(len(ar), k, ar))