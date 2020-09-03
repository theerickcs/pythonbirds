class Pessoa:
    coracao = 1

    def __init__(self, *filhos, nome='Erick'):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 'retornando método estático Decorator'

    @classmethod
    def metodo_classe(cls):
        return f'Nome da classe: {cls} e atributo olhos: {cls.coracao}'


if __name__ == '__main__':
    erick = Pessoa(nome='Erick')
    anelito = Pessoa(erick, nome='Anelito')
    for listagem in anelito.filhos:
        print(listagem.nome)

    print(Pessoa.metodo_estatico() + " ou " + erick.metodo_estatico())
    print(f'{Pessoa.metodo_classe()} ou {erick.metodo_classe()}')