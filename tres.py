#crear un menu de opciones 

contador = 0 

print ("***Pueblos")
print ("1.Agregar pueblos")
print ("2.Mostrar Rutas")
print ("3.Salir ")
pueblos=[]
while (contador!=3):
    pueblo={}
    contador=int(input("Digita una opcion:"))
    if(contador==1):
            print("Agregando Pueblos ")
            pueblo['Nombre']=input("Ingrese el nombre")
            pueblo['Distancia']=int(input("Ingrese la distancia"))
            pueblo['poblacion']=int(input("Ingrese los habitantes"))
    elif(contador==2):
            print(pueblos)
    elif(contador==3):
            print("Saliendo")
            break
    else:
            print("Opcion no valida")
