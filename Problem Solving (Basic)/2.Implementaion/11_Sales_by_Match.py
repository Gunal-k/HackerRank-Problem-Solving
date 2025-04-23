def sockMerchant(n, ar):
    unmatched = set()
    pairs = 0

    for sock in ar:
        if sock in unmatched:
            unmatched.remove(sock)
            pairs += 1
        else:
            unmatched.add(sock)
    
    return pairs

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n, ar))