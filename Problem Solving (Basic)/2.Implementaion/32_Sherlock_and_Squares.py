import math
def squares(a, b):
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) +1 

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        print(result)