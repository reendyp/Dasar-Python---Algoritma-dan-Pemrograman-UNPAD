# tipe data : angka satuan yang tidak ada koma (integer)

data_integer = 11
print("Data : ", data_integer)
print('- bertipe : ', type(data_integer))

# tipe data : angka dengan koma (float)
data_float = 1.5
print('data = ', data_float)
print('- bertipe : ', type(data_float))

# ti[e data : kumpulan karakter (string)
data_string = 'rendy 37'
print('data : ', data_string)
print('- bertipe : ', type(data_string))

#tipe data : biner true/false (boolean)

data_bool = False
print('data : ', data_bool)
print('- bertipe : ', type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6) # complex(real number, imaginer number)

print('data : ', data_complex)
print('- bertipe : ', type(data_complex))

# Penggunaan tipe data dari bahasa C 
from ctypes import c_double
data_c_double = c_double(10.5)
print('data : ', data_c_double)
print('- bertipe : ', type(data_c_double))