"""
Les variables sont des conteneurs permettant de stocker des valeurs de données.
Pour creer une variable on doit lui donner une nom et assigner une valeur.
"""

# Exemple
x = 10
y = 12.5
nom = "Minteligencia"
print(x)
print(y)
print(nom)

# Comme dans d'autres langage de programmation, en Python on a pas besoin
# de preciser le type de la variable. On peut aussir changer le type
# d'une variable a tout moment.
a = 45
a = "Python"

""" Connaitre le type d'une variable en utilisant la fonction 'type' """
print(type(x))
print(type(y))
print(type(nom))


""" Nom des Variables """
# Une variable peut avoir un nom court comme x et y ou un nom plutot 
# descriptive comme age, nom_de_famille.

# C'est quoi la difference entre ces deux variables? -> une est plus descriptive
age = 23
x = 34

# Les noms des variables sont sensibles a la casse
prenom = "John"
Prenom = "Fosso"
print(prenom)
print(Prenom)

# Variables avec beaucoup de mots
# - Snake Case: Nous allons utiliser cette convention
taille_de_personne = 1.75

""" Exercice: Creer une variable appele nomDeSociete et donne lui la
    la valeur 'Mercedes' et afficher le resultat.
"""
nom_de_societe = "Mercedes"
print(nom_de_societe)

print(f"La nom de ma societé est: {nom_de_societe}.")