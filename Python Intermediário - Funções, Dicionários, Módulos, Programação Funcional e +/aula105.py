"""
    Introdução ás funções (def) em python 
    funções são trechos de código usado para
    replicar determinada ação ao longo so seu código
    elas podem receber valores para parêmetros (argumentos)
    e retornar um valor específico
    por padrão, funções Python retornam none (nada)
"""

def saudacao(nome = 'Sem nome'):
    print(f"Olá {nome}!")
    

saudacao("Rhuan")
saudacao("Lucas")
saudacao("Paulinho")
saudacao()
