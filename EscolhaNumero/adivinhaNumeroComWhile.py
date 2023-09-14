import random

print("Iniciando...")
print("************")
numero = random.randrange(1, 100, 1)

acertou = False
totalTentativas = 5
tentativa = 0

print("Estou pensando número de 1 a 100\n\n")
print('Você tem {} tentativas:', format(totalTentativas))

chute = int(input('Tente adivinhar o número em que estou pensando:\n'))

while (acertou == False and tentativa < totalTentativas):
    if(chute > numero):
        tentativa += 1
        print('Seu chute é maior que o número que estou pensando\nVocê ainda tem' , totalTentativas - tentativa , 'tentativas')
        chute = int(input('Tente novamente:'))
    if(chute < numero):
        tentativa += 1
        print('Seu chute é menor que o número que estou pensando\nVocê ainda tem' , totalTentativas - tentativa , 'tentativas')
        chute = int(input('Tente novamente:'))
    if(chute == numero):
        acertou = True
        print('Você acertou, o número que eu pensei é', numero)


if(acertou == False and tentativa >= totalTentativas):
    print('Você perdeu :(')
    print('O número que eu pensei foi:', numero)

print("*********")
print("GAME OVER")
print("*********")