#1 menyambung string (concatenate)

nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama +" "+ nama_tengah +"'" +nama_akhir

print(nama_lengkap)

#2 menghitung panjang string

pjg = len(nama_pertama)
print(pjg)

#3 operator str
# mengecek apakah ada komponen char atau str pada string

d ="d"
status = d in nama_lengkap
print("string " + d + " ada di "+ nama_lengkap+ "=" + str(status))

D ="D"
status = D in nama_lengkap
print("string " + D + " ada di "+ nama_lengkap+ "=" + str(status))

d ="d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di "+ nama_lengkap+ "=" + str(status))

# mengulang string
print("wk"*10)

# indexing []

print("Index ke-0 : " + nama_lengkap[0] )
print("Index ke-[-1] : " + nama_lengkap[-1] )
print("Index ke-[3:8] : " + nama_lengkap[3:8] )
print("Index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2] )
print("Indek ke-[0:4]" + nama_lengkap[0:4])

# item max or min

print("Paling kecil : "+ min(nama_lengkap))
print("Paling besar : "+ max(nama_lengkap))

ascii_code = ord(" ")
print('ASCII code untuk spasi adalah ' + str(ascii_code))
data = 117
print('char untuk ascii 117 adalah '+chr(data))

# operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada " + data + "=" + str(jumlah))