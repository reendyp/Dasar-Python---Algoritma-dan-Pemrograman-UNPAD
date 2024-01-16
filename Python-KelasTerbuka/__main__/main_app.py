# __main__ adalah top level dari environment

print(f"nilai __name__ pada main_app.py = {__name__}")

# file pada program eksternal

import fungsi # coba panggil di terminal, __name__ akan berubah menjadi __main__ saat menjalankan file fungsi.py


def tambah(a:int,b:int)->int:
    return a+b

if __name__=="__main__":
    angka1 = 9
    angka2 = 10
    hasil = tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")
    
#coba import package

import package