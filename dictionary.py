data_dict={
    "name":"denta",
    "umur":22,
    "jenis-kelamin":"laki-laki"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary = {LENDICT}")

#mengecek key exist atau tidak
KEY="name"
CHECKKEY= KEY in data_dict
print(f"apakah {KEY} ada di dict: {CHECKKEY}")

#mengakses value (read) dengan get
print(data_dict["name"])
print(data_dict.get("name")) # lebih baikk pkai get agar tidak return eror jika kosong

#update data
data_dict["name"]="nina"

#bisa menggunahan update jika add dan update, karena jika not found auto update
data_dict.update({"status":"single"})

#delete dictionary
del data_dict['umur']

# LOOPING DICTIONARY
friends={
    "club1":"denta nina",
    "club2":"jeje cenggur"
}

#loop keluar key saja
for teman in friends:
    print(teman) # akan keluar keynya saja
#untuk ambil isinya
for key in friends.keys():
    print(friends.get(key))

keys= friends.keys() # untuk ambil key saja
value= friends.values() # untuk ambil valuenya
items=friends.items() #ambil key dan value

for key,value in friends.items():
    print(f"keys= {key}, value= {value}")

# NESTED DICTIONARY

import datetime
mahasiswa1={
    'nama':'denta',
    'nim':"612015002",
    'sks_lulus' : 100,
    'beasiswa': False,
    'lahir': datetime.datetime(2000,2,29)
}

mahasiswa2={
    'nama':'Nina',
    'nim':"612015003",
    'sks_lulus' : 100,
    'beasiswa': False,
    'lahir': datetime.datetime(2000,2,29)
}
mahasiswa3={
    'nama':'Jeje',
    'nim':"612015004",
    'sks_lulus' : 80,
    'beasiswa': True,
    'lahir': datetime.datetime(2000,2,29)
}

data_mahasiswa={
    "MAH001":mahasiswa1,
    "MAH002":mahasiswa2,
    "MAH003":mahasiswa3
}
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa.keys():
    KEY=mahasiswa
    NAMA=data_mahasiswa[KEY]['nama']
    NIM=data_mahasiswa[KEY]['nim']
    SKS=data_mahasiswa[KEY]['sks_lulus']
    BEASISWA=data_mahasiswa[KEY]['beasiswa']
    LAHIR=data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")

