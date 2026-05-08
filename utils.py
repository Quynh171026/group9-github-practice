def show_students():
    print("\n===== DANH SÁCH SINH VIÊN =====")

    if len(students) == 0:
        print("Hiện chưa có sinh viên nào.")
    else:
        for i, student in enumerate(students, start=1):
            print(f"STT {i}: {student}")

        print(f"\nTổng số sinh viên: {len(students)}")

