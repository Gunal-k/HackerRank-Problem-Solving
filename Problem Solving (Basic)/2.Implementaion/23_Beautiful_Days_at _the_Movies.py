def beautifulDays(i, j, k):
    final_val = 0
    for num in range(i,j+1):
        val = int(str(num)[::-1])
        final_val += 1 if abs(num - val) % k == 0 else 0
    return final_val

if __name__ == '__main__':
    i, j, k = map(int, input().rstrip().split())
    result = beautifulDays(i, j, k)
    print(result)