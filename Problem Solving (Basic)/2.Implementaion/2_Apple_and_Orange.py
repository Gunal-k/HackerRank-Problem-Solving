def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = sum(1 for apple in apples if s <= a + apple <= t)
    orange_count = sum(1 for orange in oranges if s <= b + orange <= t)
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    input()  # m, n not needed
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    
    countApplesAndOranges(s, t, a, b, apples, oranges)