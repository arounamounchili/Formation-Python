"""
    En python, les chaînes de caractères sont entourées soit 
    de guillemets simples, soit de guillemets doubles.
"""

print("Minteligencia")
print('Minteligencia')

# Affecter une chaîne de caractères à une variable
name = "Ngannou"
print(name)

# Chaînes multilignes en utilisants trois guillemets doubles
# ou trois guillemets simples
paragraph = """Bonjour ceci est une autre facon
de travailler avec des  strings qui vont sur plusieurs lignes."""
print(paragraph)


"""
    Slicing/Découpage: Vous pouvez renvoyer une plage de caractères 
    en utilisant la syntaxe de découpage.
"""
#  [start:stop:step]
hello_world = "Hello, world!"
print(hello_world[2:5]) # Obtenez les caractères de la position 2 à la position 5 (non inclus)

hello_world = "Hello, world!"
print(hello_world[:5]) # Obtenez les personnages du début jusqu'à la position 5 (non incluse)

hello_world = "Hello, world!"
print(hello_world[2:]) # Obtenez les caractères à partir de la position 2, et ce jusqu'à la fin


"""
    Modifier les chaînes de caractères
"""

# Majuscules: la méthode upper() renvoie la chaîne en majuscules
hello_world = "Hello, world!"
print(hello_world.upper())

# Minuscules: La méthode lower() renvoie la chaîne en minuscules
hello_world = "Hello, world!"
print(hello_world.lower())

# Supprimer les espaces blancs/vides: La méthode strip() supprime tout espace blanc 
# au début ou à la fin de la chaîne
hello_world = "  Hello, world! "
print(hello_world)
print(hello_world.strip())

# Remplacer la chaîne: La méthode replace() remplace une chaîne 
# de caractères par une autre chaîne de caractères
hello_world = "Hello, world!"
print(hello_world.replace("H", "G"))

# Fractionner une chaîne de caractères: La méthode split() renvoie une liste 
# dans laquelle le texte entre le séparateur spécifié devient les éléments 
# de la liste
hello_world = "Hello, world!"
print(hello_world.split(","))


"""
    Concaténation de chaînes de caractères
"""
# Pour concaténer, ou combiner, deux chaînes de caractères, 
# vous pouvez utiliser l'opérateur +

firstname = "Abdel"
lastname = "Jordan"
name = firstname + " " + lastname
print(name)