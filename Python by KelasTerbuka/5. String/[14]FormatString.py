# string
nama = "marlene"

format_str = f"hello {nama}"
print(format_str)

# angka

angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# boolean

boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 17
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 2000000
format_str = f"angka = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.5364820
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.5364820
format_str = f"desimal = {angka:010.2f}"
print(format_str)

# menampilkan tanda +-
angka_negatif = -10
angka_positif = 90
format_minus = f"angka minus = {angka_negatif}"
format_plus = f"angka plus = {angka_positif:+d}"  #+d atau +f sesuai dengan format angka float(menampilkan beberapa angka dibelakang koma ex : +.2f) atau integer
print(format_minus)
print(format_plus)

# memformat presentase
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder {}

harga = 1000
jumlah = 5
format_string = f"harga total = Rp.{harga*jumlah}"
print(format_string)

# format angka = binary, octal, hex, hexadecimal

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)