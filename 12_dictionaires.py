"""
    Les dictionnaires sont utilisés pour stocker des valeurs de données dans 
    des paires clé/valeur.
    Un dictionnaire est une collection qui est ordonnée*, modifiable 
    et qui n'autorise pas les doublons.
"""

# Les dictionnaires s'écrivent avec des crochets, et ont des clés et des valeurs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Les éléments du dictionnaire sont présentés sous forme de paires clé/valeur 
# et peuvent être référencés en utilisant le nom de la clé.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Longueur du dictionnaire
print(len(thisdict))

# La méthode keys() renvoie une liste de toutes les clés du dictionnaire
x = thisdict.keys()
print(x)

# Vous pouvez modifier la valeur d'un élément spécifique 
# en vous référant au nom de sa clé
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# Vous pouvez modifier la valeur d'un élément spécifique 
# en vous référant au nom de sa clé
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# The pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)

# Un dictionnaire peut contenir des dictionnaires, 
# c'est ce qu'on appelle des dictionnaires imbriqués.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Créez trois dictionnaires, puis créez un dictionnaire qui contiendra 
# les trois autres dictionnaires
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Pour accéder aux éléments d'un dictionnaire imbriqué, vous utilisez le nom 
# des dictionnaires, en commençant par le dictionnaire extérieur
print(myfamily["child2"]["name"])