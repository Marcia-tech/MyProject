#alunos aprovados ou reprovados?
N1 = float(input("1a. nota:"))
N2 = float(input("2a. nota:"))
N3 = float(input("3a. nota:"))
N4 = float(input("4a. nota:"))

#cálculo de média final
MEDIA = (N1 + N2 + N3 + N4) / 4

#verificação se aprovado ou não
if MEDIA >=6:
    print ("Estudante aprovado!")
else:
    print ("Estudante reprovado!")

    print ("A média dele é:", MEDIA)
