def sumar_num(num1, num2):
    num1 + num2
    return num1 + num2


def restar_num(num1, num2):
    num1 - num2
    return num1 - num2


def multiplicar_num(num1, num2):
    num1 * num2
    return num1 * num2


def dividir_num(num1, num2):
    num1 / num2
    return num1 / num2


def calcular(num1, num2, operador):
    resultado = None
    messaggio = "Input non valido"
    if operador == "+":
        resultado = sumar_num(num1, num2)
        messaggio = f"El resultado de la suma es: {resultado:.2f}"
    elif operador == "-":
        resultado = restar_num(num1, num2)

    elif operador == "*":
        resultado = multiplicar_num(num1, num2)

    elif operador == "/":

        if num2 != 0:
            resultado = dividir_num(num1, num2)
        else:
            # throw error division by zero
            print("Error: división por cero.")
    else:
        # throw error operador non valido
        print("Operador no válido. Intente de nuevo.")
    return [resultado, messaggio]
