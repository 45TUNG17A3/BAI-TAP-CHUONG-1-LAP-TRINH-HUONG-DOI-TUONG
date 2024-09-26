import math

class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.kiem_tra_hop_le()

    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            raise ValueError("Mẫu số không được bằng 0.")
    
    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        self.kiem_tra_hop_le()

    def in_phan_so(self):
        if self.mau_so == 1:
            print(self.tu_so)
        elif self.tu_so == 0:
            print(0)
        else:
            print(f"{self.tu_so}/{self.mau_so}")

    def tim_ucln(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)  

    def toi_gian(self):
        ucln = self.tim_ucln(self.tu_so, self.mau_so)
        tu_so_rut_gon = self.tu_so // ucln
        mau_so_rut_gon = self.mau_so // ucln
        print(f"Phân số sau khi tối giản là: {tu_so_rut_gon}/{mau_so_rut_gon}")

ps = PhanSo()
ps.nhap_phan_so()
ps.toi_gian()