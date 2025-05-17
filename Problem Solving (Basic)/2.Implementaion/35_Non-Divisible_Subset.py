def nonDivisibleSubset(k, s):
    from collections import defaultdict

    remainder_counts = defaultdict(int)
    
    for num in s:
        remainder = num % k
        remainder_counts[remainder] += 1

    max_size = 0

    if remainder_counts[0] > 0:
        max_size = 1

    for r in range(1, (k // 2) + 1):
        if r != k - r:
            max_size += max(remainder_counts[r], remainder_counts[k - r])
        else:
            max_size += 1

    return max_size

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    print(result)