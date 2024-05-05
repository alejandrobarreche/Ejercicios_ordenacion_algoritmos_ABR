import random

def ordenacion_topologica(n, restricciones):
    # Creamos una lista de listas para representar el grafo
    grafo = [[] for _ in range(n)] # [[], [], [], [], []]
    
    
    # Creamos una lista para almacenar los grados de entrada de cada tarea
    grados_entrada = [0] * n #[0, 0, 0, 0, 0] siendo cada cero el numero de veces que una tarea se encuentra en una restricción como "tarea siguiente"
    
    
    # Creamos una lista para almacenar el orden final de las tareas
    orden_final_tareas = [] 


    # Construimos el grafo y calculamos los grados de entrada de cada tarea
    for restriccion in restricciones:
        (tarea_ant, tarea_sig) = restriccion  # Decimos que una restricción definida por una tupla, el primer número define la tarea que va antes y el segundo la tarea la tarea que irá después
        
        
        grafo[tarea_ant - 1].append(tarea_sig - 1)  # Restamos 1 para ajustar los índices
        # En las posiciones correspondientes a las tareas añadimos a las tareas que tienen que ir después 
        
        
        grados_entrada[tarea_sig - 1] += 1 #Almacena el número de tareas posteriores para cada tarea, siendo en un principio 0 a no ser que esté en la primera tarea de alguna restricción

    # Inicializamos una cola con tareas que no tienen dependencias (grado de entrada cero)
    cola = [i for i in range(n) if grados_entrada[i] == 0]

    # Recorremos el grafo
    while cola: # Al ir eliminando elementos de la lista cola, mientras haya elementos en la lista se ejecuta el bucle
        tarea = cola.pop(0) # Se va eliminando el primer elemento de la lista
        orden_final_tareas.append(tarea + 1)  # Se añade el elemento a la lista final


        # Una vez hemos añadido un elemento a la lista final hay que añadir las tareas que van después de estos elementos
        
        for siguiente_tarea in grafo[tarea]:
            grados_entrada[siguiente_tarea] -= 1
            # Si el grado de entrada se vuelve cero, añadimos la tarea a la cola
            if grados_entrada[siguiente_tarea] == 0:
                cola.append(siguiente_tarea)

    # Si no se pudieron visitar todas las tareas (hay un ciclo), devolvemos None
    if len(orden_final_tareas) != n:
        return None
    else:
        return orden_final_tareas
    
    
    
    
def main():
    # Solicitar al usuario el número de tareas
    n = int(input("Ingrese el número de tareas: "))
    
    opcion = input("¿Desea generar restricciones aleatorias? (s/n): ")
    
    numero_restricciones = int(input("Ingrese el número de restricciones que van a tener estas tareas: "))
    
    if opcion.lower() == "s":
        # Generar restricciones aleatorias
        restricciones = [(random.randint(1, n), random.randint(1, n)) for _ in range(numero_restricciones)]
    else:
        # Solicitar al usuario las restricciones
        restricciones = []
        print("Ingrese las restricciones.")
        for i in range(numero_restricciones):
            tarea_ant = int(input(">>> Ingrese la primera tarea: "))
            tarea_sig =  int(input(">>> Ingrese la segunda tarea: "))
            print(f"La restricción {i+1} es la siguiente:")
            print(f"({tarea_ant},{tarea_sig})")
            print()
            restricciones.append((tarea_ant, tarea_sig))
    
    print(f"Las restricciones son las siguientes: {restricciones}")
    # Obtener el orden topológico de las tareas
    orden = ordenacion_topologica(n, restricciones)
    
    if orden is None:
        print("No se puede ordenar debido a restricciones contradictorias.")
    else:
        print("Orden de tareas:", orden)

if __name__ == "__main__":
    main()