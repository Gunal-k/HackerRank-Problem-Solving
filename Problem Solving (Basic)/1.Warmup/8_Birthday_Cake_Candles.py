def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)

if __name__ == '__main__':
    _ = int(input())
    candles = list(map(int, input().split()))
    print(birthdayCakeCandles(candles))