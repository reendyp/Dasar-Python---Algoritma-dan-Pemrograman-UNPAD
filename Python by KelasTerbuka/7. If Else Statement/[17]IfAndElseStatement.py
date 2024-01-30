nama = input("Siapa nama anda?")
print(f"Nama anda adalah {nama}")

# if kondisi: aksi

# program if inline
if nama=="Rendy": print("Kamu pasti bisa!")
print(f"Terimakasih, {nama}!")

# program if dengan indentation
nama1 = input("Siapa ya?")
if nama1=="Sersa":
    # jika terdapat dalam satu indentasi maka masih dalam satu aksi
    print("Berpetualang mengejar impian")
    print("Sersa Bisa!")
print(f"Semangat, {nama1}")

nama2 = input("Siapa ya?")

if nama2 == "Sersa":
    print("Semangat ya!")
else:
    print("Kamu keren")
print("yaudah")