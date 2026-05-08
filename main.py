from utils import add_student, show_students, find_student

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            find_student()
        elif choice == "0":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
