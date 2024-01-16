import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory,"modeAppend.txt")

with open(file_path,"a",encoding="utf-8") as file:
    file.write("Dadang Suradang\n")
    file.write("Otong Surotong\n")
    # ada dua teks yang ditambahkan diatas
with open(file_path,"a",encoding="utf-8") as file:
    file.write("Ucup Surucup\n")
    
    ## dapat dilihat pada teks ketika program dijalankan berulang kali, program akan menuliskan seluruh teks yang diperintahkan tanpa menggeser atau menimpa teks sebelumnya.