import numpy as np

def vecinput(name):
    n = int(input(f'Nhập số phần tử của mảng {name}:'))
    a = [0]*n
    for i in range(n):
        a[i] = int(input(f'{name}[{i}] = '))
    return a

def create_dict_from_input():
    d = {}
    while True:
        key = input("Nhập key (nhấn Enter để dừng nhập): ").strip()
        if key == "":
            break
        value = input(f"Nhập giá trị cho key '{key}': ").strip()
        d[key] = value
    return d

# # Sử dụng hàm để tạo dictionary từ nhập liệu từ bàn phím
# my_dict = create_dict_from_input()
# print("Dictionary từ nhập liệu bàn phím:", my_dict)

def create_dict_from_lists(keys,values):
    if len(keys) != len(values):
        print (ValueError,'Số lượng phần tử hai danh sách không bằng nhau.')
        return
    d = dict(zip(keys,values))
    return d

def vec2Dinput(name):
    n = int(input('Nhập số dòng của mảng: '))
    m = int(input('Nhập số cột của mảng: '))
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            x = float(input(f'{name}[{i}][{j}] = '))
            b.append(x)
        a.append(b)
    return a

def writefile(a):
    f = open('C:/Users/ADMIN/Desktop/MATRIX.txt', mode='w')
    f.write(str(len(a)) + ' ')      #ghi số dòng
    f.write(str(len(a[0])) + '\n')  #ghi số cột

    for i in range(len(a)):
        for j in range(len(a[0])):
            f.write(str(a[i][j]) + ' ')
        f.write('\n')
    f.close()

a = vecinput('a')
print('Mảng a:',a)
a.sort()
print('Mảng sau khi sắp xếp tăng dần:',a)

a.sort(reverse=-1)
print('Mảng sau khi sắp xếp giảm dần:',a)

b = vecinput('b')
print('Mảng b:',b)

d = create_dict_from_lists(a,b)
print('Dictionary được tạo từ 2 mảng trên: ',d)

c = vec2Dinput('c')
print('Mảng 2 chiều sau khi nhập: ',c)

writefile(c)

s = 0
for i in range(len(c)):
    for j in range(len(c[0])):
        if c[i][j] % 2 == 0: s+=c[i][j]
print(s)