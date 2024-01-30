import modulemtk # bisa pake as x atau variabel yang mempermudah
# from modulemtk import tambah, kali, pangkat kalo pake ini gaperlu pake modulemtk.tambah(), cukup langsung tambah() dst, 

# from modulemtk import tambah as add. langsung aja add(12,23,4,5) dst

hasil_tambah = modulemtk.tambah(1,2,4,5,6,3)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = modulemtk.kali(1,2,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_4 = modulemtk.pangkat(3)
print(f"hasil pangkat 4 dari 5 = {pangkat_4(5)}")