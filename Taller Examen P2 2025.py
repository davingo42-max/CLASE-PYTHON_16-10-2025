#DAVID LEONARDO RUBIO CONTRERAS

trabajadores = [
    ("1", "Mauricio Peñaranda", "MauriPe@email.com","Gerente de ventas",[("Diapositivas conferencia", "pendiente"), ("Instruir a los nuevos", "completado")]),
    ("2", "Luis Perez", "Lupez@yahoo.es","Pasante",[("Realizar el inventario de la sala B", "pendiente")]),
    ("3", "Kassandra moreno", "KassMoreno@yahoo.es","Oficinista",[])
    ]

#CLASES PARA EL MENU PRINCIPAL---------------------------------------------------

def Id_trabajador(lista):#C
    if not lista:
        identificacion = 1
    else:
        ultimo_id = lista[-1][0]
        identificacion = int(ultimo_id) + 1
    return str(identificacion)

def Agregar_trabajador():#C
    id=Id_trabajador(trabajadores)
    while True:
        nombre=input("Digite el nombre del nuevo trabajador: ")
        contacto=input("Digite el contacto/correo: ")
        rol=input("Digite el rol:  ")
        if not nombre or not contacto or not rol:
            print("Por favor, digite toda la informacion pedida. Gracias...")
        else:
            break
    
    trabajador_nuevo=(id, nombre, contacto, rol,[])
    trabajadores.append(trabajador_nuevo)
    print(f"El trabajador {nombre} fue agregado con la identificacion: {id}")

def Mostra_trabajador():#R
    for id, nombre, contacto, rol, trabajo in trabajadores:
        print(f"\nID: {id} \nNOMBRE: {nombre}, {contacto}, {rol}, \ntrabajo:{len(trabajo)}\n{'-'*25}")


def Actualizar_contacto_trabajador():#U
    identificador_str = input("Digite el ID del trabajador para actualizar su CONTACTO: ")

    indice_a_actualizar, trabajador_actual = Buscar_trabajador(trabajadores, identificador_str)

    if indice_a_actualizar is not None:
        id_actual, nombre_actual, contacto_actual, rol_actual, tareas_actuales = trabajador_actual
        
        nuevo_valor = input("Digite el nuevo CONTACTO/correo: ")
        
        trabajador_actualizado = (id_actual, nombre_actual, nuevo_valor, rol_actual, tareas_actuales)
        
        trabajadores[indice_a_actualizar] = trabajador_actualizado
        print(f"Contacto del trabajador con ID {identificador_str} actualizado a: {nuevo_valor}")
    else:
        print(f"Error: No se encontró un trabajador con ID {identificador_str}.")

def Actualizar_rol_trabajador():#U
    identificador_str = input("Digite el ID del trabajador para actualizar su ROL: ")

    indice_a_actualizar, trabajador_actual = Buscar_trabajador(trabajadores, identificador_str)

    if indice_a_actualizar is not None:
        id_actual, nombre_actual, contacto_actual, rol_actual, tareas_actuales = trabajador_actual
        
        nuevo_valor = input("Digite el nuevo ROL: ")
        
        trabajador_actualizado = (id_actual, nombre_actual, contacto_actual, nuevo_valor, tareas_actuales)
        
        trabajadores[indice_a_actualizar] = trabajador_actualizado
        print(f"Rol del trabajador con ID {identificador_str} actualizado a: {nuevo_valor}")
    else:
        print(f"Error: No se encontró un trabajador con ID {identificador_str}.")

def Eliminar_trabajador():#D
    identificador_str = input("Digite el ID del trabajador a ELIMINAR: ")

    indice_a_eliminar, trabajador_actual = Buscar_trabajador(trabajadores, identificador_str)

    if indice_a_eliminar is not None:
        nombre_eliminado = trabajador_actual[1]
        del trabajadores[indice_a_eliminar]
        
        print(f"\n¡Éxito! El trabajador '{nombre_eliminado}' (ID: {identificador_str}) ha sido ELIMINADO del sistema.")
    else:
        print(f"\nError: No se encontró un trabajador con ID {identificador_str} para eliminar.")


def Buscar_trabajador(lista, identificador_str):#U and D
    for i, trabajador in enumerate(lista):
        if trabajador[0] == identificador_str:
            return i, trabajador
    return None, None

#CLASES PARA EL MENU TAREAS--------------------------------------------------------------------------

def Agregar_tarea():#C
    identificador_str = input("Digite el ID del trabajador para asignarle una TAREA: ")
    indice_trabajador, trabajador_actual = Buscar_trabajador(trabajadores, identificador_str)

    if indice_trabajador is not None:
        id_actual, nombre_actual, contacto_actual, rol_actual, tareas_actuales = trabajador_actual
        
        nombre_tarea = input("Nombre de la nueva tarea: ")
        
        if not nombre_tarea:
            print("El nombre de la tarea no puede estar vacío.")
            return

        nueva_tarea = (nombre_tarea, "pendiente")
        
        tareas_actuales.append(nueva_tarea)
        
        print(f"Tarea '{nombre_tarea}' asignada a {nombre_actual} (ID: {identificador_str}) como 'pendiente'.")
    else:
        print(f"Error: No se encontró un trabajador con ID {identificador_str}.")

