def hurdleRace(k, height):
    return max(0, max(height) - k)

if __name__ == '__main__':
    n, k = map(int, input().split())
    height = list(map(int, input().split()))
    print(hurdleRace(k, height))