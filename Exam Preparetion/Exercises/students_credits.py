def students_credits(*data):
    def print_func():
        result = ''
        if total_credits >= 240:
            result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
        else:
            result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

        sorted_book = dict(sorted(student_book.items(), key=lambda x: -x[1]))
        for k, v in sorted_book.items():
            result += f'{k} - {v:.1f}\n'
        return result

    student_book = {}
    total_credits = 0
    for info in data:
        course, credits, max_point, diyans_point = info.split('-')
        student_credits = int(credits) * (int(diyans_point)/int(max_point))
        student_book[course] = student_credits
        total_credits += student_credits

    return print_func()


print(

    students_credits(

        "Python Development-15-200-200",

        "JavaScript Development-12-500-480",

        "C++ Development-30-500-405",

        "Java Development-10-300-150"

    )

)
print(students_credits("Computer Science-12-300-250","Basic Algebra-15-400-200","Algorithms-25-500-490"))
print(students_credits(

        "Discrete Maths-40-500-450",

        "AI Development-20-400-400",

        "Algorithms Advanced-50-700-630",

        "Python Development-15-200-200",

        "JavaScript Development-12-500-480",

        "C++ Development-30-500-405",

        "Game Engine Development-70-100-70",

        "Mobile Development-25-250-225",

        "QA-20-300-300", ))