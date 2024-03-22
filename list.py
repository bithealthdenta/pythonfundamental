# data campuran
print("============== DASAR LIST ==================")
data_campuran=[1,"bala-bala",2,"mendoan"]
print(data_campuran)

#cara lain membuat list 
cara_lain=range(0,10,2) # range(starts,stop,step)
data_list=list(cara_lain)
print(data_list)

# dengan pakai for
list_with_for=[i for i in range(0,10)]
print(list_with_for)
list_with_for_pangkat=[i**2 for i in range(0,10)] #dikuadratkan dengan 2
print(list_with_for_pangkat)

# dengan if dan for
list_with_if_for=[i for i in range(0,10) if i !=5]
print(list_with_if_for);
list_with_if_for1=[i for i in range(0,10) if i%2 == 0] # genap
print(list_with_if_for1);
list_with_if_for2=[i for i in range(0,10) if i%2 != 0] # ganjil
print(list_with_if_for2);

#OPERASI PADA LIST
print("=================== OPERASI PADA LIST ==============")
data=["a","b","c"]

# mengambil data dari list
data_0=data[0]
print(data_0)

# bisa dengan index (-)
data_terakhir= data[-1]
print(data_terakhir)

# mengetahui panjang
panjang_data = len(data)
print(f"panjang_data= {panjang_data}")

# manipulasi list
# menambahkan item pad alist
print(f"data sebelum = {data}")

data.insert(1,"d") #insert(posisi,item) untuk dengan posisi
print(f"data sesudah ditambah = {data}")

#menambah di akhir list
data.append("F")
print(f"data sesudah ditambah diakhir = {data}")

#menambah list dengan list
data_baru=["1","2","3"]
data.extend(data_baru)
print(f"data setelah ditambah list baru= {data}")

#mengubah data pada list
data[2]="denta";
print(f"data setelah diubah {data}")

#meremove data
data.remove("denta")
print(f"data yang sudah dihapus denta = {data}")

#count data
data_angka=[1,2,2,3,4,4,5,6,3,7,8]
jumlah_data_4= data_angka.count(4)
jumlah_data_3= data_angka.count(3)
print(f"jumlah data 4 = {jumlah_data_4}")
print(f"jumlah data 3 = {jumlah_data_3}")

#ambil index
index=data_angka.index(1)
print(f"index angka 1 = {index}")

#mengurutkan list
print(f"data angka sebelum short = {data_angka}");
data_angka.sort();
print(f"data setelah di sort = {data_angka}")

# untuk descending
data_angka.reverse();
print(f"data setelah di reverse = {data_angka}")

#melakukan duplicate copy tidak bisa dengab b=a hrus menggunakan b-a.copy()

a=[1,2]
b=[];
b=a.copy()
print(f"setelah di copy kan {b}")

#nested list
data_0=[1,2]
data_1=[3,4]

list_2d=[data_0,data_1]
list_2d_campuran=[data_0,data_1,1,2]

print(f"list 2d biasa{list_2d}")
print(f"list 2d campuran= {list_2d_campuran}")

# contoh lain nested list
peserta_0=["denta",25,"laki-laki"]
peserta_1=["Nina",28,"perempuan"]
peserta_2=["Dimas",30,"laki-lali"]

list_peserta=[peserta_0,peserta_1,peserta_2]
print(f"List Peserta = \n {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# COPY NESTING LIST
# mengambil data dri nested list
data_copy=list_2d[0][1]
print(f"data = {data_copy}")

#copy nested list dengan deepcopy

from copy import deepcopy


    

