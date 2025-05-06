def circularArrayRotation(a, k, queries):
    k = k % len(a)
    a = a[-k:] + a[:-k]

    return [a[q] for q in queries]
 
if __name__ == '__main__':
    n, k, q = map(int, input().strip().split())
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print('\n'.join(map(str, result)))