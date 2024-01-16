print("Selamat datang di PaintMan v1.0")

jml_dinding = int(input("Jumlah dinding: "))


luas_total = 0
for i in range(jml_dinding):
    
    print("~~")
    print(f"Dinding {i+1}")
    p = float(input("Panjang (m): "))
    l = float(input("Lebar (m): "))
    
    luas = p*l
    print(f"Luas (m2): {luas:.2f}")
    luas_total += luas
    
print("~~~~")
print(f"Luas total dari semua dinding adalah {luas_total} m2")
