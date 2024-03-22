#Lambda function
# still same with ordinary function but in diffrent way
# the purpose of lambda is to make simplyfy of function

kuadrat= lambda angka:angka**2
print(kuadrat(3))

pangkat = lambda num,pow: num**pow
print(pangkat(3,5))

#sorting list using lambda
data_list=["Denta","Andi","Nina"]
data_list.sort(key=lambda nama: len(nama))
print(f"sorted list by len = {data_list}")

#filter list using lambda
data_angka=[1,2,3,4,5,6]
data_angka_baru=list(filter(lambda x:x<5,data_angka))
print(data_angka_baru)

#even using lambda
data_genap=list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

#Anonymouse function
# currying 

#without carrying
def pangkat(angka,n):
    hasil=angka**n
    return hasil;

data_hasil=pangkat(5,2)
print(data_hasil)

#with carrying

def pangkat2(n):
    return lambda angka:angka**n
hasil_pangkat2_dengan2var=pangkat2(4)(2)
print(hasil_pangkat2_dengan2var)