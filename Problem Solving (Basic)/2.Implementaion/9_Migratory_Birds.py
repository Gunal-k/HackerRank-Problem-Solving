from collections import Counter
import os
import sys

def migratoryBirds(arr):
    count = Counter(arr)
    max_freq = max(count.values())
    return min(bird for bird, freq in count.items() if freq == max_freq)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input()  # Skip arr_count since it's not needed
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()