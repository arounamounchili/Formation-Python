# En Python, le type de données est défini lorsque vous 
# attribuez une valeur à une variable. 

"""
Chiffres Python
Il existe trois types de nombres en Python (int, float, complex)
"""
# int => positive or negative, without decimals
x = 23 
x = -24

# float => positive or negative, containing one or more decimals
y = 23.5
y = -34.643
y = 12E0    # e ou E indique la puissance de 10

# complex => on utilise j comme partie imaginaire
z = 4 + 1j
z = -4j

print(type(x))
print(type(y))
print(type(z))


"""
    Conversion de type
    Les méthodes int(), float() et complex() permettent de convertir 
    un type en un autre.
"""
x = 10  # int
y = 4.5 # float
z = 3j  # complexe

#conversion de int en float :
a = float(x)    # 10.0

#conversion de float à int :
b = int(y) # b = 4

#conversion de int en complexe :
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))