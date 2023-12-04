def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Erreur: Division par zéro"

def calculator():
    print("Sélectionnez un choix:")
    print("1. addition")
    print("2. soustraction")
    print("3. multiplication")
    print("4. division")

    selection = input("Entrez le numéro de l'opération souhaitée (1/2/3/4): ")

    if selection not in ('1', '2', '3', '4'):
        print("Erreur, veuillez entrer un choix valide")
    
        calculator()
        return

    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))

    if selection == '1':
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif selection == '2':
        print(f"{num1} - {num2} = {soustraction(num1, num2)}")
    elif selection == '3':
        print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    elif selection == '4':
        print(f"{num1} / {num2} = {division(num1, num2)}")

calculator()
