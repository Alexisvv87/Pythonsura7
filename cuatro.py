#Crear menu empanadas inteligentes

contador = 0
empanadas=[]


print ("Empanadas Inteligentes")
print ("1.Agregar Empanadas")
print ("2.Mostrar empanadas")
print ("3.Salir ")

while (contador!=3):
    ingredientes=[]
    empanada={}
    contador=int(input("Digite la opcion"))
    if (contador==1):
        empanada['nombre']=input("Digite el mombre de la empanada")
        for i in range (3):
            ingredientes.append (input(f"Digite el ingrediente{i+1}:"))
        empanada ['ingredientes']=ingredientes
        empanada['precio']=int(input("Precio"))
        empanadas.append(empanada)
        
    elif (contador==2):
        print("mostrar empanadas")
        print(empanadas)

    elif (contador==3):
        print("Saliendo")
        break
    else:
        print("Opcion no valida")





