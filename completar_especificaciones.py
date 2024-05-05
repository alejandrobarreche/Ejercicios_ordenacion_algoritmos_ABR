import random

def está_explorado(t, inicio, fin):
    # Verificar precondición
    # Los valores de inicio y fin deben de estar en los índices de la tabla
    if not t or inicio < 0 or fin >= len(t) or inicio > fin:
        return False

    # Variable para llevar el máximo del segmento
    maximo = t[inicio] # Ponemos un elemento de la tabla y no 0 para que en caso de error, la tabla que devuelva siempre esté formada por los mismos elementos que los que había al principio
    

    # Encontrar el máximo del segmento
    for i in range(inicio + 1, fin + 1):
        if t[i] > maximo:
            maximo = t[i]

    # Verificar las condiciones del segmento
    for i in range(inicio, fin + 1):
        if t[i] == maximo:
            # Hacer copia de seguridad del máximo del segmento
            mi = t[i]

            # Desplazar los elementos del segmento una celda hacia la izquierda
            for j in range(i, inicio, -1):
                t[j] = t[j - 1]

            # Colocar el elemento más grande del segmento "en lo alto"
            t[inicio] = mi
            return True

    return False  # Si no se encontró el máximo correctamente



def main():
    opcion = input("¿Desea generar una lista aleatoria? (s/n): ")
    
    if opcion.lower() == "s":
        longitud = int(input("Ingrese la longitud de la lista: "))
        t = [random.randint(1, 100) for _ in range(longitud)]
    else:
        t = [int(x) for x in input("Ingrese una lista de números separados por espacio: ").split()]
    
    inicio = int(input("Ingrese el índice de inicio del segmento a explorar: "))
    fin = int(input("Ingrese el índice de fin del segmento a explorar: "))

    print("Tabla original:", t)
    print("Explorando segmento...")
    if está_explorado(t, inicio, fin):
        print("Tabla después de explorar:", t)
    else:
        print("No se pudo explorar el segmento.")

if __name__ == "__main__":
    main()
