"""
Recolectar datos del paciente: Nombre(str), edad(int), peso en Kg (float) y si tiene alergias (bool)
Calcular dosis base: La dosis es 0.5 mg por Kg de peso. Calcula la dosis total usando operaciones (float)
Ajustar por edad: Si el paciente es menor de 12 o mayor de 65, reduce la dosis 20% usa operadores booleanos
Verificar contraindicaciones: Si tiene alergias emite una advertencia, usa el valor booleano para control de flujo
Generar reporte: Muestra nombre, dosis calculada (Redondeada a 2 decimales), advertencias y recomendaciones de administracion
"""

nombrePaciente = str(input("Ingrese el nombre del paciente: "))    # Nombre del paciente
edadPaciente = int(input("Ingrese la edad del paciente: "))              # Edad del paciente 
peso = float(input("Ingrese el peso del paciente en kilogramos: "))            # Peso del paciente en kilogramos , almacenado en flotante
alergias = str(input("¿El paciente tiene alergias? (Si/No): "))

# ============================================
dosisBase = 0.5         # mg por kilo de peso
dosisPaciente = dosisBase * peso
alergiAlerta = "Tome precaucuciones, lea la informacion del medicamento."

# calculo contraindicaciones y ajuste por edad
if (edadPaciente <= 12 or edadPaciente >= 65):
    dosisPaciente = dosisPaciente * (.8)
if (alergias != "Si"):
    alergiAlerta = ""

# Medios visuales
bar = "=" * 50

print(bar)
print("Reporte de dosis medica para el paciente: ", nombrePaciente)
print("Dosis calculada (mg): ", round(dosisPaciente, 2))
print(alergiAlerta)
print(bar)