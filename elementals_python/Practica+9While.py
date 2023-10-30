# Uso de while en python
numero = 1

# Repeticion de numeros

#while numero <= 10:
#    print(numero)
#    numero += 1

# Repeticion de numeros con breakk

#while numero <= 10:
#    print(numero)
#    if numero == 6:
#        break
#    numero +=1

# Repeticion de numeros con Continue

numero2 =  0

#while numero2 <= 10:
#    numero2 +=1
#    if numero2 == 6:
#        continue
#    print(numero2)

# suma de numeros anturales

numeros = int(input("introduce un numero natural"))
result = 0
control = 1

while control <= numeros:
    result += control
    control += 1

print("La suma de numeros naturales es:", result)
