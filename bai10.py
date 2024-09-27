import math

class Diem:
    def __init__(self, hoanh=0, tung=0):
        self.hoanh = hoanh
        self.tung = tung

    def __str__(self):
        return f"Điểm({self.hoanh}, {self.tung})"


class Elip(Diem):
    def __init__(self, hoanh, tung, ban_truc_larger, ban_truc_smaller):
        super().__init__(hoanh, tung)  
        self.ban_truc_larger = ban_truc_larger  
        self.ban_truc_smaller = ban_truc_smaller  

    def dien_tich(self):
        return math.pi * self.ban_truc_larger * self.ban_truc_smaller  

    def __str__(self):
        return f"Elip với tâm {super().__str__()}, bán trục lớn = {self.ban_truc_larger}, bán trục nhỏ = {self.ban_truc_smaller}"


class HinhTron(Elip):
    def __init__(self, hoanh, tung, ban_kinh):
        super().__init__(hoanh, tung, ban_kinh, ban_kinh)  
        self.ban_kinh = ban_kinh

    def dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)  
    def __str__(self):
        return f"Hình tròn với tâm {super().__str__()} và bán kính = {self.ban_kinh}"


def main():
    hoanh = float(input("Nhập tọa độ hoành của tâm elip: "))
    tung = float(input("Nhập tọa độ tung của tâm elip: "))
    ban_truc_larger = float(input("Nhập bán trục lớn của elip: "))
    ban_truc_smaller = float(input("Nhập bán trục nhỏ của elip: "))
    
    elip = Elip(hoanh, tung, ban_truc_larger, ban_truc_smaller)
    print(elip)  
    print(f"Diện tích elip: {elip.dien_tich()}")

    ban_kinh = float(input("\nNhập bán kính của hình tròn: "))
    hinh_tron = HinhTron(hoanh, tung, ban_kinh)
    print(hinh_tron)  
    print(f"Diện tích hình tròn: {hinh_tron.dien_tich()}")


main()