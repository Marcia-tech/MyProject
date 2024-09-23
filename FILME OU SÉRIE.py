#Registrar o conteúdo e a sua nota...
CONTEUDO = input("Qual o filme ou série preferido?")
AVALIACAO = int(input("Atribuir uma nota de 1 a 5:"))

#Realizar a avaliação
match AVALIACAO:
    case 1:
        print("Péssimo!")
        PORQUE = input("Descreva porque a avaliação foi baixa:")
    case 2:
        print("Ruim!")
        PORQUE = input("Descreva porque a avaliaçãofoi baixa:")
    case 3:
        print("Razoável.")
    case 4:
        print("Bom!")
    case 5:
        print("Ótimo!")
    case _:
        print("opção não reconhecida...")
              


