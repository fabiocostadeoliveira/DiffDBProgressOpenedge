def myfunc(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)

dict_vec = {'y': 0, 'z': 1, 'x': 1}

teste = {
    "valor1": "teste"
}

myfunc(*tuple_vec)
myfunc(*dict_vec)
print(teste['valor1'])