import os

# buat program untuk memilih menghitung luas atau keliling

# ambil input panjang dan lebar dari user
def header(choose1):
    print(f"Program menghitung {choose1}")
    print("-"*40)

def input_user():
    panjang = int(input("Masukkan nilai panjang: ")) 
    lebar = int(input("Masukkan nilai lebar: "))
    
    return panjang,lebar

#buat rumus menghitung luas
def area(panjang,lebar):
    return panjang*lebar

# buat rumus menghitung keliling
def calc_keliling(panjang,lebar):
    return 2*(panjang+lebar)

# lupa ngeprint hasilnya bang wwkwk
def hasil(choose,value):
    print(f"Hasil perhitungan {choose} = {value}")
    
# buat perulangan menggunakan while cuy

while True:
    opsi = input("1. Luas | 2. Keliling (1/2): ")
    os.system("cls")
    # buat opsi
    if opsi == "1":
        header("Luas")
        p,l = input_user()
        luas = area(p,l)
        hasil("luas",luas)
        isDone = input("Apakah ingin melakukan perhitungan kembali (y/n)?: ")
        
        if isDone == "n":
            break
        
    elif opsi == "2":
        header("Keliling")
        p,l = input_user()
        keliling = calc_keliling(p,l)
        hasil("keliling",keliling)
        isDone2 = input("Apakah ingin melakukan perhitungan kembali (y/n)?: ")
        
        if isDone2 == "n":
            break


print("Perhitungan selesai, Terimakasih!")
# mantappp
    