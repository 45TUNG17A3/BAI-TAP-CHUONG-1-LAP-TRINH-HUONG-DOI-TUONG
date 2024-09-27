class TamGiac:
    def __init__(self, canh_a, canh_b, canh_c):
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.canh_c = canh_c
        
    def kiem_tra_tam_giac(self):
        return (self.canh_a + self.canh_b > self.canh_c) and (self.canh_a + self.canh_c > self.canh_b) and (self.canh_b + self.canh_c > self.canh_a) 
    
    def chu_vi(self):
        if self.kiem_tra_tam_giac():
            return self.canh_a + self.canh_b + self.canh_c
        else:
            return "Tam giác không hợp lệ"
        
    def dien_tich(self):
        if self.kiem_tra_tam_giac():
            p = self.chu_vi() / 2
            s = (p * (p - self.canh_a) * (p - self.canh_b) * (p - self.canh_c)) ** 0.5
            return s
        else:
            return "Tam giác không hợp lệ"
    
class TamGiacVuong(TamGiac):
    def kiem_tra_tam_giac_vuong(self):
        canh_a, canh_b, canh_c = sorted([self.canh_a, self.canh_b, self.canh_c])
        return canh_a**2 + canh_b**2 == canh_c**2
    
class TamGiacCan(TamGiac):
    def kiem_tra_tam_giac_can(self):
        return (self.canh_a == self.canh_b) or (self.canh_b == self.canh_c) or (self.canh_a == self.canh_c)
    
class TamGiacDeu(TamGiacCan):
    def kiem_tra_tam_giac_deu(self):
        return self.canh_a == self.canh_b == self.canh_c
    
def nhap_du_lieu():
    canh_a = int(input("Nhập độ dài cạnh a: "))
    canh_b = int(input("Nhập độ dài cạnh b: "))
    canh_c = int(input("Nhập độ dài cạnh c: "))
    return canh_a, canh_b, canh_c

canh_a, canh_b, canh_c = nhap_du_lieu()
tam_giac = TamGiac(canh_a, canh_b, canh_c)

print("Chu vi của tam giác:", tam_giac.chu_vi())
print("Diện tích của tam giác:", tam_giac.dien_tich())

tam_giac_vuong = TamGiacVuong(canh_a, canh_b, canh_c)
print("Tam giác có phải là tam giác vuông không?", tam_giac_vuong.kiem_tra_tam_giac_vuong())

tam_giac_can = TamGiacCan(canh_a, canh_b, canh_c)
print("Tam giác có phải là tam giác cân không?", tam_giac_can.kiem_tra_tam_giac_can())

tam_giac_deu = TamGiacDeu(canh_a, canh_b, canh_c)
print("Tam giác có phải là tam giác đều không?", tam_giac_deu.kiem_tra_tam_giac_deu())