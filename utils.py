from student import Student

students = []

def add_student():
    id = input("Nhập ID: ")
    name = input("Nhập tên: ")
    student = Student(id, name)
    students.append(student)
    print("✅ Thêm sinh viên thành công!")

def show_students():
    if not students:
        print("Danh sách rỗng!")
        return
    for s in students:
        print(s)

def find_student():
    keyword = input("Nhập tên cần tìm: ")
    found = False
    for s in students:
        if keyword.lower() in s.name.lower():
            print(s)
            found = True
    if not found:
        print("❌ Không tìm thấy!")
