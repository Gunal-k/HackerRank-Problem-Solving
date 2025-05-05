def viralAdvertising(n):
    shared = 5
    total_likes = 0
    
    for day in range(n):
        liked = shared // 2
        total_likes += liked
        shared = liked * 3
        
    return total_likes

if __name__ == '__main__':
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)