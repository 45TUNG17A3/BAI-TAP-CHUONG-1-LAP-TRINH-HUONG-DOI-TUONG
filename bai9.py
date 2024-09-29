import math

class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh 

    def tinh_chu_vi(self):
        pass  
    def tinh_dien_tich(self):
        pass  


class HinhBinhHanh(DaGiac):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(4)  
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong


class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)


class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)  


def main():
    canh_vuong = float(input("Nhập chiều dài cạnh hình vuông: "))
    hinh_vuong = HinhVuong(canh_vuong)
    print("Chu vi hình vuông:", hinh_vuong.tinh_chu_vi())
    print("Diện tích hình vuông:", hinh_vuong.tinh_dien_tich())

    # Nhập dữ liệu hình chữ nhật
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    hinh_chu_nhat = HinhChuNhat(chieu_dai, chieu_rong)
    print("Chu vi hình chữ nhật:", hinh_chu_nhat.tinh_chu_vi())
    print("Diện tích hình chữ nhật:", hinh_chu_nhat.tinh_dien_tich())

    # Nhập dữ liệu hình bình hành
    chieu_dai_hinh_binh_hanh = float(input("Nhập chiều dài hình bình hành: "))
    chieu_rong_hinh_binh_hanh = float(input("Nhập chiều rộng hình bình hành: "))
    hinh_binh_hanh = HinhBinhHanh(chieu_dai_hinh_binh_hanh, chieu_rong_hinh_binh_hanh)
    print("Chu vi hình bình hành:", hinh_binh_hanh.tinh_chu_vi())
    print("Diện tích hình bình hành:", hinh_binh_hanh.tinh_dien_tich())

main()