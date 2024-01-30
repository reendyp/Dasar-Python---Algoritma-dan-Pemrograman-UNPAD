import os
os.system("cls")

# fungsi dengan args
def say_hello(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    
    # data dalam bentuk tuples
    print(f"saya {nama}, tinggi {tinggi}, berat {berat}")
    
say_hello("ucup surucup",180,90) # data tuples

# fungsi dengan keyword args
def say_hi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    
    print(f"saya {nama}, tinggi saya {tinggi}, berat saya {berat}")
    
say_hi(nama="ucup",tinggi=170,berat=90)

# gabungan kwargs dan args
#kwargs bisa ngasih variabel. contoh : option = "value"
def fungsi1(*args, **kwargs):
    if kwargs["option"] == "tambah":
        output = 0
        for data in args:
            output += data
    elif kwargs["option"] == "kali":
        output = 1
        for data in args:
            output *= data
    return output

hasil = fungsi1(1,2,3,4,option="tambah")
print(f"hasil jumlah: {hasil}")
hasil = fungsi1(1,2,3,4,option="kali")
print(f"hasil kali: {hasil}")