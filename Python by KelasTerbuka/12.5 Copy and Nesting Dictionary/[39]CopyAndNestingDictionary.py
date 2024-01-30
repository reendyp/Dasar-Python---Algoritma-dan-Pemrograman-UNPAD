import datetime as dt

mahasiswa1 = {
    'nama' : 'Ucup surucup',
    'nim' : 140310230001,
    'sks_lulus': 130,
    'beasiswa' : False,
    'lahir' : dt.datetime(2002,10,10)
}
mahasiswa2 = {
    'nama' : 'Dadang Suradang',
    'nim' : 140310230002,
    'sks_lulus': 140,
    'beasiswa' : True,
    'lahir' : dt.datetime(2000,2,29)
}
mahasiswa3 = {
    'nama' : 'Asep si Kasep',
    'nim' : 140310230003,
    'sks_lulus': 120,
    'beasiswa' : True,
    'lahir' : dt.datetime(2001,2,21)
}

data_mahasiswa = {
    'mah1' : mahasiswa1,
    'mah2' : mahasiswa2,
    'mah3' : mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<10}")

print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa # konstanta pakai kapital
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA =  data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
    # ^ = Center; < = rata kiri ; > = rata kanan