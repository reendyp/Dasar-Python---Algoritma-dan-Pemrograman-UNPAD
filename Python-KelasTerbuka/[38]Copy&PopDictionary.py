teman_teman = {
    "cup" : "ucup surucup",
    "dung" : "dudung surudung",
    "tong" : "otong surotong",
    "sep" : "asep si kasep"
}
# setelah di copy, reference dari friends berbeda dengan teman_teman, ubah data pada friends tidak akan mengubah data pada teman_teman, berlaku sebaliknya
friends = teman_teman.copy()
print(f"teman teman = {teman_teman}\n")
print(f"friends = {friends}\n")

friends["cup"] = "dadang suradang"
print(f"data ucup pada friend diganti = {friends}\n")
print(f"data teman_teman tetap = {teman_teman}\n")

# mengambil data pada dictionary
# .pop(isi key yang ingin diambil)
FirstData = friends.pop("cup")
print(f"Fungsi .pop() mengambil data yang ada didalam () : {FirstData}\n")

# .popitem() = engambil data terakhir

lastData= friends.popitem()
print(f".popitem() mengambil data terakhir : {lastData}\n ")
print(f"data setelah .popitem() dan .pop(cup) : {friends}\n")