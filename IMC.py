#Verificar o IMC (peso / altura)
PESO = int(input("Digite o peso:"))
ALTURA = float(input("Digite a altura:"))

#Cálculo do IMC
IMC = PESO / ALTURA ** 2

#Exibição dos resultados
if IMC < 18:
    print ("Seu peso está abaixo...")
elif IMC > 25:
    print ("Seu peso está acima...")
else:
    print ("O seu peso está ideal!")
    
