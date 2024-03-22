def hello_world():
    print("hello world")

def hello_worldd(nama):
    print(f"Nama anda {nama}")

for i in range(5):
    hello_world()

hello_worldd("denta")

#function with one return
def sum(a,b):
    c=a+b
    return c;

d=sum(1,2)
print(d);

#function with mmore than one return
def sumandmean(a,b):
    c=a+b;
    d=c/(a*b)
    return c,d

ans1,ans2=sumandmean(2,2)
print(f"{ans1} {ans2}")

# function with default argument
def printname(name="Default"):
    print(f"hello {name}")

printname("Denta")
printname()

def pangakt(angka, pangkat=2):
    hasil=angka ** pangkat
    return hasil

funchasil=pangakt(pangkat=5, angka=2)
funchasil2=pangakt(angka=3)
print(funchasil)
print(funchasil2)

# function with hints
def pangkat_sepuluh(nilai:int=2) -> int: 
    hasil=10 ** nilai
    return hasil

hasilpangkatsepuluh=pangkat_sepuluh(3)
hasilpangkatsepuluh2=pangkat_sepuluh()

print(hasilpangkatsepuluh)
print(hasilpangkatsepuluh2)

#FUNCTION WITH *ARGS (*)
def fungsi(*args):
    nama=args[0]
    tinggi=args[1]
    berat=args[2]
    print(f"{nama} {tinggi} {berat}")
fungsi("denta",120,20);

#another benefit using args
def tambah(*data):
    output=0
    for angka in data:
        output+=angka
    return output

hasil=tambah(1,2)
hasil2=tambah(1,2,3,4)
print(f"{hasil} {hasil2}")

#function with *kwargs
# make function becomde dictionary
def fungsi(**kwargs):
    print(kwargs["nama"])
fungsi(nama="denta",tinggi=120, berat=80)

