# def nama_fungsi(argument):
    # isi fungsi
import os
os.system("cls")

def say_hi(nama):
    '''Fungsi say hi dengan nama sebagai input'''
    print(f"Hai, {nama}. Selamat Pagi!\n")

say_hi("Rendy")
print("*"*20)
# fungsi dengan list sebagai argument

def say_hello(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"    Hallo, {peserta}!")

anggota = ["Ucup","Dadang","Otong"]
say_hello(anggota)

# fungsi dengan default argument
# jika tidak ada argument dari user, program akan menjalankan argument default
print("-"*20)

def hello_world(nama="user"):
    print(f"Hi, {nama}. Apa kabar?")

hello_world("rendy")
hello_world()

# fungsi dengan default argumen
def penjumlahan(input1=1,input2=2,input3=3,input4=4):
    hasil = input1+input2+input3+input4
    return hasil
print(penjumlahan()) # jika tidak ada input yang diubah
print(penjumlahan(input3=10)) # kita bisa mengkustomisasi salah satu nilai input tanpa harus mengubah default nilai input yang lain

# fungsi dengan return
print("-"*20)
def math_operation(angka_1,angka_2):
    '''fungsi operasi matematika sederhana'''
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    
    return tambah, kurang, kali, bagi
k,l,m,n =  math_operation(10,2)

print(f"\nhasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil perkalian = {m}")
print(f"hasil pembagian = {n}")