#Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

j=[] #Tạo một danh sách rỗng để lưu kết quả
for i in range(2000, 3201): #Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200
    if (i%7==0) and (i%5!=0): #Kiểm tra xem số i có chia hết cho 7 và không phải là bội số của 5 không
        j.append(str(i)) #Nếu đúng, thì thêm số i vào danh sách result
print (','.join(j)) #In ra màn hình danh sách result, các phần tử cách nhau bằng dấu phẩy