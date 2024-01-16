import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory,"modeWrite.txt")

with open(file_path,"w",encoding="utf-8") as file:
    file.write("ucup\n")
    file.write("dadang")

# perintah dibawah akan menimpa teks yang telah ditulis sebelumnya
with open(file_path,"w",encoding="utf-8") as file:
    file.write("Rendy Putra Pratama")

# Mode "w" akan mengganti semua teks yang telah ditulis dengan tulisan/teks terbaru

# coba pake writelines
with open(file_path,"w",encoding="utf-8") as file: # perintah 0
    file.writelines("Selaksa Harsa\n")
    file.writelines("Fisika Universitas Padjadjaran\n")
with open(file_path,"w",encoding="utf-8") as file: # perintah 1
    file.writelines("Ata Endut\n") 
    
    # writelines mirip kayak append, tp tetep aja klo buat perintah baru file teks sebelumnya bakal dihapus sama perintah yang terbaru (perintah 1)