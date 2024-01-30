print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")
print(f""""
      a. Addition 
      b. Subtraction
      c. Multiplication
      d. Division
      """)
a = "Addition"
b = "Subtraction"
c = "Multiplication"
d = "Division"

operation = input("Choose your operation = ")
print(operation)

if operation == "a".lower:
    x = float(input("Masukkan angka pertama = "))
    y = float(input("Masukkan angka kedua = "))
    
    z = x+y
    print(f"hasil penjumlahan {x} dengan {y} adalah {z}")
elif operation == "b".lower:
    x = float(input("Masukkan angka pertama = "))
    y = float(input("Masukkan angka kedua = "))
    z = x-y
    print(f"hasil pengurangan {x} dengan {y} adalah {z}")
elif operation=="c".lower:
    x = float(input("Masukkan angka pertama = "))
    y = float(input("Masukkan angka kedua = "))
    z = x*y
    print(f"hasil perkalian {x} dengan {y} adalah {z}")
elif operation=="d".lower:
    x = float(input("Masukkan angka pertama = "))
    y = float(input("Masukkan angka kedua = "))
    z = x/y
    print(f"hasil pembagian {x} dengan {y} adalah {z}")
else : 
    print("Menu lain")