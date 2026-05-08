def search_student(students, keyword):
    result = []
def add_student():
    id = input("Nhập ID: ")
    name = input("Nhập tên: ")
    student = Student(id, name)
    students.append(student)
    print("Thêm sinh viên thành công!")
def show_students():
    print("\n===== DANH SÁCH SINH VIÊN =====")

    if len(students) == 0:
        print("Hiện chưa có sinh viên nào.")
    else:
        for i, student in enumerate(students, start=1):
            print(f"STT {i}: {student}")

        print(f"\nTổng số sinh viên: {len(students)}")

    for student in students:
        if keyword.lower() in student.lower():
            result.append(student)

    return result
