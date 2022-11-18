# Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi, 
# da se dodadat vo lista i 
# da se soberat site broevi vo listata


lista = []

for x in range(10):
    x = int(input("Vnesete broj"))
    lista.append(x)
zbir = sum(lista)
print(lista)
print("Zbirot na site broevi koi gi vnesovte vo listata e: {}.".format(zbir))

