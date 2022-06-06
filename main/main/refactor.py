import pandas as pd

df = pd.read_json (r'C:\Users\vinicius.reisch\PycharmProjects\pythonProject\main\main\dados.json')

lista1 = [df]
# lista1.replace(lista1[0]['Preco'], "R$")
print(lista1[0]['Preco'])