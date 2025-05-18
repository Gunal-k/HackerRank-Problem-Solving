def repeatedString(s, n):
    count_a_in_s = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    
    count = count_a_in_s * full_repeats
    count += s[:remainder].count('a')
    
    return count
    

if __name__ == '__main__':
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(str(result))