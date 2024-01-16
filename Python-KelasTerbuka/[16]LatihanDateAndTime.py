# latihan : date and time

import datetime as dt

hari_ini = dt.date.today()
print(f"hari ini tanggal {hari_ini}" )

tanggal = dt.date(2003,5,20)
print(f"tanggal lahir saya adalah {tanggal}")

# menebak hari lahir
print(f"Masukkan tanggal, \n bulan dan tahun \n lahir anda")
# deskripsiin tahun tanggal dan bulan pada saat lahir
tanggal = int(input("Tanggal \t:"))
bulan   = int(input("Bulan \t\t:"))
tahun   = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")

print(f"harinya adalah : {tanggal_lahir:%A}") # pake fungsi %A buat nebak senin

umur_hari = hari_ini - tanggal_lahir
print(f"umur anda dalam hari adalah {umur_hari}")

umur_tahun = umur_hari.days/365
print(f"umur anda dalam tahun adalah {umur_tahun} tahun")

umur_bulan_sisa = (umur_hari.days%365)//30
print(f"umur anda adalah {umur_tahun} tahun, {umur_bulan_sisa} bulan")