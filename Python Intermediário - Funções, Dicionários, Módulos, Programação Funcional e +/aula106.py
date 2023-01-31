"""
Argumentos nomeados e não nomeados em funções Python
Arugmento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)


"""

#Não nomeado
def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

soma(1,2)



#Nomeado - Se você nomear um parametro todos depois dele tbm terão que ser nomeados
#           (1,5,6,y=7,a=9 ...)
def diminuir(y, x):
    print(f'{x=} y={y}', '|', 'x - y = ', x - y)

diminuir(x=10, y=5)