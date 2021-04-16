import csv

with open("tabela.csv", 'w', newline='') as arquivo:

    escrever = csv.writer(arquivo)

    escrever.writerow(["id", "nome", "salario"])
    escrever.writerow(["1", "fulano", "1000.00"])
    escrever.writerow(["2", "beltrano", "2000.00"])


arquivo.close()

