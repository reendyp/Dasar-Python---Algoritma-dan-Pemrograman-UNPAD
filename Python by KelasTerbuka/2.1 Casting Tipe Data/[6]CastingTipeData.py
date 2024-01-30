# Mengubah suatu tipe data ke tipe data yang lain

# Mengubah type data integer ke tipe data yang lain
print('Integer => tipe data lain')
data_integer = 10;
print('tipe data : ', data_integer, '- bertipe : ',type(data_integer))

data_float = float(data_integer)
data_string = str(data_integer)
data_bool = bool(data_integer)

print('tipe data : ', data_float, '- bertipe : ',type(data_float)) # akan false jika nilai = 0
print('tipe data : ', data_string, '- bertipe : ',type(data_string))
print('tipe data : ', data_bool, '- bertipe : ',type(data_bool))

# Mengubah tipe data float ke tipe data yang lain

data_float = 1.5
print('tipe data : ', data_float, '- bertipe : ',type(data_float))

data_integer = int(data_float)
data_string = str(data_float)
data_bool = bool(data_float)

print('Float => tipe data lain')

print('tipe data : ', data_integer, '- bertipe : ',type(data_integer)) 
print('tipe data : ', data_string, '- bertipe : ',type(data_string))
print('tipe data : ', data_bool, '- bertipe : ',type(data_bool))

data_string = '37'
print('tipe data : ', data_string, '- bertipe : ',type(data_string))

print('String => tipe data lain')

data_bool = bool(data_string)
data_integer = int(data_string)
data_float = float(data_string)

print('tipe data : ', data_integer, '- bertipe : ',type(data_integer)) # akan error jika ada karakter selain angka
print('tipe data : ', data_float, '- bertipe : ',type(data_float))
print('tipe data : ', data_bool, '- bertipe : ',type(data_bool))


# Mengubah tipe data bool ke tipe data yang lain

data_bool = False
print('tipe data : ', data_bool, '- bertipe : ',type(data_bool))

print('Boolean => tipe data lain')

data_string = str(data_bool)
data_integer = int(data_bool)
data_float = float(data_bool)

print('tipe data : ', data_integer, '- bertipe : ',type(data_integer)) # akan error jika ada karakter selain angka
print('tipe data : ', data_float, '- bertipe : ',type(data_float))
print('tipe data : ', data_string, '- bertipe : ',type(data_string))