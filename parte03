import sympy as sp

x = sp.symbols('x')
    
limites = [
        ("L1", sp.limit(1/x**2 - sp.cot(x)**2, x, 0)),
        ("L2", sp.limit(((1 + x)**(1/x) - sp.E) / x, x, 0)),
        ("L3", sp.limit(x - x**2 * sp.log(1 + 1/x), x, sp.oo)),
        ("L4", sp.limit((sp.asin(x)/x)**(1/x**2), x, 0)),
        ("L5", sp.limit(1/sp.log(x) - 1/(x - 1), x, 1)),
        ("L6", sp.limit((sp.tan(sp.tan(x)) - sp.sin(sp.sin(x))) / x**3, x, 0)),
        ("L7", sp.limit(x**sp.sin(x), x, 0, '+')),
        ("L8", sp.limit(x**2 / ((1 + 5*x)**(1/5) - (1 + x)), x, 0))
    ]
    
for nome, l in limites:
        print(f"  {nome} = {l}")

