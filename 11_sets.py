"""
    Les Sets(ensembles) sont utilisés pour stocker plusieurs éléments dans une 
    seule variable. Un ensemble est une collection non ordonnée, 
    non modifiable* et non indexée.
"""

# Créer un ensemble :
thisset = {"apple", "banana", "cherry"}
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(thisset)

# Les ensembles ne peuvent pas comporter deux éléments de même valeur
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True et 1 sont considérés comme la même valeur
thisset = {"apple", "banana", "cherry", True, 1, 2, False}
print(thisset)

# Obtenir la longueur d'un ensemble
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Vous ne pouvez pas accéder aux éléments d'un ensemble en vous référant 
# à un index ou à une clé. En revanche, vous pouvez parcourir les éléments 
# d'un ensemble à l'aide d'une boucle for, ou demander si une valeur 
# spécifiée est présente dans un ensemble, en utilisant le mot-clé in.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Once a set is created, you cannot change its items, 
# but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Pour ajouter des éléments d'un autre ensemble à l'ensemble actuel, 
# utilisez la méthode update().
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Pour supprimer un élément d'un ensemble, utilisez la méthode remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# La méthode clear() vide l'ensemble
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)




