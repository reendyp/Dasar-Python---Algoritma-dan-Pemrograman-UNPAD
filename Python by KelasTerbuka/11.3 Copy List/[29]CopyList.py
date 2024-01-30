# teknik meng-copy list

a = ["Dudung","Otong", "Ujang"]

b = a # hanya mengganti variabel saja
print(f"a ={a}")
print(f'b = {b}')

# address a dan b adalah sama, sehingga jika kita mengubah data di a, b akan ikut berubah

a[1] = "Miky"
print(f"data a setelah diubah = {a}")
print(f"data b ikut berubah = {b}")

# cek address
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

c = a.copy()

print(f"address c = {hex(id(c))}")
print(f"data c = {c}")

# ubah data c

c[0] = "Bruce"
print(f"data c setelah diubah = {c}")