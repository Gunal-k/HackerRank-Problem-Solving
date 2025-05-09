def findDigits(n):
    a = list(str(n))
    return sum(1 for num in a if int(num) !=0 and n % int(num) == 0)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(str(result))