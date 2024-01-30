#        0,-1   1,-2     2,-3
data = ["ucup","Otong","dudung"]
data_0 = [0]
print(data_0)

data_terakhir = data[-1]
print(f"data terakhir adalah index [-1] = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup adalah index[-3] = {data_ucup}")

#mengambil info jumlah data

panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

#manipulasi data list

# menambahkan item pada list

print(f"data sebelum ditambah = {data}")

data.insert(1,"Asep")
print(f"data sesudah ditambah = \n{data}")

# menambah data dan meletakkannya diakhir list
data.append("Jajang")
print(f"data setelah diappend oleh jajang \n{data}")

#menambahkan data ke data

data_new = ["Ujang","Usep","Dadang"]
data.extend(data_new)
print(f"data gabungan = \n {data}")

# mengubah data x dengan data lain

# contoh ubah data ke 2 dengan mikey

data[2] = "Mikey"
print(f"data setelah diubah = \n{data}")

# menghapus data

data.remove("Ujang") # besar kecilnya harus sesuai atau hurufna harus sesuai
print(f"data remove = \n{data}")

# menghapus data paling belakang
data_akhir = data.pop()
print(f"ini adalah data akhir = \n{data}")
print(f"data terakhir oleh data.pop = {data_akhir}")