def add_student():
    id = input("Nhập ID: ")
    name = input("Nhập tên: ")
    student = Student(id, name)
    students.append(student)
    print("Thêm sinh viên thành công!")
