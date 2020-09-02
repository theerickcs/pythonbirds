class Pessoa:
    def __init__(self, *filhos, nome='Erick'):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    erick = Pessoa(nome='Erick')
    anelito = Pessoa(erick, nome='Anelito')
    for listagem in anelito.filhos:
        print(listagem.nome)