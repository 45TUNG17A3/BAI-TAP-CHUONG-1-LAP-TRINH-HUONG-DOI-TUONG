class qlydiemthi:
    def __init__(self):
        self.ho_ten = ""
        self.diem_Toan = 0
        self.diem_Ly = 0
        self.diem_Hoa = 0
        
    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên của thí sinh: ")
        self.diem_Toan = float(input(f"Nhập điểm Toán của thí sinh {self.ho_ten}: "))
        self.diem_Ly = float(input(f"Nhập điểm Lý của thí sinh {self.ho_ten}: "))
        self.diem_Hoa = float(input(f"Nhập điểm Hóa của thí sinh {self.ho_ten}: "))
        return self
    
    def tong_diem(self):
        return self.diem_Toan + self.diem_Ly + self.diem_Hoa
    
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_Toan}")
        print(f"Điểm Lý: {self.diem_Ly}")
        print(f"Điểm Hóa: {self.diem_Hoa}")
        print(f"Tổng điểm: {self.tong_diem()}")
        
    def lay_tong_diem(self):  
        return self.tong_diem()

tiep_tuc = "y"
danh_sach = []

while tiep_tuc.lower() == "y":
    ql = qlydiemthi()
    thong_tin = ql.nhap_thong_tin()
    danh_sach.append(thong_tin)
    tiep_tuc = input("Bạn có muốn tiếp tục nhập thông tin thí sinh không (y/n): ")

danh_sach.sort(key=qlydiemthi.lay_tong_diem, reverse=True)

print("\nDanh sách thí sinh trúng tuyển:")
for thi_sinh in danh_sach:
    if thi_sinh.tong_diem() >= 20:
        thi_sinh.in_thong_tin()
    else:
        break 