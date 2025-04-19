def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade >= 38:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                res.append(next_multiple)
            else:
                res.append(grade)
        else:
            res.append(grade)
    return res

if __name__ == '__main__':
    grades = [int(input().strip()) for _ in range(int(input().strip()))]
    for result in gradingStudents(grades):
        print(result)