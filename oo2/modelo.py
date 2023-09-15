class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self ._nome
    
    @property
    def likes(self):
        return self ._likes
    
    @nome.setter
    def nome(self, novo_nome):
        self ._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # Utiliza o construtor da classe mãe para criar um objeto novo
        self.duracao = duracao
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) # Utiliza o construtor da classe mãe para criar um objeto novo
        self.temporadas = temporadas
    

totoro = Filme('meu vizinho totoro', 1995, 75)
totoro.dar_like()
totoro.dar_like()
totoro.dar_like()
totoro.dar_like()
print(f'Nome: {totoro.nome}\nAno: {totoro.ano}\nduracao: {totoro.duracao}\nLikes: {totoro.likes}')

bones = Serie('bones', 2006, 14)
bones.dar_like()
print(f'Nome: {bones.nome}\nAno: {bones.ano}\ntemporadas: {bones.temporadas}\nLikes: {bones.likes}')