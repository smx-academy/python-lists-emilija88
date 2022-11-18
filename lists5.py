# Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na broevi, 
# da se dodadat vo lista i 
# da se najde vtoriot najgolem broj

n = int(input("Kolku broevi sakate da vnesete vo listata?"))
broevi = []
for i in range(n):
    x = int(input("Vnesete broj"))
    broevi.append(x)
print("Originalna lista e: {}".format(broevi))
broevi.sort()
broevi.reverse()
print("Vtoriot najgolem broj od listata e: {}.".format(broevi[1]))
