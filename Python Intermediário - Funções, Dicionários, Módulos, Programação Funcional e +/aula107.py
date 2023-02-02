"""
    Valores padrão para parâmetros
    ao definir uma função, os parâmetros podem
    ter valores padrão. Caso o valor não seja
    enviado para o parâmetro, o valor padrão será usado.
"""

def multiplicar(a, b, c = None):
    if c is not None:
        print((a*b) + c)
    else:
        print(a*b)
    
multiplicar(4,2,1)
multiplicar(5,2) 

    
    
    