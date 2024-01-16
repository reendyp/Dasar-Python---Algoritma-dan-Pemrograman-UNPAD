''' *args'''

# memasukkan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi{tinggi} dan berat {berat}")

fungsi("ucup",170,67)

# coba pake list

def fungsi1(data_list):
    data = data_list.copy()
    
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi1(["dadang",178,87])

def fungsi_args(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi_args("rendy",175,80)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    
    return output

hasil = tambah(1,2,3,4)
print(f"Hasil tambah = {hasil}")    