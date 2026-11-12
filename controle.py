lancamentos = []

categorias_despesa = [
    "Comida", 
    "Mercado", 
    "Aluguel", 
    "Saúde", 
    "Água", 
    "internet", 
    "luz", 
    "Lazer", 
    "Outros"
]

categorias_receita = [
    "Salário", 
    "Investimentos", 
    "Outros"
]


def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))

            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            else:
                return valor

        except ValueError:
                print("Valor inválido. Digite um número válido.")


def escolher_categoria(categorias):
    print ("\nCategorias de despesa:")

    for indice, categoria in enumerate(categorias, start=1):
        print (f"{indice} - {categoria}")

    while True:
        try:
            opcao = int(input("Escolha uma categoria: "))

            if 1 <= opcao <= len(categorias):
                return categorias[opcao -1]
            else:
                print("Escolha uma opção válida.")

        except ValueError:
            print("Digite apenas o número da categoria.")


def adicionar_receita():
    descricao = input("Descrição da receita: ")
    valor = ler_valor("Valor da receita: ")
    categoria = escolher_categoria(categorias_receita)

    receita = {
        "tipo": "Receita",
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    }

    lancamentos.append(receita)
    print("\nReceita cadastrada com sucesso!\n")


def adicionar_despesa():
    descricao = input("Descrição da despesa: ")
    valor = ler_valor("Valor da despesa: ")
    categoria = escolher_categoria(categorias_despesa)

    despesa = {
        "tipo": "Despesa",
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
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
                f"{lancamento['categoria']} | "
                f"R$ {lancamento['valor']:.2f}"
            )

    print()


def gerar_relatorio():
    total_receitas = 0
    total_despesas = 0

    for lancamento in lancamentos:
        if lancamento["tipo"] == "Receita":
            total_receitas += lancamento["valor"]
        elif lancamento["tipo"] == "Despesa":
            total_despesas += lancamento["valor"]

    saldo = total_receitas - total_despesas

    print("\n--- RELATÓRIO FINANCEIRO ---")
    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}\n")


def menu():
    while True:
        print("=== CONTROLE FINANCEIRO ===")
        print("1 - Adicionar receita")
        print("2 - Adicionar despesa")
        print("3 - Listar lançamentos")
        print("4 - Gerar relatório financeiro")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_receita()
        elif opcao == "2":
            adicionar_despesa()
        elif opcao == "3":
            listar_lancamentos()
        elif opcao == "4": 
            gerar_relatorio()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")


menu()