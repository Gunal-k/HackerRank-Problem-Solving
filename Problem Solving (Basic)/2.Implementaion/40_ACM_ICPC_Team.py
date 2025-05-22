import os
from itertools import combinations

def acmTeam(topic):
    max_topics = 0
    team_count = 0

    for p1, p2 in combinations(topic, 2):
        combined = bin(int(p1, 2) | int(p2, 2)).count('1')
        if combined > max_topics:
            max_topics = combined
            team_count = 1
        elif combined == max_topics:
            team_count += 1

    return [max_topics, team_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()