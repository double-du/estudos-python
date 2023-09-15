from conta import Conta
from cliente import Cliente

conta = Conta(123, 'Eduardo', 1000.0, 8000.0)

conta.ver_extrato()

conta.depositar(1000.0)

conta.sacar(1000.0)
conta.sacar(2000.0)

conta2 = Conta(123, 'Natalia', 1000.0, 8000.0)

conta2.transferir(100, conta)

conta2.limite = 9000

cliente = Cliente("weber")
print(cliente.nome)

cliente.nome = 'eber' # Criando um acesso direto, pode-se setar o valor como se tivesse acesso direto à variavel
print(cliente.nome)

conta.codigo_banco()