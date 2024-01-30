import paketsains.modulemtk

hasil_tambah = paketsains.modulemtk.tambah(1,2,4,5,6,3)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = paketsains.modulemtk.kali(1,2,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_4 = paketsains.modulemtk.pangkat(3)
print(f"hasil pangkat 4 dari 5 = {pangkat_4(5)}")

from paketsains import fisika 
gaya = fisika.force(9,10) # force itu fungsi yang ada didalam file fisika
print(f"gaya adalah {gaya}")