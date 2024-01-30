salam = 'bro!'
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

salam2 = "HaI AWkWkkWkk"
print("normal = " + salam2)
salam2 = salam2.lower()
print("lower = " + salam2)

# pengecekan dengan isX method

salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))

# isalpha() -> mengecek apakah semua str adalah huruf
# isalnum() -> mengecek apakah huruf dan angka
# isdecimal() -> mengecek apakah desimal
# isspace() -> spasi,tab, newline in
# istitle() -> semua kata dimulai dengan huruf besar

judul = "It's Okay Not To Be Okay"
cek_judul = judul.istitle()

print(judul + " is title " + str(cek_judul))

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()

print(judul + " is title " + str(cek_judul))

spasi = "cek satu "
cek = spasi.isspace()
print("apakah ada spasi pada" + str(cek))

# cek komponen startswith() endswith()

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")  # apakah kalimat dimulai dari Sangjangnim

print("Start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print('End = ' + str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(gabungan)
gabungan2 =' '.join(pisah)
print(gabungan2)

gabung = 'akuxsayangxkamu'
pisah = gabung.split("x")
print(pisah)

# alokasi karakter

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah1 = "tengah".center(20,"#")
print("'"+tengah1+"'")