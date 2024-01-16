import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory,"modeR+.txt")

with open(file_path,"r+",encoding="utf-8") as file:
    file.write("Baris - 1\n")
    file.write("Baris - 2\n")

with open(file_path,"r+",encoding="utf-8") as file:
   file.write("Ganti")  #Kata Ganti akan menimpa kata Baris pada Baris - 1, r+ akan menyesuaikan panjang dari data. Ganti memiliki 5 huruf, baris juga 5 huruf 

with open(file_path,"r+",encoding="utf-8") as file:
    file.write("bARIS")
    
    # Mode r+ akan menimpa teks sebelumnya dengan panjang karakter yang diganti mengikuti panjang karakter pengganti, misal pada kata baris ditimpa oleh kata ganti, sehigga, kata baris dengan tepat ditimpa oleh kata baris

