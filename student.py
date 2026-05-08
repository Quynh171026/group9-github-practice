def search_student(students, keyword):
    result = []

    for student in students:
        if keyword.lower() in student.lower():
            result.append(student)

    return result
