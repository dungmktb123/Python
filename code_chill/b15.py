#Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. 
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
# Bài tập Python 14, viết bởi Quantrimang.com
print (','.join(value))