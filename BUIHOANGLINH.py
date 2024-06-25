# Nhập vào từ bàn phím một từ điển (dictionary) gồm n items, mỗi item gồm mã hàng và số lượng của chúng.
d = {}
n = int(input('Nhập n:'))
for i in range(n):
    print('Nhập item thứ {}'.format(i+1))
    mh = input('Mã hàng:')
    sl = int(input('Số lượng:'))
    d[mh] = sl
# Khởi tạo một từ điển thứ hai gồm m items, mỗi item chứa mã nhà cung cấp và tên nhà cung cấp tương ứng.
# In từ điển thứ hai ra màn hình.
e = {'ncc01':'lenovo','ncc02':'asus','ncc03':'acer','ncc04':'dell'}
print(e)
# Cho biết trong từ điển thứ nhất có chứa mã hàng “H001” hay không? Nếu có, hãy sửa lại số lượng của nó thành 200.
# Nếu không có, hãy bổ sung dữ liệu mã hàng đó từ bàn phím.
if 'H001' in d : d['H001'] = 200
else :
    print('Bổ sung dữ liệu của mã hàng H001')
    mh = input('Mã hàng:')
    sl = int(input('Số lượng:'))
    d[mh] = sl
print(d)
# Xóa tất cả các mặt hàng có số lượng bằng 0 ra khỏi từ điển.
for mh in list(d.keys()):
    if d[mh] == 0:        d.pop(mh)

print(d)
# Chuyển dữ liệu của từ điển thứ nhất sang hai list. List thứ nhất chứa các mã hàng, listthứ 2 chứa các số lượng của từng item.
# In ra màn hình 3 phần tử đầu tiên (nếu có) của list thức nhất và 3 phần từ cuối cùng (nếu có) của list thứ hai
mh = list(d.keys())
sl = list(d.values())
if len(mh) >= 3:
    for i in range(3):
        print(mh[i])
if len(sl) >= 3:
    for i in range(len(sl)-1,len(sl)-4,-1):
        print(sl[i])