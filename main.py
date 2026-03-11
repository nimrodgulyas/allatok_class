from allat import Allat
from emlos import Emlos, Macska, Kutya
allat1 = Allat("Bodri", "kutya", 5, "kert", "közepes")
allat2 = Allat("Cirmi", "macska", 3, "ház", "közepes")

print(allat1)
print(allat2)

emlos1 = Emlos("Morzsi", "kutya", 5, "kert", "barna")
emlos2 = Emlos("Cicó", "macska", 2, "kert", "cirmos")

print(emlos1)
print(emlos2)

macska1 = Macska("Hubert", 4, "ház", "fehér")
print(macska1)
macska1.dorombol()

kutya1 = Kutya("Cézár", 7,  "udvar", "fekete")
print(kutya1)
kutya1.ugat()