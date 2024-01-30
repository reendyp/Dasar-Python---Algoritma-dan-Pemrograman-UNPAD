# operator yang dapat dilakukan dengan penyingkatan

# 1. Operasi tambah dengan assignment

a = 5
print('nilai a =',a)
#a = a+1 dapat ditulis sebagai berikut a +=1
#print('nilai a =',a)

a += 1
print('nilai a+=1 =',a)

a -= 2 #hasilnya 4, karena nilai a = 6
print('nilai a-=2 =',a)

a *= 5 #hasilnya 20 karena nilai sebelumnya adalah 20
print('nilai a*=5 =',a)

a /= 2
print('nilai a /= 2 =',a)

b = 10
print('\nnilai b = ',b)

b %= 3 # 10 dibagi 3 tersisa 1
print('nilai b %= 3 =',b)

b //= 3 # 10 dibagi 3 tersisa 1
print('nilai b //= 3 =',b)

a = 5 
print("nilai a = ",a)
a**=3
print("nilai a**=3 = ",a)


# operasi bitwise

c = True
print("nilai c = ",c)

c |= False
print("nilai c| False, nilai c menjadi = ", c)