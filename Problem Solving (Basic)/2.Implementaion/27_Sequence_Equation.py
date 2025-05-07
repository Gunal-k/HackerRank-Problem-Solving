def permutationEquation(p):
    n = len(p)
    p = [0] + p

    pos = [0] * (n + 1)
    for i in range(1, n + 1):
        pos[p[i]] = i

    result = []
    for x in range(1, n + 1):
        y = pos[pos[x]]
        result.append(y)
    return result
    
if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    print("\n".join(map(str,result)))