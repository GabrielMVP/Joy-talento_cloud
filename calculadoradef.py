def calculadora():
    while True:
        print("Operações:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        escolha = input("Digite o número para a operação correspondente: ")
        
        if escolha == "0":
            print("Saindo da calculadora.")
            break
        elif escolha in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            
            if escolha == "1":
                resultado = num1 + num2
            elif escolha == "2":
                resultado = num1 - num2
            elif escolha == "3":
                resultado = num1 * num2
            elif escolha == "4":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Divisão por zero não é permitida."
            
            print("Resultado:", resultado)
        else:
            print("Essa opção não existe.")

calculadora()
