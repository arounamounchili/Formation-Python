"""
    Listes :
    Les listes sont utilisées pour stocker plusieurs éléments dans 
    une seule variable. Utilisés pour stocker des collections de données.
"""

# Les listes sont créées à l'aide de crochets:
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Les éléments d'une liste sont indexés: le premier élément a l'index [0],
# le deuxième élément a l'index [1], etc.
print(fruits[0])
print(fruits[2])

fruits[2] = "ananas"
print(fruits)

# Pour déterminer le nombre d'éléments d'une liste, 
# utilisez la fonction len() :
print(len(fruits))


# Vous pouvez spécifier une plage d'index en précisant le point de départ 
# et le point d'arrivée de la plage.
# Si vous spécifiez une plage, la valeur de retour sera une nouvelle 
# liste contenant les éléments spécifiés.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Ajouter des éléments
# Pour ajouter un élément à la fin de la liste, utilisez la méthode append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Pour insérer un élément de liste à un index spécifié, utilisez la méthode insert().
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# La méthode remove() supprime l'élément spécifié.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# La méthode pop() supprime l'index spécifié
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Si vous ne spécifiez pas l'index, la méthode pop() supprime le dernier élément.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# La méthode clear() vide la liste.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Tri alphanumérique d'une liste
# Les objets de type liste possèdent une méthode sort() qui trie 
# la liste par défaut de manière alphanumérique et ascendante
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Trier la liste par ordre numérique :
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Pour trier en ordre décroissant, utilisez l'argument du mot-clé reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# La méthode reverse() inverse l'ordre de tri actuel des éléments
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# Copie d'une liste
# list2 = list1 : list2 ne sera qu'une référence à list1, 
#  utiliser la méthode copy() pour faire une copie
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# La méthode list() permet de faire une copie d'une liste :
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# Rejoindre deux listes
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)