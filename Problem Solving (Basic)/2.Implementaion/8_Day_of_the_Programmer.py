def dayOfProgrammer(year):
    # Special case: transition year from Julian to Gregorian
    if year == 1918:
        return "26.09.1918"
    
    # Julian calendar (before 1918): leap year if divisible by 4
    if year < 1918:
        is_leap = year % 4 == 0
    else:
        # Gregorian calendar: leap year if divisible by 400 or divisible by 4 and not by 100
        is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    return f"12.09.{year}" if is_leap else f"13.09.{year}"

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result)