def Mostrar_tareas():#R
    identificador_str = input("Digite el ID del trabajador para ver sus TAREAS: ")
    indice_trabajador, trabajador_actual = Buscar_trabajador(trabajadores, identificador_str)

    if indice_trabajador is not None:
        nombre_actual = trabajador_actual[1]
        tareas_actuales = trabajador_actual[4]
        
        print(f"\n--- Tareas de {nombre_actual} (ID: {identificador_str}) ---")
        if not tareas_actuales:
            print("No hay tareas asignadas a este trabajador.")
        else:
            for i, (nombre, estado) in enumerate(tareas_actuales):
                print(f"  {i+1}. Tarea: {nombre} | Estado: {estado}")
        print("-" * 40)
    else:
        print(f"Error: No se encontró un trabajador con ID {identificador_str}.")


def Actualizar_tarea():#U
    identificador_str = input("Digite el ID del trabajador para actualizar una TAREA: ")
    indice_trabajador, trabajador_actual = Buscar_trabajador(trabajadores, identificador_str)

    if indice_trabajador is None:
        print(f"Error: No se encontró un trabajador con ID {identificador_str}.")
        return

    id_actual, nombre_actual, contacto_actual, rol_actual, tareas_actuales = trabajador_actual
    
    if not tareas_actuales:
        print(f"{nombre_actual} no tiene tareas para actualizar.")
        return

    Mostrar_tareas() 

    try:
        idx_tarea = int(input("Digite el NÚMERO de la tarea a actualizar (1, 2, ...): ")) - 1
        
        if 0 <= idx_tarea < len(tareas_actuales):
            nombre_tarea_actual = tareas_actuales[idx_tarea][0]
            nuevo_estado = input("Digite el NUEVO ESTADO ('pendiente' o 'completado'): ").lower()

            if nuevo_estado not in ("pendiente", "completado"):
                 print("Estado no válido. Debe ser 'pendiente' o 'completado'.")
                 return
            
            tarea_actualizada = (nombre_tarea_actual, nuevo_estado)
            tareas_actuales[idx_tarea] = tarea_actualizada
            
            print(f"Estado de la tarea '{nombre_tarea_actual}' actualizado a '{nuevo_estado}' para {nombre_actual}.")

        else:
            print("Número de tarea no válido.")

    except ValueError:
        print("Entrada no válida. Por favor, digite un número.")


def Eliminar_tarea():#D
    identificador_str = input("Digite el ID del trabajador para ELIMINAR una TAREA: ")
    indice_trabajador, trabajador_actual = Buscar_trabajador(trabajadores, identificador_str)

    if indice_trabajador is None:
        print(f"Error: No se encontró un trabajador con ID {identificador_str}.")
        return

    nombre_actual = trabajador_actual[1]
    tareas_actuales = trabajador_actual[4]
    
    if not tareas_actuales:
        print(f"{nombre_actual} no tiene tareas para eliminar.")
        return

    Mostrar_tareas() 

    try:
        idx_tarea = int(input("Digite el NÚMERO de la tarea a ELIMINAR (1, 2, ...): ")) - 1
        
        if 0 <= idx_tarea < len(tareas_actuales):
            nombre_tarea_eliminada = tareas_actuales[idx_tarea][0]
            del tareas_actuales[idx_tarea]
            
            print(f"Tarea '{nombre_tarea_eliminada}' eliminada de {nombre_actual}.")
        else:
            print("Número de tarea no válido.")
            
    except ValueError:
        print("Entrada no válida. Por favor, digite un número.")

#MENU TAREA------------------------------------------------------------------------------
def menu_tareas():
    while True:
        print(f"\n--- MENU TAREAS ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas de un trabajador")
        print("3. Actualizar estado de una tarea")     
        print("4. Eliminar tarea")
        print("5. Volver al menú principal")

        opcion = input("Opción: ")

        if opcion == '1':
            Agregar_tarea()
        elif opcion == '2':
            Mostrar_tareas()
        elif opcion == '3':
            Actualizar_tarea()
        elif opcion == '4':
            Eliminar_tarea()
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

#MENU PRINCIPAL------------------------------------------------------------------------------
def menu_principal():
    i=0
    while True or i<20:#Esto es innecesario, pero igual lo puse como para darle un limite fijo al codigo
        i+=1
        if i==20:
            print("\nDemasiadas acciones realizadas. Cerrando programa...")
            break
        print("\n" + "="*25)
        print("     MENU PRINCIPAL  ")
        print("="*25)
        print("1. Agregar trabajador")
        print("2. Mostrar los trabajadores")
        print("3. Actualizar contacto de trabajador")
        print("4. Actualizar rol de trabajador")
        print("5. Eliminar trabajador")
        print("6. Acceder al menu 'Tareas'")
        print("7. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            Agregar_trabajador()
        elif opcion == '2':
            Mostra_trabajador()
        elif opcion == '3':
            Actualizar_contacto_trabajador()
        elif opcion == '4':
            Actualizar_rol_trabajador()
        elif opcion == '5':
            Eliminar_trabajador()
        elif opcion == '6':
            menu_tareas()
        elif opcion == '7':
            print("\nSaliendo del sistema.")
            break
        else:
            print("\nOpción no válida.")

menu_principal()
