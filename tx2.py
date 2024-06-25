import numpy as np
import matplotlib.pyplot as mp
def nhapmang(name,n):
    a = np.random.rand(n)
    for i in range (n):
        a[i] = float(input(f'{name}[{i}] = '))
    return a

def to2D(a,n):
    try:
        t = int(input('Nhập số dòng của mảng:'))
        if n % t!=0: raise ValueError
        k = a.reshape(t,n//t)
        return k
    except:
        print(ValueError,'Không thểt reshape!')
        return

n = int(input('Nhập số phần tử của mảng đầu tiên:'))
a = nhapmang('a',n)

m = int(input('Nhập số phần tử của mảng thứ hai:'))
b = nhapmang('b',m)

c = to2D(a,n)
print(c)

d = np.where((a%3==0)&(a%2==0))
print(a[d])

a = np.sort(a,kind='heapsort')
b = b[::-1]
e = np.concatenate((a,b))
print(e)

explode = [0.1,0.1, 0.1, 0.1, 0.1, 0.1]
color = ('orange','blue','red','gray','purple','white')
wp = { 'linewidth' : 1,'edgecolor' : 'black' }
mp.title('BIỂU ĐỒ MẢNG A')
mp.pie(a,labels=a, explode=explode, colors=color, wedgeprops=wp,
       shadow = True, autopct = '%.2f')
mp.show()
