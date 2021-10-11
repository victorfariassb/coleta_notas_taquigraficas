# coleta_notas_taquigraficas
Script em Python para coletar notas taquigráficas da CPI da Covid-19, salvá-las em arquivo csv e fazer contagem das palavras. Feito para a disciplina de Pensamento Computacional, do Master em jornalismo de dados, automação e data storytelling do Insper.

## Autoria:
Victor Farias

## Apoio técnico:
Álvaro Justen e Bernardo Vianna

## Data:
Feito entre setembro e outubro de 2021

## Explicação:
O Senado Federal não traz em API as notas taquigráficas das sessões. Na realidade, para acessá-las, o usuário precisa entrar na comissão buscada, procurar a sessão de interesse e clicar nas notas taquigráficas, expostas em HTML. Não é possível baixar as informações em planilha editável. Essa forma de organização dificulta análises do que foi dito nas comissões. 

Por isso, decidi criar um programa (voltado especificamente para a CPI da Covid-19, mas que pode ser replicado em outras comissões da casa) para coletar todas as falas de todas as sessões disponíveis. As falas ficam salvas em um documento CSV. Cada linha traz o nome do autor e sua fala. Além disso, também fiz um contador de palavras, para ver quais termos foram mais mencionados.

## Programa consiste em quatro scrips:
1. **coleta_codigos.py** — Na API do Senado, coleta o código de cada sessão da comissão;
2. **coleta_sites_notas.py** —  Usa os códigos coletados para chegar aos sites onde estão as notas taquigráficos. O script coleta o link desses sites;
3. **coleta_limpeza_falas.py** — Usa os links coletados para coletar o nome do autor e a fala, além de fazer limpeza em formatações do HTML;
4. **contagem_palavras.py** — Faz nova limpeza nos dados e conta quantas vezes cada palavra aparece no texto. Também salva os dados em um arquivo CSV.

**notas_cpicovid.py** — Além dos quatro arquivos separados, também deixei um arquivo com todos os scripts juntos, de modo a simplificar o uso da ferramenta.
