"""Escribe un programa que tome como entrada un número del 1 al 7 y
 muestre el día de la semana correspondiente (por ejemplo, 1 para lunes, 2 para martes, etc.).
   """

#El input es para poder ingresar datos por teclado(Este no lo utilizaremos mucho)
#Explicale a los estudiantes estos pero si no estas segura preguntale a gemini
#Explicarles que si el operador ==
#Para que funcione en la terminal deben escribir el numero

dia = int(input("Ingrese un número del 1 al 7: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Número inválido.")