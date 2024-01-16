import os
print(3*"=", "Membaca File Txt", 3*"=")
# Mendapatkan path lengkap direktori saat ini
current_directory = os.path.dirname(os.path.abspath(__file__))

# Menggabungkan path lengkap dengan nama file
file_path = os.path.join(current_directory, 'data.txt') #gabungin directory skrg sama name filenya

# cek status
# Membuka file
with open(file_path, mode='r') as file:
    # Lakukan operasi baca file di sini
    print(f"status read : {file.readable()}")
    print(f"status write : {file.writable()}")
    
    print(3*"=","Membaca Text File External",3*"=")
    
    # Membaca dan mencetak seluruh isi file
    #print(file.read())
    
    # membaca dan mencetak baris perbaris
    #print(file.readline(),end=" ") # cetak baris 1 # end=" " mengganti \n dengan string kosong
    #print(file.readline()) # cetak baris 2
    # dst

    # membaca semua baris sebagai list
    print(file.readlines())
    
# karena pake with open jadi gaperlu di close
#file.close()
#print(f"apakah file sudah ditutup: {file.closed}") 