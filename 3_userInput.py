"""
    Entrée utilisateur:
    Python permet à l'utilisateur d'entrer des données.
    Cela signifie que nous pouvons demander à l'utilisateur d'entrer des données.
"""

# uses the input() method
# L'exemple suivant demande le nom d'utilisateur, et lorsque vous l'avez saisi, 
# il s'affiche à l'écran
age = input(" votre age: ")
age = int(age) + 1 # 35
print(f"age is: {age}")