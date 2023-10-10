listanm = []
listaid = []
listarg = []

def cadastro():
    nome = input(f"\nQual o nome do {len(listanm) + 1}° cliente ? ")
    listanm.append(nome)
    idade = int(input(f"{nome}, qual sua idade ? "))
    listaid.append(idade)
    estado = str(input("De qual estado você é ? "))
    listarg.append(estado)

numero_de_clientes = int(input("\nQuantos clientes deseja cadastrar ? "))

for i in range(numero_de_clientes):
    cadastro()
    resposta = input("\nDeseja continuar?'s' para sim ou 'n' para não: ")
    if resposta.lower() == "n":
        break

print("\n")
print("\t== Cadastro Finalizado! ==")
print("=" * 40)
print("\nNome\t\tIdade\t\tRegião")

for i in range(len(listanm)):
    print(f"{listanm[i]}\t\t\t{listaid[i]}\t\t{listarg[i]}")
