import csv

with open("tabela.csv", 'w', newline='') as arquivo:

    escrever = csv.writer(arquivo)

    escrever.writerow(["id", "nome", "salario"])
    escrever.writerow(["1", "fulano", "1000.00"])
    escrever.writerow(["2", "beltrano", "2000.00"])
    escrever.writerow(["3", "andre", "1500.00"])
    escrever.writerow(["4", "renato", "10.50"])

arquivo.close()

while True:
    print("Escolha uma opção:")
    print("1 - listar | 2 - incluir | 3 - excluir")

    opcao = int(input("Opção: "))

    if(opcao == 1):
        with open("tabela.csv") as arquivo:
            lista = csv.reader(arquivo)

            for linha in lista:
                print(linha)
            print("\n")


    if(opcao == 2):
        id = input("Id: ")
        nome = input("Nome: ")
        salario = input("Salário: ")

        with open("tabela.csv", 'a', newline='') as arquivo:
            incluir = csv.writer(arquivo)
            incluir.writerow([id, nome, salario])
            print("\n")
        arquivo.close()

    if(opcao == 3):
        with open("tabela.csv", 'w', newline='') as arquivo:
            escrever = csv.writer(arquivo)
            escrever.writerow(["id", "nome", "salario"])
        arquivo.close()

    

