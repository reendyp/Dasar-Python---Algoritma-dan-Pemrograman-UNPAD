import science
#from science import mathematics,physics

hasil_tambah = mathematics.tambah(9,1,2,3)
print(f"hasil tambah : {hasil_tambah}")

gaya = physics.force(9,8)
print(f"gaya adalah : {gaya}")

# file package didalam package

from science.maths import scientific
pangkat2 = scientific.pangkat(2)
print(f"hasil pangkat 2 dari 9 adalah {pangkat2(9)}")