# fromkeys 
import os
import datetime as dt
import random
import string

template_mahasiswa = {
    'nama' : 'nama',
    'nim' : '0000',
    'sks_lulus' : 0,
    'lahir' : dt.datetime(1111,1,11)
}



# ambil input dari user
# bikin looping

data_mahasiswa = {} # data kosong
while True:
    os.system("cls")
    
    print(f"{'Selamat Datang':^20}")
    print(f"{'Data Mahasiswa':^20}")
    print("*"*20)

    mahasiswa = dict.fromkeys(template_mahasiswa.keys())


    mahasiswa["nama"] = input("Nama : ")
    mahasiswa["nim"] = str(input("NIM : "))
    mahasiswa["sks_lulus"] = int(input("SKS Lulus : "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31) : "))
    mahasiswa["lahir"] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY =''.join((random.choice(string.ascii_uppercase) for i in range (6))) # generate 6 random string
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'LAHIR':<10}")
    print("-"*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa # konstanta pakai kapital
        
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {LAHIR:<10}")
    print("\n")

    is_done = input("Ingin menambahkan data kembali? (y/n)")
    if is_done != "y":
        break
    
print("Data Saved!")
# bikin looping

