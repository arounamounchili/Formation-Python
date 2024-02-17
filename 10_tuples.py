"""
    Les tuples sont utilisés pour stocker plusieurs éléments dans une seule variable.
    Un tuple est une collection ordonnée et inchangeable.
    Les n-uplets s'écrivent avec des crochets ronds.
"""

# Créer un Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Les tuples permettent de dupliquer les valeurs
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Taille d'un tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Pour créer un tuple avec un seul élément, vous devez ajouter une virgule
# après l'élément, sinon Python ne le reconnaîtra pas comme un tuple.
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Les éléments d'un tuple peuvent être de n'importe quel type de données
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")


# Accéder aux éléments d'un tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Indexation négative
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
