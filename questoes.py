import numpy as np

# Q1 - Cilindro fechado: volume de 1000 cm³
def area_cilindro(r):
    if r <= 0:
        return np.nan #Representa um valor numérico 
    #indefinido ou inválido (Not a Number)
    return 2 * np.pi * r**2 + 2000 / r


# Q2 - Alcance do arremesso de peso
velocidade = 13.7
altura = 2.25
gravidade = 9.8


def alcance(alpha):
    seno = np.sin(alpha)
    raiz = np.sqrt(seno**2 + 2 * gravidade * altura / velocidade**2)
    return velocidade**2 * np.cos(alpha) / gravidade * (seno + raiz)


# Q3 - Menor comprimento da viga
def comprimento_viga(theta):
    if np.sin(theta) <= 0 or np.cos(theta) <= 0:
        return np.nan
    return 3 / np.sin(theta) + 9 / np.cos(theta)


# Q4 - Caixa aberta feita de uma folha 40 x 75 cm
def volume_caixa(lado):
    if lado <= 0 or lado >= 20:
        return np.nan
    return lado * (40 - 2 * lado) * (75 - 2 * lado)


# Q5 - Funcao dos extremos globais
def funcao_q5(x):
    u = x - 2

  #A função sign (de signal, sinal) devolve apenas -1, 0 ou 1 
  # para indicar se o número u é negativo, nulo ou positivo:
    if abs(u) > 1: 
        return np.sign(u) * np.sqrt(abs(u)) / (1 + 2 / u**4)**(1 / 8)

    return u / (u**4 + 2)**(1 / 8)


# Q6 - Copo de papel em forma de cone, volume 250 cm³
def area_copo(raio):
    if raio <= 0:
        return np.nan
    altura = 750 / (np.pi * raio**2)
    return np.pi * raio * np.sqrt(raio**2 + altura**2)


# Q7 - Cilindro inscrito em esfera de raio 14 cm
raio_esfera = 14


def volume_cilindro_inscrito(raio):
    if raio <= 0 or raio >= raio_esfera:
        return np.nan
    return 2 * np.pi * raio**2 * np.sqrt(raio_esfera**2 - raio**2)


# Q8 - Retangulo inscrito na elipse de semieixos 19 e 5
def area_retangulo(x):
    if x <= 0 or x >= 19:
        return np.nan
    return 20 * x * np.sqrt(1 - x**2 / 19**2)



