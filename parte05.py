import sympy as sp
import numpy as np


x = sp.symbols('x')
    f_sym = x**3 * sp.tan(x) / sp.log(x**2 + 1)
    df_sym = sp.diff(f_sym, x)
    df_exato = float(df_sym.subs(x, 1.0).evalf())
    
    f_num = sp.lambdify(x, f_sym, 'numpy')
    hs = [1e-2, 1e-4, 1e-6, 1e-8]
    
    print(f"  Valor exato f'(1.0) = {df_exato:.10f}\n")
    print(f"  {'h':<10} | {'Derivada Numérica':<18} | {'Erro Absoluto':<15}")
    print("  " + "-" * 47)
    for h in hs:
        df_num = (f_num(1.0 + h) - f_num(1.0 - h)) / (2 * h)
        erro = abs(df_exato - df_num)
        print(f"  {h:<10.0e} | {df_num:<18.10f} | {erro:<15.2e}")
    print("\n  [N4] Explicação: h grande demais gera erro de truncamento; h pequeno demais gera catástrofe de arredondamento[cite: 5, 6].")
