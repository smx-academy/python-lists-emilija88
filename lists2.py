# Da se napravi programa vo koja korisntikot ke moze da vnese proizvolen broj na broevi, 
# da se dodadat vo lista i 
# da se najde najgolemiot broj

n = int(input("Kolku broevi sakate da vnesete vo listata?"))
lista = []
for i in range(n):
    x = int(input("Vnesete broj"))
    lista.append(x)
print(lista)
print("Najgolemiot broj od listata e: {}.".format(max(lista)))
