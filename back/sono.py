registro_sono = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar sono")
    print("2. Meus registros de sono")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        data = input("Digite a data do consumo: ")
        hora_inicio = input("Digite a hora do consumo: ")
        hora_final = input("Digite a quantidade de água consumida (em ml): ")
        qualidade = input("Digite a quantidade de água consumida (em ml): ")
        hora_final = input("Digite a quantidade de água consumida (em ml): ")

        registro = {
            'data': data,
            'hora': hora,
            'quantidade': quantidade
        }

        registro_sono.append(registro)
        print("Consumo de água registrado com sucesso!")

    elif escolha == '2':
        if registro_sono:
            print("\nSeus registros de consumo de água:")
            for i, registro in enumerate(registro_sono, 1):
                print(f"\nRegistro {i}:")
                print(f" Data: {registro['data']}")
                print(f" Hora: {registro['hora']}")
                print(f" Quantidade: {registro['quantidade']}")
        else:
            print("\nVocê ainda não registrou nenhum consumo de água.")

    elif escolha == '3':
        print("\nSaindo do programa. Registro de consumo de água encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
