from student import students

def add_student():
    name = input("Nhập tên sinh viên: ")
    students.append(name)
    print("Đã thêm sinh viên!")

def show_students():
    if len(students) == 0:
        print("Danh sách trống!")
    else:
        print("\n===== DANH SÁCH SINH VIÊN =====")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student}")

def find_student():
    keyword = input("Nhập tên cần tìm: ")

    found = False

    for student in students:
        if keyword.lower() in student.lower():
            print("Tìm thấy:", student)
            found = True

    if not found:
        print("Không tìm thấy sinh viên!")from student import students

def add_student():
    name = input("Nhập tên sinh viên: ")
    students.append(name)
    print("Đã thêm sinh viên!")

def show_students():
    if len(students) == 0:
        print("Danh sách trống!")
    else:
        print("\n===== DANH SÁCH SINH VIÊN =====")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student}")

def find_student():
    keyword = input("Nhập tên cần tìm: ")

    found = False

    for student in students:
        if keyword.lower() in student.lower():
            print("Tìm thấy:", student)
            found = True

    if not found:
        print("Không tìm thấy sinh viên!")
