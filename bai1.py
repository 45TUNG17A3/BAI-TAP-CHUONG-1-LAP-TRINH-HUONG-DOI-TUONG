class HinhChuNhat:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0
        
    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập độ dài chiều dài hình chữ nhật: "))
        self.chieu_rong = float(input("Nhập độ dài chiều rộng hình chữ nhật: "))
        
    def chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def ket_qua(self):
        print("Chiều dài hình chữ nhật là:",self.chieu_dai)
        print("Chiều rộng hình chữ nhật là:",self.chieu_rong)
        print("Chu vi của hình chữ nhật là:",self.chu_vi())
        print("Diện tích của hình chữ nhật là:",self.dien_tich())
        
hcn = HinhChuNhat()
hcn.nhap_du_lieu()
hcn.ket_qua()