#Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. Giả sử đầu vào sau được cấp cho chương trình
s = input("Nhập câu của bạn: ")
# Bài tập Python 16, Code by Quantrimang.com
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])