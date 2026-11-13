import numpy as np


def derivada_primeira(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

#Aqui neste trecho é possível observar que temo a função, o x, e 
#altura que pode se realizar pos se passar desta circustancia 
# cai na tolerancia de é 1 ^ - 6


def derivada_segunda(f, x, h=1e-5):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)

def newton_raphson_otimizacao(f, x0, h=1e-5, tol=1e-6, max_iter=100):
    x = x0
    historico = [x]
    for i in range(max_iter):
        df  = derivada_primeira(f, x, h)
        d2f = derivada_segunda(f, x, h)
        if abs(d2f) < 1e-14:          # evita divisão por zero
            print("Segunda derivada nula — método falhou.")
            break
        x_novo = x - df / d2f
        historico.append(x_novo)
        if abs(derivada_primeira(f, x_novo, h)) < tol:
            x = x_novo
            break
        x = x_novo
#Aqui é onde é destacado a derivada depois disso u
# utilizamos para maximo e mínimo 

    d2f_final = derivada_segunda(f, x, h)
    if d2f_final > 0:
        tipo = "mínimo"
    elif d2f_final < 0:
        tipo = "máximo"
    else:
        tipo = "inconclusivo"
    return {
        "x": x,
        "f(x)": f(x),
        "f'(x)": derivada_primeira(f, x, h),
        "f''(x)": d2f_final,
        "iteracoes": i + 1,
        "classificacao": tipo,
        "historico": historico
    }

# def newton_raphson_otimizacao(f, x0, h=1e-5, tol=1e-6, max_iter=100):
#     x = x0
#     for i in range(max_iter):
#         df = derivada_primeira(f, x, h)
#         d2f = derivada_segunda(f, x, h)
# 
#         if abs(d2f) < 1e-14:  # Segurança contra divisão por zero
#             print("Segunda derivada nula — método falhou.")
#             break
# 
#         # Fórmula de atualização de Newton-Raphson
#         x_novo = x - df / d2f
# 
#         # Critério de parada: se a derivada for quase zero, achamos o ponto crítico
#         if abs(derivada_primeira(f, x_novo, h)) < tol:
#             x = x_novo
#             break
#         x = x_novo
# 
#     # Classificação final pelo teste da segunda derivada
#     d2f_final = derivada_segunda(f, x, h)
#     if d2f_final > 0:
#         tipo = "mínimo"
#     elif d2f_final < 0:
#         tipo = "máximo"
#     else:
#         tipo = "inconclusivo"
# 
#     return {"x": x, "f(x)": f(x), "classificacao": tipo}
