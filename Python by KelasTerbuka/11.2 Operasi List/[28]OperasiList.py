angka_acak = [1,2,6,9,0,5,6,7,4,5,7,9,0,2,3,1,4,2,5,6,2]
print(f"data angka acak = \n{angka_acak}")

# menghitung banyak data
jumlah_data_2 = angka_acak.count(2)
print(f"banyak angka 2 = {jumlah_data_2}")

data = ["Ucup","Ujang","Dadang","Otong"]
print(f"Data = {data}")

index_dadang = data.index("Dadang")
print(f"index dadang adalah {index_dadang}") 

# mengurutkan list

print(f"Data angka acak = \n{angka_acak}")
angka_acak.sort()
print(f"Data angka urut = \n{angka_acak}")

print(f"Daftar nama acak = \n{data}")
data.sort()
print(f"Daftar nama urut = \n{data}")

# mengurut dari belakang
angka_acak.reverse()
print(f"angka dari yang terbesar = {angka_acak}")

data.reverse()
print(f"daftar nama berurut dari alfabet terakhir = \n {data}")