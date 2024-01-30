import os 
os.system("cls")
# membuat fungsi dengan def

def f_kuadrat(angka):
    return angka**2

print(f"hasil kuadrat dari 10 : {f_kuadrat(10)}")

# pakai lamda

f_quadratic = lambda angka: angka**2
print(f"hasil kuadrat dari 4 adalah {f_quadratic(4)}")

## kegunaan 

# sorting data list dengan cara biasa
data_list = ["Otong","Ucup","Dadang"]
data_list.sort()

print(f"sorted {data_list}")

# sorted by len

def sortedbylen(nama):
    return len(nama)

data_list.sort(key=sortedbylen)
print(f"data sorted by len : {data_list}")


data_list = ["Otong","Ucup","Dadang"]
data_list.sort(key =lambda nama : len(nama))
print(f"sorted by lambda with len : {data_list}")

# filter angka < x
list_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
# pake def
def kurangdari5(angka):
    return angka < 5 
list_baru = list(filter(kurangdari5,list_angka))
print(f"angka kurang dari 5 mengggunakan fungsi def : {list_baru}")

list_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
# pakai lambda
data_list_baru = list(filter(lambda x : x <5,list_angka))
print(f"angka kurang dari lima menggunakan fungsi lambda : {data_list_baru}")

list_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
# cari bilangan genap

genap = list(filter(lambda x : (x%2==0), list_angka))
print(f"angka genap mengggunakan fungsi lambda : {genap}")

# anonymous function

def pangkat(n):
    return lambda angka : angka ** n

pangkat2 = pangkat(2) # sama aja kayak pangkat(2)(5)
print(f"fungsi kuadrat dari 5 = {pangkat2(5)}") # fungsi komposisi

print(f"pangkat bebas = {pangkat(4)(5)}")