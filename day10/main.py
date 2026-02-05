import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("Was ist die erste Zahl?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Wähle eine Rechenoperation: ")
        num2 = float(input("Was ist die nächste Zahl?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Gib 'j' ein, um mit {answer} weiterzurechnen, oder 'n', um eine neue Rechnung zu starten: "
        )

        if choice == "j":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
