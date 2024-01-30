data_0 = [1,2] # 0,1 
data_1 = [3,4] # 1,1

data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()

print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

#mengambil unit data
data = data_2d[1][1]
print(f"data = {data}")

# cek address

print(f"addres data asli = {hex(id(data_2d))}")
print(f"addres data copy = {hex(id(data_2d_copy))}")
print(40*"#")
# cek address unit data
print(f"cek salah satu address unit data: ")
print(f"addres data asli ke 0 = {hex(id(data_2d[0]))}")
print(f"addres data copy ke 0 = {hex(id(data_2d_copy[0]))}") # address sama, maka copy data tidak sampai ke unit yang ada didalamnya (tidak mendetail)

# coba ganti unit data yang terjadi data copy ikut berubah

data_2d[0][1] = 10
print(f"data modifikasi asli = {data_2d}")
print(F"data copy juga ikut berubah = {data_2d_copy}")

# namun jika yang diubah list yang ada didalam list, maka data copy tidak akan berubah
data_2d = [data_0,data_1,100]
data_2d[2] = 8 # mengubah dari 100 menjadi 8 pada data_2d => [[1,2],[3,4],8]
print(f"data modifikasi asli = {data_2d}")
print(F"data copy tidak ikut berubah = {data_2d_copy}")
print(50*"$")
# pake deep copy
# akan meng-copy secara rekursif atau satu persatu tiap itemnya
from copy import deepcopy

data_2d = [data_0,data_1,100]
data_2d_deepcopy = deepcopy(data_2d)

print(f"address asli = {hex(id(data_2d))}")
print(f"address data deep copy = {hex(id(data_2d_deepcopy))}")

# cek address tiap unit data

print(f"address data asli ke-0= {hex(id(data_2d[0]))}")
print(f"address data deep copy ke-0 = {hex(id(data_2d_deepcopy[0]))}")

# coba ubah data member guis

data_2d[0][1] = 250

print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}") # ikut berubah karena ga dilakukan deep copy
print(f"data deep copy = {data_2d_deepcopy}") # tidak berubah karena dilakukan deep copy. Setiap elemen dicopy secara rekursif atau satu per satu