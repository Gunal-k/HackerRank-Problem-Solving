def saveThePrisoner(n, m, s):
    return ((s + m - 2) % n) + 1
    
if __name__ == '__main__':
    for t_itr in range(int(input().strip())):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        s = int(first_multiple_input[2])
        result = saveThePrisoner(n, m, s)
        print(result)