AÑO_ACTUAL=2022


nombre=input("1. ¿Cuál es tu nombre? ")
primer_apellido=input("2. ¿Cuál es tu primer apellido? ")
segundo_apellido=input("3. ¿Cuál es tu segundo apellido? ")
año_nacimiento=int(input("4. ¿En qué año naciste? "))
fecha_nacimiento=input("5. ¿En qué mes y día naciste? (En el siguiente formato 'mm-dd' )")

nombre_completo=(nombre+ " "+ primer_apellido +" "+ segundo_apellido)

print(f"A. Este es tu nombre completo en mayúsculas: {nombre_completo.upper()}")
print(f"B. Este es tu nombre completo en minúsculas: {nombre_completo.lower()}")
print(f"C. Esta es tu fecha de nacimiento {fecha_nacimiento}-{año_nacimiento}")

edad=AÑO_ACTUAL-año_nacimiento
print(f"D. Esta es tu edad: {edad} años.")

n_vocales= 0
for letra in nombre_completo.lower():
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        n_vocales+=1
print(f"E. Tu nombre completo tiene {n_vocales} vocales")

len_nombre=len(nombre)+len(primer_apellido)+len(segundo_apellido)
print(f"F. Tu nombre completo tiene {len_nombre} letras")


print(f"G. ¿Tu edad es un carácter de tipo número? {type(edad)==int}")

print(f"H. ¿Tu nombre completo es un carácter de tipo alfanumérico? {type(nombre_completo)==str}")

print(f"I. Tu edad en 10 años será: {edad+10} años")

print(f"J.La media de tu edad actual y tu edad en 20 años es {((edad+20)+edad)/2} años")