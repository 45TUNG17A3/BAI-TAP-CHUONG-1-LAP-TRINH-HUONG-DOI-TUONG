class Date:
    def __init__(self, ngay=0, thang=0, nam=0):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def nhap_du_lieu(self):
        self.ngay = int(input("Nhập ngày: "))
        while self.ngay <= 0 or self.ngay > 31:
            self.ngay = int(input("Ngày nhập vào không hợp lệ, hãy nhập lại: "))
        self.thang = int(input("Nhập tháng: "))
        while self.thang <= 0 or self.thang > 12:
            self.thang = int(input("Tháng nhập vào không hợp lệ, hãy nhập lại: "))
        self.nam = int(input("Nhập năm: "))
        while self.nam < 0:
            self.nam = int(input("Năm nhập vào không hợp lệ, hãy nhập lại: "))

    def xuat_du_lieu(self):
        return f"{self.ngay}/{self.thang}/{self.nam}"

class Employee:
    def __init__(self):
        self.ho_ten = ""
        self.ngay_sinh = Date()  
        self.ngay_vao_cong_ty = Date()  

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ và tên nhân viên: ")
        print("Nhập ngày sinh:")
        self.ngay_sinh.nhap_du_lieu()
        print("Nhập ngày vào công ty:")
        self.ngay_vao_cong_ty.nhap_du_lieu()

    def xuat_thong_tin(self):
        return f"Họ tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh.xuat_du_lieu()}, Ngày vào công ty: {self.ngay_vao_cong_ty.xuat_du_lieu()}"

class QuanLyNhanVien:
    def __init__(self):
        self.danh_sach_nhan_vien = []

    def them_nhan_vien(self):
        nv = Employee()
        nv.nhap_thong_tin()
        self.danh_sach_nhan_vien.append(nv)

    def xuat_danh_sach_nhan_vien(self):
        print("\nDanh sách nhân viên:")
        for nv in self.danh_sach_nhan_vien:
            print(nv.xuat_thong_tin())

    def tim_kiem_nhan_vien(self, ten):
        ket_qua = []
        for nv in self.danh_sach_nhan_vien:
            if ten.lower() in nv.ho_ten.lower():
                ket_qua.append(nv)
        return ket_qua

    def xuat_thong_tin_tim_kiem(self, ten):
        ket_qua = self.tim_kiem_nhan_vien(ten)
        if len(ket_qua) > 0:
            print(f"\nKết quả tìm kiếm cho nhân viên có tên '{ten}':")
            for nv in ket_qua:
                print(nv.xuat_thong_tin())
        else:
            print(f"\nKhông tìm thấy nhân viên nào có tên '{ten}'")

def main():
    quan_ly_nhan_vien = QuanLyNhanVien()

    while True:
        print("\n1. Thêm nhân viên")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Tìm kiếm nhân viên theo tên")
        print("4. Thoát")
        lua_chon = int(input("Nhập lựa chọn: "))

        if lua_chon == 1:
            quan_ly_nhan_vien.them_nhan_vien()
        elif lua_chon == 2:
            quan_ly_nhan_vien.xuat_danh_sach_nhan_vien()
        elif lua_chon == 3:
            ten = input("Nhập tên nhân viên cần tìm: ")
            quan_ly_nhan_vien.xuat_thong_tin_tim_kiem(ten)
        elif lua_chon == 4:
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy thử lại.")

main()