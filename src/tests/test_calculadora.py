def sumar_numero(num1,num2):
    return num1 + num2


while True:
    operador = input("Ingrese la operación (+, -, *, /) o 's' para salir: ")

    if operador == 's':
        break

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Entrada inválida. Intente de nuevo.")
        continue

    if operador == '+':
        resultado =  sumar_numero(num1,num2)
        print(f"El resultado de la suma es: {resultado:.2f}")
    elif operador == '-':
        resultado = 0 
        print(f"El resultado de la resta es: {resultado:.2f}")
    elif operador == '*':
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado:.2f}")
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado:.2f}")
        else:
            print("Error: división por cero.")
    else:
        print("Operador no válido. Intente de nuevo.")

print("Saliendo de la calculadora...")


