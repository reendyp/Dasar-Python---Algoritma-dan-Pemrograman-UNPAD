# operator dictionary

data_dict = {
    "cup" : "ucup serucup",
    "otong" : 'otong surotong',
    "dung" : "dudung surudung"
}

# panjang dict

lendict = len(data_dict)
print(f"Panjang dictionary : {lendict}")

#check key exist

key = "cup"
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# mengakses value dengan get
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # ada pesan yang bisa diberikan jika data tidak ditemukan berbeda dengan print(data_dict["ucup"]) yang lgsg memberika warning error

# mengupdate data

data_dict["cup"] = "ucup si ganteng"
print(data_dict)

data_dict.update({"cup": "ucup serucup"})
print(data_dict)
#nambahin data

data_dict.update({"rendy" : 140310230037})
print(data_dict)