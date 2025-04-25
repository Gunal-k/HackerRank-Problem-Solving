def countingValleys(path):
    altitude = 0
    valleys = 0

    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1
        else:
            altitude -= 1

    return valleys

if __name__ == '__main__':
    steps = int(input().strip())
    path = input().strip()
    result = countingValleys(path)
    print(str(result))