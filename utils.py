def print_menu():
    print("\n" + "="*40)
    print("   HỆ THỐNG QUẢN LÝ SINH VIÊN")
    print("="*40)
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách")
    print("3. Tìm kiếm sinh viên")
    print("0. Thoát")
    print("="*40)

def get_input(prompt, input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("⚠️  Nhập sai định dạng, thử lại.")
