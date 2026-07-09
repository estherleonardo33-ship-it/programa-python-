# --------------------------------------------------------
# Estudiante: Mileth Esther Leonardo Ramos
# grupo: 213022_168
# programa: Fundamentos de Programación
# Código Fuente: autoría propia 
# --------------------------------------------------------

# Función para calcular el total de horas y clasificar la jornada
def calcular_horas(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Matriz con los recursos y las horas trabajadas de lunes a viernes
recursos = [
    ["Carlos", 8, 8, 9, 8, 9],
    ["María", 8, 8, 8, 8, 8],
    ["Juan", 10, 9, 8, 9, 8],
    ["Ana", 7, 8, 7, 8, 7]
]

print("=" * 60)
print("REPORTE DE HORAS TRABAJADAS")
print("=" * 60)

# Recorrer la matriz
for recurso in recursos:

    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_horas(horas)

    print(f"\nRecurso: {nombre}")
    print(f"Horas trabajadas: {horas}")
    print(f"Total semanal: {total} horas")
    print(f"Clasificación: {clasificacion}")

print("\nProceso finalizado correctamente.")