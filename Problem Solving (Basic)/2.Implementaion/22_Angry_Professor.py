def angryProfessor(k, a):
    return "NO" if (sum(1 for val in a if val <=0) >= k) else "YES"

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = map(int,input().rstrip().split())
        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)