class Date:
    def __init__(self):
        self.ngay = 0
        self.thang = 0
        self.nam = 0

    def nhap_du_lieu(self):
        self.ngay = int(input("Nhập ngày: "))
        while self.ngay <= 0 or self.ngay >= 32:
            self.ngay = int(input("Ngày nhập vào không hợp lệ, hãy nhập lại: "))
        self.thang = int(input("Nhập tháng: "))
        while self.thang <= 0 or self.thang >= 13:
            self.thang = int(input("Tháng nhập vào không hợp lệ, hãy nhập lại: "))
        self.nam = int(input("Nhập vào năm: "))
        while self.nam < 0:
            self.nam = int(input("Năm nhập vào không hợp lệ, hãy nhập lại: "))

    def la_nam_nhuan(self):
        return (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0)

    def kiem_tra_ngay_hop_le(self):
        if self.thang < 1 or self.thang > 12:
            return False
        
        if self.thang in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= self.ngay <= 31
        elif self.thang in [4, 6, 9, 11]:
            return 1 <= self.ngay <= 30
        elif self.thang == 2:
            if self.la_nam_nhuan():
                return 1 <= self.ngay <= 29
            else:
                return 1 <= self.ngay <= 28
        return False

    def tinh_ngay_tiep_theo(self):
        if not self.kiem_tra_ngay_hop_le():
            print("Ngày tháng nhập vào không hợp lệ.")
            return

        print(f"Hôm nay là ngày {self.ngay} tháng {self.thang} năm {self.nam}")
        if self.la_nam_nhuan():
            print("Đây là năm nhuận")
            if self.thang == 2:
                if self.ngay == 29:
                    print(f"Ngày tiếp theo là ngày 1 tháng {self.thang + 1} năm {self.nam}")
                else:
                    print(f"Ngày tiếp theo là ngày {self.ngay + 1} tháng {self.thang} năm {self.nam}")
            elif self.thang in [4, 6, 9, 11]:
                if self.ngay == 30:
                    print(f"Ngày tiếp theo là ngày 1 tháng {self.thang + 1} năm {self.nam}")
                else:
                    print(f"Ngày tiếp theo là ngày {self.ngay + 1} tháng {self.thang} năm {self.nam}")
            else:
                if self.ngay == 31:
                    if self.thang == 12:
                        print(f"Ngày tiếp theo là ngày 1 tháng 1 năm {self.nam + 1}")
                    else:
                        print(f"Ngày tiếp theo là ngày 1 tháng {self.thang + 1} năm {self.nam}")
                else:
                    print(f"Ngày tiếp theo là ngày {self.ngay + 1} tháng {self.thang} năm {self.nam}")
        else:
            print("Đây không phải là năm nhuận")
            if self.thang == 2:
                if self.ngay == 28:
                    print(f"Ngày tiếp theo là ngày 1 tháng {self.thang + 1} năm {self.nam}")
                else:
                    print(f"Ngày tiếp theo là ngày {self.ngay + 1} tháng {self.thang} năm {self.nam}")
            elif self.thang in [4, 6, 9, 11]:
                if self.ngay == 30:
                    print(f"Ngày tiếp theo là ngày 1 tháng {self.thang + 1} năm {self.nam}")
                else:
                    print(f"Ngày tiếp theo là ngày {self.ngay + 1} tháng {self.thang} năm {self.nam}")
            else:
                if self.ngay == 31:
                    if self.thang == 12:
                        print(f"Ngày tiếp theo là ngày 1 tháng 1 năm {self.nam + 1}")
                    else:
                        print(f"Ngày tiếp theo là ngày 1 tháng {self.thang + 1} năm {self.nam}")
                else:
                    print(f"Ngày tiếp theo là ngày {self.ngay + 1} tháng {self.thang} năm {self.nam}")

ng_th_n = Date()
ng_th_n.nhap_du_lieu()
ng_th_n.tinh_ngay_tiep_theo()