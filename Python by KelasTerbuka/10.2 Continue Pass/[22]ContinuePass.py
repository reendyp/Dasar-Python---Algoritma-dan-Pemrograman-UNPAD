# pass  --> berfungsi sebagai dummy, tidak akan dieksekusi

#angka = 0
#while angka <5:
#    angka += 1
#    if angka ==3:
#        pass
        
#    print(angka)

# continue    

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang ->  {angka}") #aksi 1
    
    if angka == 3:
        print("nice") # ini aksi 1
        continue # akan mengcutoff proses loop yang harusnya berlanjut ke aksi 2 namun kembali ke aksi 1
    
    print("whatssup") #aksi 2
print("finish")