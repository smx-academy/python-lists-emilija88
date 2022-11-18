# Da se napravi programa koja ke bide upotrebuvana vo nekoja prodavnica za prodazba. 
# Korisnikot da moze da vnesuva produkti se dodeka ne izbere deka saka da plati. 
# Produktitte da se dodavaat vo edna lista, cenite vo druga lista. 
# Koga ke izbere deka saka da plati da mu se ispecatat produktite i cenite vo nalik na "fiskalna smetka". 
# Da ima moznost korisnikot da plati i da se presmeta dali i kolku treba da mu se vrati kusur.

produkti = []
ceni = []
zbir = 0
while True:
    x = input("Vnesete produkt")
    produkti.append(x)
    y = int(input("Vnesete cena za {}:".format(x)))
    ceni.append(y)
    zbir+=y
    nov=input("Dali sakate da vnesete nov produkt?")
    if nov.lower() == "da":
        pass
    else:
        break
print("Na vashata fiskalna smetka imate: {}. Suma za plakanje: {}.".format(produkti,zbir))
z=int(input("Koja suma ja vnesuvate pri plakanje(vo denari)?"))
razlika=z-zbir
print("Imate za vrakjanje {}den".format(razlika))
print("Vo vashata koshnichka gi imate slednite proizvodi: {}.".format(produkti))
print("Vi blagodarime na doverbata.")