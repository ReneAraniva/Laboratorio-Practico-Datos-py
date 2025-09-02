# Ejercicio 1: Simulación de un Historial de Navegación
Historial = []#Pila vacia para agregar paginas

# Funciones para manejar el historial

# Agrega una pagina al historial
def agregar_pagina(pagina):
    Historial.append(pagina)#Metodo para agregar
    print(f"Página agregada: {pagina}")

# Retrocede a la última página visitada(borrandola)
def retroceder():
    if Historial:
        pagina = Historial.pop()#Metodo para borrar
        print(f"Retrocediendo a la página: {pagina}")
    else:
        print("No hay páginas en el historial.")

# Muestra el historial completo
def mostrar_historial():
    print("Historial de navegación:")
    for pagina in reversed(Historial):
        print(f"- {pagina}")

# Simulación de navegación  
print("---"*17)
#Agrega las paginas 
agregar_pagina("www.ejemplo1.com")
agregar_pagina("www.ejemplo2.com")
print("---"*17)
#Muestra el historial
mostrar_historial()
print("---"*17)
#Elimina la última página
retroceder()
print("---"*17)
#Muestra el historial modificado
mostrar_historial()

#Ejemplo con input simulado de usuario
#Bucle con while 
while True:
    print("\nOpciones:")
    print("1. Agregar página")
    print("2. Retroceder")
    print("3. Mostrar historial")
    print("4. Salir")
    opcion = input("Seleccione una opción: ") #Input del usuario

    if opcion == "1":
        pagina = input("Ingrese la URL de la página: ")
        agregar_pagina(pagina)
    elif opcion == "2":
        retroceder()
    elif opcion == "3":
        mostrar_historial()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente de nuevo.")#Si no se elige una opción válida