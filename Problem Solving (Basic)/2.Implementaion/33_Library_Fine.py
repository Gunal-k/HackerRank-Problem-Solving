from datetime import datetime

def libraryFine(d1, m1, y1, d2, m2, y2):
    return_date = datetime(y1, m1, d1)
    due_date = datetime(y2, m2, d2)

    if return_date <= due_date:
        return 0

    elif return_date.year == due_date.year and return_date.month == due_date.month:
        days_late = (return_date - due_date).days
        return 15 * days_late

    elif return_date.year == due_date.year:
        months_late = (return_date.month - due_date.month)
        return 500 * months_late

    else:
        return 10000
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])
    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)