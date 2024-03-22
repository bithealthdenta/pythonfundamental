#if steatment
# nama=input("Siapa nama anda? ")

# count =0;
# if "a" in nama:
#     print(f"ada a di {nama}")
#     count+=1;
# if "i" in nama:
#     print(f"ada i di {nama}")
#     count+=1;
# if "u" in nama:
#     print(f"ada u di {nama}")
#     count+=1;
# if "e" in nama:
#     print(f"ada e di {nama}")
#     count+=1;
# if "o" in nama:
#     print(f"ada o di {nama}")
#     count+=1;
# if count==0:
#     print(f"tidak ada huruf vokal di {nama}")

# Looping
angka2=[0,1,2,3,4]
count=0;
for i in range(len(angka2)):
    count+=i
print(count)

count=0;
ii=0;
while ii < len(angka2):
    count+=angka2[ii]
    ii+=1
print(count);

#excercise

tinggi=int(input("berapa tinggi segitiga? "))

count=1;
for i in range(tinggi):
    print("*"*count);
    count+=1;
    if count< tinggi:
        continue

    
