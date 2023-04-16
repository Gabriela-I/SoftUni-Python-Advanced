number_of_students = int(input())
students = {}
for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))
for k, v in students.items():
    grade_as_str = [''.join(f'{grade:.2f}') for grade in v] # ' '.join(map(lambda grade: f'{grade:.2f}', v))
    average = sum(v) / len(v)
    print(f"{k} ->", *grade_as_str, sep=' ', end=' ')
    print(f"(avg: {average:.2f})")
