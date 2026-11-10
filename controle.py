lancamentos = []


def adicionar_receita():
    descricao = input("Descrição da receita: ")
    valor = float(input("Valor da receita: "))

    receita = {
        "tipo": "Receita",
        "descricao": descricao,
        "valor": valor
    }

    lancamentos.append(receita)
    print("\nReceita cadastrada com sucesso!\n")


def adicionar_despesa():
    descricao = input("Descrição da despesa: ")
    valor = float(input("Valor da despesa: "))

    despesa = {
        "tipo": "Despesa",
        "descricao": descricao,
        "valor": valor
    }

    lancamentos.append(despesa)
    print("\nDespesa cadastrada com sucesso!\n")


def listar_lancamentos():
    print("\n--- LANÇAMENTOS ---")

    if not lancamentos:
        print("Nenhum lançamento cadastrado.")
    else:
        for lancamento in lancamentos:
            print(
                f"{lancamento['tipo']} | "
                f"{lancamento['descricao']} | "
                f"R$ {lancamento['valor']:.2f}"
            )

    print()


def menu():
    while True:
        print("=== CONTROLE FINANCEIRO ===")
        print("1 - Adicionar receita")
        print("2 - Adicionar despesa")
        print("3 - Listar lançamentos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_receita()
        elif opcao == "2":
            adicionar_despesa()
        elif opcao == "3":
            listar_lancamentos()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")


menu()