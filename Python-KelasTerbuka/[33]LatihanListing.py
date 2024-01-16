print(10*"=","Daftar Buku",10*"=")

list_buku = []

while True:
    print(10*"=","Daftar Buku",10*"=")
    
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    
    daftar_buku = [judul,penulis]
    list_buku.append(daftar_buku)
    
    print("=========Data Buku=========")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
        
    lanjut = input("Apakah anda ingin mendaftarkan buku kembali? (y/n)")
    
    if lanjut == "n":
        break
print("Buku telah didata!")