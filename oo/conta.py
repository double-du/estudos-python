class Conta:
    # Construtor
    def __init__(self, numero, titular, saldo, limite):
        # Self descreve o Objeto em sí
        # O '__' diz que o atributo é privado, entretanto o encapsulamento do Python é fraco
        # # Parecido com o que acontece com o Javascript (Não TypeScript)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Métodos:
    def ver_extrato(self):
        print("Titular: {}\nSaldo: {}".format(self.__titular, self.__saldo))
    
    def depositar(self, valor):
        print('\nDepositando {}...'.format(valor))
        self.__saldo += valor
        print("Novo saldo de {}\nValor: {}".format(self.__titular, self.__saldo))
    
    def sacar(self, valor):
        print('\nSacando {}...'.format(valor))
        if(self.__saldo >= valor):
            self.__saldo -= valor
            print("Novo saldo de {}\nValor: {}".format(self.__titular, self.__saldo))
            return
        else:
            print("{}, você não possui saldo suficiente para este saque".format(self.__titular))
    
    def mostrar_dados_conta(self):
        print('Numero: ', self.__numero)
        print('Titular: ', self.__titular)
        print('Saldo: ', self.__saldo)
        print('Limite: ', self.__limite)

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Metodos de Acesso
    @property #trata getter como atributo
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
   
    @limite.setter    #trata setter como atributo
    def limite(self, valor):
        self.__limite = valor
        print("Novo limite de: {}\nValor:{}".format(self.titular, self.limite))

    @staticmethod
    def codigo_banco():
        print('3009')