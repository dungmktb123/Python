#Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. 
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

#ưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

input_str = input("Nhập X, Y: ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# Viết bởi Quantrimang.com
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print (multilist)