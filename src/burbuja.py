## Ahora que ya sabemos como funciona el algoritmo de burbuja, pasemos a la práctica. 
#Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento.


##PROCESO

def ordenar(a):
    recorrido = len(a)

    for i in range(recorrido-1): #(n-1) Primer bucle, controla numero del recorrido
        for j in range(recorrido-1-i):  #(n-1-1) Segundo recorrido del bucle, realiza comprobaciones
            if a[j] > a[j+1]: #Si el numero del recorrido es mayor que el siguiente, se intercambian
                a[j], a[j+1] = a [j+1], a[j]  #intercambia el elemento
    return a

if __name__ == "__main__":
    #ENTRADA


    a = [8, 3, 1, 19, 14]


    #SALIDA


    print("lista dada", a)
    print(f"Lista ordenada {ordenar(a)}")
