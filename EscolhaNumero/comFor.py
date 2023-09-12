import random

print("************************************************")
print("****************[ Iniciando...  ]***************")
print("************************************************")
numero = random.randrange(1, 100, 1)

acertou = False
totalDeTentativas = 5
tentativa = 0

print("Estou pensando número de 1 a 100\n\n")
print("Você tem {} tentativas:".format(totalDeTentativas))
print('---> estou pensando em: {} <---'.format(numero))

chute = int(input('Tente adivinhar o número em que estou pensando:\n'))

for rodada in range(1, totalDeTentativas,1):
    if(chute < 1 or chute > 100):
        rodada-=1
        chute = int(input('Você deve digitar um número entre 1 e 100: '))
        continue
    if(chute > numero):
        tentativa += 1
        print("{} é MAIOR que o número que estou pensando\nVocê ainda tem {} tentativas".format(chute, totalDeTentativas-tentativa))
        chute = int(input('Tente novamente:'))
    if(chute < numero):
        tentativa += 1
        print("{} é MENOR que o número que estou pensando\nVocê ainda tem {} tentativas".format(chute, totalDeTentativas-tentativa))
        chute = int(input('Tente novamente:'))
    if(chute == numero):
        acertou = True
        print('Você acertou, o número que eu pensei é', numero)
        break

if(acertou == False):
    print('Você perdeu :(')
    print('O número que eu pensei foi:', numero)

print("*************************************************")
print("******************[ GAME OVER ]******************")
print("*************************************************")