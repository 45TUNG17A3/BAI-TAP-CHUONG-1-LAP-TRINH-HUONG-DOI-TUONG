class Stack:
    def __init__(self, size):
        self.capacity = size
        self.stack = []  
        self.top = -1    

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            print(f"Ngăn xếp đã đầy, không thể thêm phần tử {value}")
            return
        self.stack.append(value)  
        self.top += 1              
        print(f"Đã thêm phần tử {value} vào ngăn xếp")

    def pop(self):
        if self.is_empty():
            print("Ngăn xếp đã trống, không thể lấy phần tử")
            return None  
        value = self.stack.pop()  
        self.top -= 1              
        return value

    def display(self):
        if self.is_empty():
            print("Ngăn xếp đang trống")
            return
        print("Các phần tử trong ngăn xếp: ", self.stack)

#HÀM PRINT IN NỘI DUNG CỦA NGĂN XẾP
    def print_stack(self):
        if self.is_empty():
            print("Ngăn xếp đang trống")
        else:
            print("Nội dung của ngăn xếp từ trên xuống dưới:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])  

def main():
    size = int(input("Nhập sức chứa của ngăn xếp: "))  
    stack = Stack(size)  
    while True:
        value = input("Nhập một số (hoặc 'q' để thoát): ")
        if value.lower() == 'q':
            break
        try:
            num = float(value)
            stack.push(num)  
        except ValueError:
            print("Hãy nhập một số hợp lệ")

    stack.display()  
    stack.print_stack()  
    print("Phần tử lấy ra:", stack.pop())
    stack.print_stack()  

main()