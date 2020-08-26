class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    weber = Pessoa(nome='weber')
    luciano = Pessoa(weber, nome='luciano', idade=40)
    print(Pessoa.cumprimentar(weber))
    print(id(weber))
    print(weber.cumprimentar())
    print(weber.nome)
    print(luciano.nome)
    print(weber.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    weber.sobrenome= 'de paula'
    del luciano.filhos
    print(luciano.__dict__)
    print(weber.__dict__)
    Pessoa.olhos = 3
    print(luciano.olhos)
    print(weber.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(weber.olhos))
