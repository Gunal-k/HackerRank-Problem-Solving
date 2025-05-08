def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0
    
    while True:
        i = (i + k) % n
        e -= 1
        if c[i] == 1:
            e -= 2
        if i == 0:
            break
            
    return e

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    print(result)