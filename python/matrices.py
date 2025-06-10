alumnos = [
]

def buscar_alumno(nombre):
    for alumno in alumnos:
        if alumno[0].lower() == nombre.lower():
            return alumno
    return None

def agregar_o_actualizar(nombre, materia, nota):
    alumno = buscar_alumno(nombre)
    if alumno:
        print(f" El alumno '{nombre}' ya existe.")
        materias = alumno[1]
        for mat in materias:
            if mat[0].lower() == materia.lower():
                print(f" Actualizando nota de {materia} a {nota}.")
                mat[1] = nota
                return
        print(f"➕ Agregando nueva materia {materia} con nota {nota}.")
        materias.append([materia, nota])
    else:
        print(f"✅ Agregando nuevo alumno: {nombre}")
        alumnos.append([nombre, [[materia, nota]]])

while True:
    nombre = input("\nIngrese el nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break

    materia = input("Ingrese el nombre de la materia: ")
    nota = int(input("Ingrese la nota (número): "))

    agregar_o_actualizar(nombre, materia, nota)

print("\n Lista final de alumnos:")
for alumno in alumnos:
    print(alumno)
