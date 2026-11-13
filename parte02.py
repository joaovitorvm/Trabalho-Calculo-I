from scipy.optimize import minimize_scalar

    # s1 = minimize_scalar(
    #         area_cilindro,
    #         method="golden",
    #         bracket=(1, 5, 10)
    #     )
    # 
    #     print("\n[S1 - Cilindro | Método Golden]")
    #     print(f"  Raio ótimo (x*)       = {s1.x:.8f} cm")
    #     print(f"  Área mínima           = {s1.fun:.8f} cm²")
    #     print(f"  Iterações             = {s1.nit}")
    #     print(f"  Nº de avaliações      = {s1.nfev}")
    #     print(f"  Convergiu             = {s1.success}")
    # 
    #     # Compara o resultado com o seu método de Newton-Raphson
    #     newton_q1 = newton_raphson_otimizacao(area_cilindro, 5.0)
    #     print(
    #         "  Diferença entre raios (Newton x Golden) = "
    #         f"{abs(newton_q1['x'] - s1.x):.3e}"
    #     )
    # 
    #     # -----------------------------------------------------------------
    #     # S2 - Arremesso de Peso (Busca de MÁXIMO invertendo o sinal)
    #     # -----------------------------------------------------------------
    #     s2 = minimize_scalar(
    #         alcance_negativo,
    #         method="brent",
    #         bracket=(0.1, 0.8, 1.4)
    #     )
    # 
    #     print("\n[S2 - Arremesso de Peso | Método Brent]")
    #     print(f"  Ângulo ótimo (rad)    = {s2.x:.8f} rad")
    #     print(f"  Ângulo ótimo (graus)  = {np.degrees(s2.x):.4f}°")
    #     print(f"  Alcance máximo        = {-s2.fun:.8f} m")  # Sinal invertido de volta!
    #     print(f"  Nº de avaliações      = {s2.nfev}")
    # 
    #     # Gráfico unindo a linha tracejada (vertical) e o ponto de máximo
    #     angulos = np.linspace(0.01, np.pi / 2 - 0.01, 500)
    #     alcances = alcance(angulos)
    # 
    #     plt.figure(figsize=(8, 4))
    #     plt.plot(angulos, alcances, label="Trajetória R(α)", color="blue")
    #     plt.axvline(s2.x, color="red", linestyle="--", label=f"α* ótimo = {s2.x:.4f} rad")
    #     plt.scatter(s2.x, -s2.fun, color="red", zorder=5, label=f"Máximo = {-s2.fun:.2f} m")
    #     plt.title("S2 - Otimização do Arremesso de Peso (SciPy)")
    #     plt.xlabel("Ângulo α (rad)")
    #     plt.ylabel("Alcance R(α) [m]")
    #     plt.legend()
    #     plt.grid(True)
    #     plt.show()
    # 
    #     # -----------------------------------------------------------------
    #     # S3 - Menor Comprimento da Viga (Método Bounded)
    #     # -----------------------------------------------------------------
    #     # 1. Teste com o intervalo amplo pedido no enunciado [0.1, 50]
    #     s3_amplo = minimize_scalar(
    #         comprimento_viga,
    #         method="bounded",
    #         bounds=(0.1, 50)
    #     )
    # 
    #     print("\n[S3 - Viga | Método Bounded - Intervalo Amplo (0.1, 50)]")
    #     print(f"  Theta encontrado      = {s3_amplo.x:.8f} rad")
    #     print(f"  Comprimento retornado = {s3_amplo.fun:.8f} m")
    #     print(f"  Iterações             = {s3_amplo.nit}")
    #     print(f"  Nº de avaliações      = {s3_amplo.nfev}")
    #     print("  ATENÇÃO: [0.1, 50] inclui vários períodos e singularidades.")
    #     print("  O método bounded pressupõe busca unimodal; este resultado não é físico.")
    # 
    #     # 2. Teste com o intervalo fisicamente válido (0 < theta < pi/2)
    #     s3_fisico = minimize_scalar(
    #         comprimento_viga,
    #         method="bounded",
    #         bounds=(0.1, np.pi / 2 - 0.1)
    #     )
    # 
    #     print("\n[S3 - Viga | Método Bounded - Intervalo Físico (0, pi/2)]")
    #     print(f"  Theta ótimo           = {s3_fisico.x:.8f} rad")
    #     print(f"  Comprimento mínimo    = {s3_fisico.fun:.8f} m")
    #     print(f"  Nº de avaliações      = {s3_fisico.nfev}")
    # 
    #     # -----------------------------------------------------------------
    #     # S4 - Q5: Extremos Globais (Análise de falha e intervalo limitado)
    #     # -----------------------------------------------------------------
    #     print("\n[S4 - Q5 | Discussão dos Métodos (Sem Extremo Global)]")
    # 
    #     for metodo in ["brent", "golden"]:
    #         try:
    #             res = minimize_scalar(funcao_q5, method=metodo)
    #             print(
    #                 f"  {metodo.capitalize()}: x = {res.x:.6f} | "
    #                 f"f(x) = {res.fun:.6f} | Avaliações = {res.nfev}"
    #             )
    #             print("    -> Atenção: este resultado não prova mínimo global.")
    #         except Exception as erro:
    #             print(f"  {metodo.capitalize()}: falhou ao localizar um mínimo.")
    #             print(f"    -> Motivo informado pelo SciPy: {erro}")
    # 
    #     limitado = minimize_scalar(
    #         funcao_q5,
    #         method="bounded",
    #         bounds=(-10, 10)
    #     )
    # 
    #     print("\n[S4 - Q5 | Método Bounded no intervalo [-10, 10]]")
    #     print(f"  x encontrado          = {limitado.x:.8f}")
    #     print(f"  f(x)                  = {limitado.fun:.8f}")
    #     print(f"  Nº de avaliações      = {limitado.nfev}")
    #     print("  -> Nota: Este é apenas um mínimo local dentro de [-10, 10],")
    #     print("     pois a função tende a -infinito e +infinito nos extremos.")
    # 
    # 
    # # Para rodar tudo:
