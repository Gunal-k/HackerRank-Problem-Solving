def breakingRecords(scores):
    max_count = min_count = 0
    max_val = min_val = scores[0]
    
    for score in scores[1:]:
        if score > max_val:
            max_val = score
            max_count += 1
        elif score < min_val:
            min_val = score
            min_count += 1
    return [max_count, min_count]

if __name__ == '__main__':
    input()  # skip n
    scores = list(map(int, input().split()))
    print(*breakingRecords(scores))