import adivinhaNumeroComFor
import forca

print('***********************************')
print('************ Joguinhos ************')
print('***********************************')

print ("(1) Forca (2) Adivinhação")
jogoEscolhido = int(input('Qual você deseja jogar? :'))

if(jogoEscolhido == 1):
    print('Você escolheu Forca')
    forca.jogar()
if(jogoEscolhido == 2):
    print("Você escolheu Adivinhação")
    adivinhaNumeroComFor.jogar()