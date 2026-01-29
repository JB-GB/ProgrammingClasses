"""# Ejercicio: Calculadora de Dosis de medicamento
Crea un programa que calcule la dosis correcta de un medicamento basandose en el peso del paciente y muestre toda la informacion de forma clara usando print
Definir variables
Realizar calculo: Calcula la dosis total multiplicando el peso del paciente por la dosis por kilogramo
Mostrar Resultados Usa print() para mostrar un reporte claro con todos los datos y el resultado calculado
Validacion adicional

"""

nombrePaciente = "Fulanito de Tal"              # Nombre del paciente
pesoPacienteKG = 75                             # Masa del paciente
nombreMedicamento = "Similyptus"                # Nombre del medicamento a suministrar
dosisPorKG = 10                                 # mg por cada kilogramo
dosisPaciente = pesoPacienteKG * dosisPorKG

print("=" * 48)
print("Paciente:", nombrePaciente)
print("Peso (Kg):", pesoPacienteKG)
print("=" * 48)
print("Medicamento recetado:", nombreMedicamento, "(", dosisPorKG, "mg por Kg)")
print("Dosis para paciente:", dosisPaciente)
print("=" * 48)

if (dosisPaciente > 500):
    print("DOSIS RECETADA ES MAYOR A 500 mg!")
    
print("=" * 48)