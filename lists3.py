# Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na elementi, 
# da se ispecati listata i 
# korisnikot da moze da izbere kolku elementi i koi elementi ke gi izbrise

n = int(input("Kolku broevi sakate da vnesete vo listata?"))
lista = []
for i in range(n):
    x = int(input("Vnesete broj"))
    lista.append(x)
print("Originalna lista e: {}".format(lista))

x = int(input("Koj element sakate da go izbrisete od listata?"))
if x in lista:
    lista.remove(x)
print(lista)

