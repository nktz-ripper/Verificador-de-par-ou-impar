print("Verifique se um número é par ou ímpar.")

while True:
    numero = input("Digite um número: ")
    inputcorreto = numero.isnumeric()
    if inputcorreto == True:
        if int(numero)%2==0:
            print(numero, "é par.")
        else:
            print(numero, "é ímpar.")
    else:
        print("O valor digitado não é número. Utilize somente números.")
    if input("Deseja repetir? (y/n) ") == "n":
        break