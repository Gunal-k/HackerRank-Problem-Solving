def timeConversion(time_str):
    period = time_str[-2:]
    h, m, s = map(int, time_str[:-2].split(':'))

    if period == 'AM' and h == 12:
        h = 0
    elif period == 'PM' and h != 12:
        h += 12

    return f"{h:02}:{m:02}:{s:02}"

if __name__ == '__main__':
    s = input()
    print(timeConversion(s))