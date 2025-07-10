print("Escolha uma das opções abaixo:")
print(f"1. Registrar medicamento")
print(f"2. Meus medicamentos")
print(f"3. Sair")

while True:
    escolha = input(f"\nDigite 1, 2 ou 3:")

    if escolha == '1':
        medicamento = input("Digite o nome de seu novo medicamento: ")
        dosagem = input("Digite a dosagem (em ml): ")
        orientacoes = input("Quais as orientações desse remédio? ")
        print(f"\nMedicamento registrado com sucesso!")
        break

    elif escolha == '2':
        print(f"\nSeus medicamentos são {medicamentos}")
        print(f"Suas dosagens são {nascimento}")
        print(f"Suas orientações são {genero}")
        break

    elif escolha == '3':
        print(f"\nRegistro de medicamento completo!")









print("Escolha uma das opções abaixo:")
print(f"1. Registrar medicamento")
print(f"2. Meus medicamentos")
print(f"3. Sair")

while True:
    escolha = input(f"\nDigite 1, 2 ou 3:")

    if escolha == '1':
        medicamento = input("Digite o nome de seu novo medicamento: ")
        dosagem = input("Digite a dosagem (em ml): ")
        orientacoes = input("Quais as orientações desse remédio? ")
        print(f"\nMedicamento registrado com sucesso!")
        break

    elif escolha == '2':
        print(f"\nSeus medicamentos são {medicamentos}")
        print(f"Suas dosagens são {nascimento}")
        print(f"Suas orientações são {genero}")
        break

    elif escolha == '3':
        print(f"\nRegistro de medicamento completo!")











meus_medicamentos = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar medicamento")
    print("2. Meus medicamentos")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        medicamento = input("Digite o nome de seu novo medicamento: ")
        
        while True:
            dosagem_input = input("Digite a dosagem (em ml): ")
            try:
                dosagem = float(dosagem_input)
                break
            except ValueError:
                print("Por favor, digite um número válido para a dosagem.")

        orientacoes = input("Quais as orientações desse remédio? ")

        registro = {
            "medicamento": medicamento,
            "dosagem": dosagem,
            "orientacoes": orientacoes
        }

        meus_medicamentos.append(registro)
        print("\nMedicamento registrado com sucesso!")

    elif escolha == '2':
        if meus_medicamentos:
            print("\nSeus medicamentos registrados:")
            for i, med in enumerate(meus_medicamentos, 1):
                print(f"\nMedicamento {i}:")
                print(f" Nome: {med['medicamento']}")
                print(f" Dosagem: {med['dosagem']} ml")
                print(f" Orientações: {med['orientacoes']}")
        else:
            print("\nVocê ainda não registrou nenhum medicamento.")
            
    elif escolha == '3':
        print("\nSaindo do programa. Registro de medicamentos encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")













meus_medicamentos = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar medicamento")
    print("2. Meus medicamentos")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        medicamento = input("Digite o nome de seu novo medicamento: ")
        dosagem_input = input("Digite a dosagem (em ml): ")

        try:
            dosagem = float(dosagem_input)
            orientacoes = input("Quais as orientações desse remédio? ")

            registro = {
                "medicamento": medicamento,
                "dosagem": dosagem,
                "orientacoes": orientacoes
            }

            meus_medicamentos.append(registro)
            print("\nMedicamento registrado com sucesso!")

        except ValueError:
            print("Valor inválido para dosagem! Digite um número (ex: 5 ou 7.5).")

    elif escolha == '2':
        if meus_medicamentos:
            print("\nSeus medicamentos registrados:")
            for i, med in enumerate(meus_medicamentos, 1):
                print(f"\nMedicamento {i}:")
                print(f" Nome: {med['medicamento']}")
                print(f" Dosagem: {med['dosagem']}")
                print(f" Orientações: {med['orientacoes']}")
        else:
            print("\nVocê ainda não registrou nenhum medicamento.")

    elif escolha == '3':
        print("\nSaindo do programa. Registro de medicamentos encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
