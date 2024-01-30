data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep si kasep"
}
# yang keluar key nya
for teman in data_dict:
    print(teman)

# ngebuat list key    
keys = data_dict.keys()
print(keys)

#manggil pake list key
for key in data_dict.keys():
    print(data_dict.get(key))

#ngebuat list value    
value = data_dict.values()
print(value)

# print pake list value
for value in data_dict.values():
    print(value)
    
# ngebuat list item = key,value    
item = data_dict.items()
print(item)

# print pake items
for item in data_dict.items():
    print(item)
    
for key,value in data_dict.items():
    print(f"{key},{value}")
