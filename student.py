students = []

def add_student(name, student_id, gpa):
    student = {
        "name": name,
        "id": student_id,
        "gpa": gpa
    }
    students.append(student)
    print(f"✅ Đã thêm sinh viên: {name}")

def display_all():
    if not students:
        print("📭 Danh sách trống.")
        return
    print("\n📋 DANH SÁCH SINH VIÊN:")
    print("-" * 40)
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} | MSSV: {s['id']} | GPA: {s['gpa']}")
    print("-" * 40)

def search_student(keyword):
    results = [s for s in students if keyword.lower() in s['name'].lower() or keyword in s['id']]
    if not results:
        print("🔍 Không tìm thấy sinh viên.")
    else:
        print(f"\n🔍 Kết quả tìm kiếm '{keyword}':")
        for s in results:
            print(f"  - {s['name']} | MSSV: {s['id']} | GPA: {s['gpa']}")
