from student import add_student, display_all, search_student
from utils import print_menu, get_input

def main():
    while True:
        print_menu()
        choice = input("👉 Chọn chức năng: ").strip()

        if choice == "1":
            name = get_input("Họ tên: ")
            sid  = get_input("MSSV: ")
            gpa  = get_input("GPA: ", float)
            add_student(name, sid, gpa)

        elif choice == "2":
            display_all()

        elif choice == "3":
            keyword = get_input("Nhập tên hoặc MSSV cần tìm: ")
            search_student(keyword)

        elif choice == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("⚠️  Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
