def utopianTree(n):
    height = 1
    for i in range(1, n + 1):
        if i % 2 == 1:  # Spring (odd cycles)
            height *= 2
        else:           # Summer (even cycles)
            height += 1
    return height

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        print(utopianTree(int(input().strip())))