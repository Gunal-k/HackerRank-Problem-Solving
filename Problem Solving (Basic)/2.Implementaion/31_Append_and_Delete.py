def appendAndDelete(s, t, k):
    common_length = 0
    min_len = min(len(s), len(t))
    
    while common_length < min_len and s[common_length] == t[common_length]:
        common_length += 1

    required_ops = (len(s) - common_length) + (len(t) - common_length)

    if required_ops <= k and (k - required_ops) % 2 == 0:
        return "Yes"
    elif k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)