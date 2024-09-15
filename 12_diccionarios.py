numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers[2])

information = {"nombre": "jean",
               "apellido": "zambrano",
               "altura": 1.70,
               "edad": 25}
print(information)
information["apellido"] = "hernandez"
del information["edad"]
print(information)

claves = information.keys()
print(claves)
print(type(claves))

values = information.values()
print(values)

pairs = information.items()
print(pairs)

contacts = {"jean": {"apellido": "zambrano",
             "altura": 1.70,
             "edad": 25},
             "carla": {"apellido": "florida",
             "altura": 1.60,
             "edad": 29}}
print(contacts["jean"])
print(contacts["jean"]["apellido"])