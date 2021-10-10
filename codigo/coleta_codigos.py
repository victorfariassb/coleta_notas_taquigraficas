# -*- coding: utf-8 -*-
"""coleta_codigos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1acYm_3YQsJ4wkjHDw-_ZhNZuBRo_BE_R
"""

import requests

url = "https://legis.senado.leg.br/comissoes/comissao?codcol=2441&data1=2021-01-01&data2=2021-10-21"  # A data precisa ser atualizada, à medida que a CPI avança
resposta = requests.get(url)
html = resposta.text
print(html)

lista = []
partes = html.split('<a href="./reuniao?reuniao=')

def coleta_dados():
  for parte in partes:
    subpartes = parte.split('&amp;codcol=2441">')
    conteudo = subpartes[0]
    if len(conteudo) > 10:
      continue 
    if conteudo not in lista:
      lista.append(conteudo)
  print(lista)

coleta_dados()
