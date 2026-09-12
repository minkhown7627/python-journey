"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Nhập tên của bạn: ")
print(f"Xin chào, {ten}!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Nhập tuổi của bạn: "))
nam_hien_tai = 2026
nam_sinh = nam_hien_tai - tuoi
print(f"Năm sinh của bạn là: {nam_sinh}")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
tong = so1 + so2
print(f"Tổng: {so1} + {so2} = {tong}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
print("\n--- TRÒ CHƠI MAD LIBS MINI ---")
ten_nhan_vat = input("Nhập một cái tên: ")
tinh_tu = input("Nhập một tính từ (ví dụ: khổng lồ, ngốc nghếch, đáng yêu): ")
con_vat = input("Nhập một con vật: ")
so_luong = input("Nhập một con số: ")
print("\n--- CÂU CHUYỆN CỦA BẠN ---")
print(f"Một ngày đẹp trời, {ten_nhan_vat} nhìn thấy một con {con_vat} trông rất {tinh_tu}.")
print(f"Con {con_vat} đó đã ăn trộm mất {so_luong} cái bánh rán rồi chạy biến mất!")