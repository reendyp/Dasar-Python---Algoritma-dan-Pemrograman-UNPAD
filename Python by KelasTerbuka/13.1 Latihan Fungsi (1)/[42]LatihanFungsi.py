import os
os.system("cls")

# program menghitung nilai luas dan keliling
# panjang, lebar, rumus luas, rumus keliling

# mengambil input user
def from_user():
    panjang = int(input("Masukkan nilai panjang: "))
    lebar =int(input("Masukkan nilai lebar: "))
    
    return panjang,lebar

# menghitung luas
def hitung_luas(panjang,lebar):
    return panjang*lebar

# menghitung keliling
def hitung_keliling(panjang,lebar):
    return 2*(panjang+lebar)

def display(message,value):
    print(f"Hasil perhitung {message} = {value}")
# looping menghitung nilai luas dan keliling

while True:
    os.system("cls")
    
    l,p = from_user()
    luas = hitung_luas(l,p)
    keliling = hitung_keliling(l,p)
    
    display("luas",luas)
    display("keliling", keliling)
    
    isDone = input("Apakah ingin lanjut (y/n)? ")
    
    if isDone == "n":
        break
    
print("Perhitungan telah selesai, Terimakasih!")