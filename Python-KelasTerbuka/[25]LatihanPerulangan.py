#coba buat segitiga siku-siku

# segitiga dengan for
sisi = 1

for i in range(4):
    print("*"*sisi)
    sisi += 1
print("good job, ren")

# segitiga dengan while

count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > 4:
        break

print("Well done, ren!")

# segitiga ganjil

ganjil = 1

while True:
    # print jika ganjil
    if ganjil%2!=0:
        print("*"*ganjil)
        ganjil +=1
        
    else:
        ganjil+=1
        continue

    if ganjil > 5:
        break   
print("kerja bagus, ren!")

