class Funcionario():
    def __init__(self, nome = '', setor = '', cargo = ''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/blue], sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo"


from rich import print

c1 = Funcionario('Renato', 'homofobia', 'Gerente Homofóbico')
print(c1.apresentacao())