def birthday(s, d, m):
    return sum(1 for i in range(len(s) - m + 1) if sum(s[i:i + m]) == d)

if __name__ == '__main__':
    input()  # skip n
    s = list(map(int, input().split()))
    d, m = map(int, input().split())
    print(birthday(s, d, m))