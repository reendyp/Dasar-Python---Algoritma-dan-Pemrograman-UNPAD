data  = [3,6,7,89,22,17]
print("for loop ez")
# for loop ez ges
for angka in data:
    print(f"angka = {angka}")
    
# for loop pake range uhui

data  = [3,6,7,89,22,17]

# tentuin dlu berapa banyak data pake len()
print("\nfor loop dan range pake len() cuy")
banyak_data = len(data)
for i in range(banyak_data):
    print(f"angka = {data[i]}")
    
print("\nWhile loop ceunah")

data  = [3,6,7,89,22,17]
# tetep pake range buat nandain loopingnya berhenti
banyak_data = len(data)

# nilai awal i = 0
i = 0
while i < banyak_data:
    print(f"angka = {data[i]}")
    # tambah i dengan 1 secara terus menerus, supaya i yang ada didalam data bisa kebaca semuanya
    i += 1
    
# list comprehension

print("\nList Comprehension")

data_mix = ["ucup",5,6,99,"otong","dadang"]

[print(f"data = {i} ") for i in data_mix]

data  = [3,6,7,89,22,17]

data_kuadrat = [i**2 for i in data]
print(data_kuadrat)

print("\nEnumerate") # bisa ganti for loop dan range karena akan memberikan informasi terkait index tiap unit data

data_mix = ["ucup",5,6,99,"otong","dadang"]

for index,data in enumerate(data):
    print(f"index data {data} = {index}")