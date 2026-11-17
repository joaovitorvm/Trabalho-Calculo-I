    import sympy as sp

    x = sp.symbols("x", positive=True)

    funcoes = [
        ("D1",sp.sqrt(sp.sin(sp.sqrt(x))) * sp.exp(sp.cos(x)**2)),
        ("D2",x**3 * sp.tan(x) / sp.log(x**2 + 1)),
        ("D3",sp.acos((x**2 - 1) / (x**2 + 1))),
        ("D4",(x / (x + 1))**(x**2)),
        ("D5",sp.log(sp.sec(x) + sp.tan(x)) * sp.atan(sp.sinh(x))),
        ("D6",x**sp.exp(x) + sp.exp(x**x)),
        ("D7",sp.log(sp.cos(x)) / sp.log(sp.sin(x))),
        ("D8",(x * sp.sqrt(x**sp.sqrt(x)))**(1/x))
        ]

    for nome, funcao in funcoes:
        derivada = sp.diff(funcao, x)
        derivada_simplificada = sp.simplify(derivada)

        print(f"\n{nome}")
        print(f"Funcao original: {funcao}")
        print(f"Derivada: {derivada_simplificada}")

