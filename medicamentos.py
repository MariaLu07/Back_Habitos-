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
