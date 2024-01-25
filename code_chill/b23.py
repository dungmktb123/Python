# #Viết chương trình Python nhập một mảng hai chiều các số thực A (m hàng, n cột) từ bàn phím.

# a. Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột

# b. Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử này.

# c. Trong mảng A có bao nhiêu phần tử bằng phần tử lớn nhất.

import numpy as np

# Nhập mảng A từ bàn phím
m, n = map(int, input("Nhập số hàng và số cột của mảng A (cách nhau bởi dấu cách): ").split())
A = np.zeros((m, n))
for i in range(m):
    row = list(map(float, input(f"Nhập dòng {i+1} của mảng A, cách nhau bởi dấu cách: ").split()))
    A[i, :] = row

# Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
max_col = np.amax(A, axis=0)
min_col = np.amin(A, axis=0)
print("Giá trị lớn nhất trên mỗi cột:", max_col)
print("Giá trị nhỏ nhất trên mỗi cột:", min_col)

# Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A cùng với chỉ số hàng và cột của 2 phần tử này
max_val = np.amax(A)
max_idx = np.unravel_index(np.argmax(A), A.shape)
min_val = np.amin(A)
min_idx = np.unravel_index(np.argmin(A), A.shape)
print("Phần tử lớn nhất của mảng A là", max_val, "ở dòng", max_idx[0]+1, "cột", max_idx[1]+1)
print("Phần tử nhỏ nhất của mảng A là", min_val, "ở dòng", min_idx[0]+1, "cột", min_idx[1]+1)

# Tính số phần tử bằng phần tử lớn nhất
count_max = np.count_nonzero(A == max_val)
print("Số phần tử bằng phần tử lớn nhất là:", count_max)