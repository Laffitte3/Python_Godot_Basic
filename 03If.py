"""Crea un programa que pida al usuario su edad y determine si es mayor de edad (18 años o más), 
menor de edad (entre 0 y 17 años) o si aún no ha nacido (edad negativa). """

#Que modifiquen el valor de edad varias veces para que vayan provando
edad = 10

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 0:
    print("Eres menor de edad.")
else:
    print("Parece que aún no has nacido.")