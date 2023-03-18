t = 0 
notlar = [90,72,81,77]
for e in notlar:
    t += e 
ortalama = t/len(notlar) 
print(ortalama)

# e'nin bir önemi yok. Kulannacapımmız için önemli
for i in range(5):
    print('iteration' ,i)

for i in range(len(notlar)):
    t +=notlar[i]
ortalama2 = t/len(notlar)
print('Ortalama:',ortalama2)

# Aşağıdaki gibi yaparsan listeye ulaşığ değerleri değiştirebilrisin.
#for i in range(len(notlar)):
 #   notlar[i] += 5
#print (notlar)


#Öğretmen 2. öğrenci hariç herkesin kağıdını beş arttıracak. 
for i in range(len(notlar)):
    if i == 1:
        continue
    
    notlar[i] += 5
    
print (notlar)

#hem key hem de valuelarda iterasyon yapmamızı sağlar.
#for k,v in d.items():
#    print("key değeri:", k, "value değeri:", v)
