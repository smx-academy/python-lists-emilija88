# Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na iminja, 
# da se dodadat vo lista i 
# da se najde najdolgoto ime

n = int(input("Kolku iminja sakate da vnesete vo listata?"))
iminja = []
for i in range(n):
    x = input("Vnesete ime")
    iminja.append(x)
print("Listata so iminja e slednava: {}".format(iminja))
name = max(iminja, key=len)
print("Najdolgoto ime od listata e: {}.".format(name))