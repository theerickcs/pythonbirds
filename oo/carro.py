class Motor():

    def acelerar(self, velocidade=1):
        self.velocidade =  velocidade + 1

    def frear(self, velocidade=-2):
        if(velocidade>= 2):
            self.velocidade = velocidade - 2
        elif(velocidade==1):
            self.velocidade = velocidade - 1
        elif(velocidade <= 0):
            print('Velocidade está zerada.')
        return self.velocidade

class Direcao():
    def girar(self, giro):
        self.giro = giro
        direcao = ['norte', 'leste', 'sul', 'oeste']
        if (giro < -3):
            return direcao[0]
        elif (giro > 3):
            return direcao[0]
        else:
            return direcao[0 + giro]


class Carro:
    def __init__(self):
        self.motor = Motor()
        self.direcao = Direcao()

if __name__=='__main__':
    #frear =  Motor()
    #print(frear.frear(1))
    direcao = Carro().direcao
    print(direcao.girar(3))

# A Direção terá a responsabilidade de controlar a direção. Ela oferece
# os seguintes atributos:
#
# Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
# Método girar_a_direita
# Método girar_a_esquerda
#
#        N
#     O     L
#        S
#
# Exemplo:
#     >>> # Testando motor
#     >>> motor = Motor()
#     >>> motor.velocidade
#     0
#     >>> motor.acelerar()
#     >>> motor.velocidade
#     1
#     >>> motor.acelerar()
#     >>> motor.velocidade
#     2
#     >>> motor.acelerar()
#     >>> motor.velocidade
#     3
#     >>> motor.frear()
#     >>> motor.velocidade
#     1
#     >>> motor.frear()
#     >>> motor.velocidade
#     0
#     >>> # Testando Direcao
#     >>> direcao = Direcao()
#     >>> direcao.valor
#     'Norte'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Leste'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Sul'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Oeste'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Norte'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Oeste'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Sul'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Leste'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Norte'
#     >>> carro = Carro(direcao, motor)
#     >>> carro.calcular_velocidade()
#     0
#     >>> carro.acelerar()
#     >>> carro.calcular_velocidade()
#     1
#     >>> carro.acelerar()
#     >>> carro.calcular_velocidade()
#     2
#     >>> carro.frear()
#     >>> carro.calcular_velocidade()
#     0
#     >>> carro.calcular_direcao()
#     'Norte'
#     >>> carro.girar_a_direita()
#     >>> carro.calcular_direcao()
#     'Leste'
#     >>> carro.girar_a_esquerda()
#     >>> carro.calcular_direcao()
#     'Norte'
#     >>> carro.girar_a_esquerda()
#     >>> carro.calcular_direcao()
#     'Oeste'
#
