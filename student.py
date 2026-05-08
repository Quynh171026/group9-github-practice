def add_student(name, student_id, gpa):
    student = {
        "name": name,
        "id": student_id,
        "gpa": gpa
    }
    students.append(student)
    print(f"Đã thêm sinh viên: {name}")
