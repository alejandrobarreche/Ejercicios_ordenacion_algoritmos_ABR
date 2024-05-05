import random

def insercion_dicotomica(lista):
    tamaño = len(lista)
    lista_nueva = [None] * tamaño  # Creamos una nueva lista para almacenar el resultado ordenado
    lista_nueva[0] = lista[0]     # El primer elemento de la tabla original se copia directamente al lista_nueva

    for i in range(1, tamaño): # Empieza en el uno porque comprobar la posición de un solo puntero no tiene sentido
        puntero = lista[i] # Llamaremos puntero a la variable que almacena temporalmente el elemento de la lista
        izquierda, derecha = 0, i - 1 #Estos son los límites en los que vamos a comprobar que esté ordenada la lista_nueva
        
        
        '''
        Con esto calculamos la posición hasta la que nos tenemos que mover en la lista_nueva
        La forma de calcularlo no es recorriendo uno a uno los elementos de la lista ordenada hasta llegar 
        a uno que no cumpla la condición. En este caso buscaremos la posición comprobando  el valor que se 
        encuentre en el medio de la lista, de tal forma que iremos cambiando los límites de acotación
        para que ese valor medio vaya cambiando, y buscar así la posición
        '''
        while izquierda <= derecha:  
            medio = (izquierda + derecha) // 2 # De esta forma estamos calculando si "puntero" está a la izquierda o a la derecha de la mitad de "lista_nueva"
            if puntero < lista_nueva[medio]: # Nuestro elemento de la lista original está a la izquierda de la mitad de la lista ordenada
                derecha = medio - 1 # Si está a la izquierda el límite superior será menor que el valor de "medio" antes de comprobar
            else:
                izquierda = medio + 1 # Si está a la derecha el límite inferior será mayor que el valor de "medio" antes de comprobar
        # En este punto, izquierda es la posición de inserción de puntero en lista_nueva
        
        '''
        Este bucle nos permite mover a la izquierda todos lo elementos ordenador que son menores
        que "puntero" y por lo tanto existe un hueco vacío en la lista ordenada donde podemos insertar
        el elemento que estabamos comparando y seguir teniendo la lista ordenada
        '''
        for j in range(i, izquierda, -1):
            lista_nueva[j] = lista_nueva[j - 1]
        lista_nueva[izquierda] = puntero

    return lista_nueva

        
        
def main():
    opcion = input("¿Desea generar una lista aleatoria? (s/n): ")
    
    if opcion.lower() == "s":
        longitud = int(input("Ingrese la longitud de la lista: "))
        lista = [random.randint(1, 100) for _ in range(longitud)]
    else:
        lista = []
        print("Ingrese un número (pulse 'x' para terminar la lista)")
        while True:
            entrada = input(">>>: ")
            if entrada.lower() == "x":
                break
            if entrada == "":
                continue
            lista.append(int(entrada))
    
    resultado_ordenado = insercion_dicotomica(lista)
    
    print("Tabla original:", lista)
    print("Tabla ordenada:", resultado_ordenado)

if __name__ == "__main__":
    main()
