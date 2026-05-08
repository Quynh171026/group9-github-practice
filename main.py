from utils import search_student
students = ["An", "Binh", "Cuong", "Dung"]

keyword = input("Nhap ten can tim: ")

result = search_student(students, keyword)

if result:
    print("Tim thay:")
    for student in result:
        print(student)
else:
    print("Khong tim thay")
