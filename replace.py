print ("*** GENERADO9R DE EMAILS***")

#PEDIMOS LOS DATOS AL USUARIO 

nombre = input("Ingresa tu nombre :")

#IMPRIMOMOS LOS DATOS DEL USUARIO 
print(f"EL NOMBRE A INGRESAR ES: {nombre}")

#LIMPIAMOS LOS DATOS DEL USUARIO

nombre_us = nombre.strip()

#REOMPLAZAMOS LOS ESPACIOS POR PUNTOS

nombre_us = nombre_us.replace(" ", ".")

#PASAMOS DE MAYUSCULAS A MINISCULAS 

nombre_us = nombre_us.lower()
print(f"NOMBRE NORMALIZADO : {nombre_us}")
#HACEMOS UN SALTO DE LINEA 
print("\n ")

#SUGUNDO PASO
empresa = input("Ingresa el nombre de la empresa :")

print(f"EL NOMBRE DE LA EMPRESA ES : {empresa}")

extension_dominio = ".com.co"

print(f"LA EXTENSION DE DOMINIO ES {extension_dominio}")

cad = "@"

empresa_us = empresa.strip()

empresa_us = empresa_us.replace(" ", ".")

empresa_us = empresa_us.lower()

print(f"NOMBRE DE EMAIL NORMALIZADO {empresa_us}")

print("\n ")

print(f"TU NUEVO EMAIS ES : {nombre_us}{cad}{empresa_us}{extension_dominio}")


