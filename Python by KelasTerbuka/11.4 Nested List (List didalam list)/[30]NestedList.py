# list didalam list

basic_data = [1,2]
basic_data2 = [3,4]
print(f"Contoh data standar {basic_data} dan {basic_data2}")

nested_data = [basic_data,basic_data2]
print(f"Contoh nested data = {nested_data}\n") # list didalam list

# contoh

peserta0 = ["Ucup",20,"Laki-laki"]
peserta1 = ["Otong",19,"Laki-laki"]
peserta2 = ["dedeh",18,"Wanita"]

data_peserta = [peserta0,peserta1,peserta2]

for peserta in data_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")
    
# dengan reference

list_copy = data_peserta.copy()
print(f"list peserta = {list_copy}")

peserta0[0] = "Dadang"
print(f"Data peserta awal= \n{data_peserta}") # data awal tidak diubah => hasil ikut berubah ketika data peserta0 diubah

print(f"copy data peserta setelah diubah = \n{list_copy}")