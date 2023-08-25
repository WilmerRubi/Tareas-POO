try:
    horas_trabajadas = float(input("Introduzca las Horas: "))
    tarifa_hora = float(input("Introduzca la Tarifa por hora: "))

    if horas_trabajadas > 40:
        horas_excedentes = horas_trabajadas - 40
        salario = (40 * tarifa_hora) + (horas_excedentes * 1.5 * tarifa_hora)
    else:
        salario = horas_trabajadas * tarifa_hora

    print("Salario:", salario)

except ValueError:
    print("Error, por favor introduzca un número")