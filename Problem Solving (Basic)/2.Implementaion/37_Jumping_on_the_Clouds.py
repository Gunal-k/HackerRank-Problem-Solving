def jumpingOnClouds(c):
    i = 0
    jumps = 0
    n = len(c)
    
    while i < n - 1:
        # Try to jump two steps if within bounds and safe
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    
    return jumps

if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)