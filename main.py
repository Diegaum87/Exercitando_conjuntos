conjunto_1 = {1, 1, 'Kenzie', 'Academy', 'Kenzie', 10}
print(conjunto_1)

tamanho_conjunto_1 = len(conjunto_1)
print("Tamanho do conjunto_1:", tamanho_conjunto_1)

conjunto_1.add('Novo Elemento')
print(conjunto_1)

conjunto_1.discard('Novo Elemento')
print(conjunto_1)

conjunto_1.clear()
print(conjunto_1)