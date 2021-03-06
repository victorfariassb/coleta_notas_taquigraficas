# -*- coding: utf-8 -*-
"""contagem_palavras

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iqRKw_TQhXc6KWrfTULgqSfr6pbz5Zvn
"""
s =','.join([str(item) for item in fala])

for char in '-.,\n?![]<>':
    s = s.replace(char, ' ')
s = s.lower()
palavras = s.split()

counts = dict()

def word_count(dado):
    for word in dado:
      if len(word) > 2 and len(word) < 20 and '=' not in word:
        if word in counts: 
          counts[word] += 1
        else:
          counts[word] = 1
    return counts

print(word_count(palavras))


a_file = open("contagem.csv", "w")

writer = csv.writer(a_file)
for key, value in counts.items():
    writer.writerow([key, value])

a_file.close()
