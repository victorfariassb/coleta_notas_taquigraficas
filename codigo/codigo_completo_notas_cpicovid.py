# -*- coding: utf-8 -*-
"""notas_cpicovid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q3dKQh7cRuew3stgeQ68YtRU6nWjhKIm
"""

import requests

"""# Coleta do código das sessões da CPI"""

url = "https://legis.senado.leg.br/comissoes/comissao?codcol=2441&data1=2021-01-01&data2=2021-10-21"
resposta = requests.get(url)
html = resposta.text
print(html)

lista = []
partes = html.split('<a href="./reuniao?reuniao=')

def coleta_dados(codcol):
  for parte in partes:
    subpartes = parte.split('&amp;codcol=' + str(codcol) + '">')
    conteudo = subpartes[0]
    if len(conteudo) > 10:
      continue 
    if conteudo not in lista:
      lista.append(conteudo)
  print(lista)

coleta_dados(2441) 

"""# Coleta site onde estão as notas taquigráficas"""

lista2 = []

def coleta_notas(dados):
  for codigo in dados:
    url2 = "https://legis.senado.leg.br/dadosabertos/reuniaocomissao/notas/" + str(codigo)
    resposta2 = requests.get(url2)
    html2 = resposta2.text
    parte = []
    partes2 = html2.split('<UrlNotasTaquigraficas>')
    if len(partes2) > 1:
      partes2 = partes2[1]
      subpartes2 = partes2.split('</UrlNotasTaquigraficas>')
      lista2.append(subpartes2[0])
    else:
      continue

coleta_notas(lista)

print(lista2)

"""# Coleta notas taquigráficas"""

fala = []

def coleta_notas(dado2):
  for link in dado2:
    url3 = link
    resposta3 = requests.get(url3)
    html3 = resposta3.text
    texto3 = html3.replace('</span></div></div><div><div class="principalStyle">', '')
    texto3 = texto3.replace('</span></div><div class="principalStyle"><span>', '')
    texto3 = texto3.replace('</span><span class="intercorrenciaMesmoSegmentoStyle">', '')
    texto3 = texto3.replace('</span></div></div><div><div class="intercorrenciaCentralizadoStyle">', '')
    texto3 = texto3.replace('</span></div></div><div><div class="anotacaoOcorrenciaStyle"><span>(<i>Procede-se à exibição de vídeo.</i>)', '')
    texto3 = texto3.replace('title="Áudio"><img src="https://www.senado.leg.br/atividade/img/sound.png" /></a> </div> </td> <td class="justificado">title="Áudio"><img src="https://www.senado.leg.br/atividade/img/sound.png" /></a> </div> </td> <td class="justificado">','')
    texto3 = texto3.replace('</span><span class="principalStyle">', '')
    texto3 = texto3.replace('</span></div></div><div><div class="anotacaoAberturaStyle"><span>(<i>S', '')
    texto3 = texto3.replace('</span></div></div><div><div class="intercorrenciaCentralizadoStyle"><span>', '') 
    texto3 = texto3.replace('</span></div></div> </td> </tr> <tr id="quarto91"> <td class="hora">','')
    texto3 = texto3.replace('(<i>Pausa.</i>) <span', '')
    texto3 = texto3.replace('</span></div></div><div><div class="intercorrenciaCentralizadoStyle"><span>(<i>Interrupção do som.</i>) (<i>Pausa.</i>)','')
    texto3 = texto3.replace('O SR.','')
    texto3 = texto3.replace('A SRA.','')
    texto3 = texto3.replace('(<i>Risos.</i>)','')
    texto3 = texto3.replace('</span></div></div> </td> </tr> <tr><td colspan="2"> <div class="hidden-print text-right naoImprimir"> <p><a name="fim" href="#topo" title="Ir para o início das Notas"><i class="icon-chevron-up"></i></a></p> </div> </td></tr> </tbody> </table> </div> </div> </div> </div> </div> </div> </div> </div> <form action="#" id="hrefFm" method="post" name="hrefFm">', '')
    texto3 = texto3.replace('</span></div></div><div><div class="anotacaoAberturaStyle">','')
    texto3 = texto3.replace('title="Áudio"><img src="https://www.senado.leg.br/atividade/img/sound.png" /></a> </div> </td> <td class="justificado"> <div><div class="principalStyle">', '')
    texto3 = texto3.replace('</span> </form> </div> <div class="sf-wrapper"> <footer class="Footer"> <div class="container"> <div class="Triad Triad--stackable"> <div class="Rail gamma my-2"> <a class="link link-deep--facebook" href="https://www.facebook.com/SenadoFederal" title="Facebook" target="_blank"><i class="fab fa-facebook"></i></a><a class="link link-deep--twitter" href="https://twitter.com/senadofederal" title="Twitter" target="_blank"><i class="fab fa-twitter"></i></a><a class="link link-deep--instagram" href="https://www.instagram.com/senadofederal" title="Instagram" target="_blank"><i class="fab fa-instagram"></i></a><a class="link link-deep--youtube" href="https://www.youtube.com/user/TVSenadoOficial" title="Youtube" target="_blank"><i class="fab fa-youtube"></i></a> </div> <div class="Rail my-2">', '')
    texto3 = texto3.replace('</span></div></div> </td> </tr> <tr id="quarto104"> <td class="hora">', '')
    texto3 = texto3.replace('<div> <span title="Texto revisado" style="border-radius: 9px; padding-left: 9px; padding-right: 9px; background-color: #999999; color: #FFFFFF; display: inline-block; font-size: 11.844px; font-weight: bold; line-height: 14px; text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25); vertical-align: baseline; white-space: nowrap;">R</span>', '')
    texto3 = texto3.replace('<a href="https://www.camara.leg.br" title="Câmara dos Deputados" target="_blank"><img src="https://www.senado.leg.br/noticias/essencial/images/icon-camara.svg" alt="Câmara dos Deputados"></a><a href="https://www.congressonacional.leg.br" title="Congresso Nacional" target="_blank"><img src="https://www.senado.leg.br/noticias/essencial/images/icon-congresso.svg" alt="Congresso Nacional"></a><a href="https://www.tcu.gov.br" title="Tribunal de Contas da União" target="_blank"><img src="https://www.senado.leg.br/noticias/essencial/images/icon-tcu.svg" alt="Tribunal de Contas da União"></a> </div> <div class="Rail Rail--fenced my-2"> <a class="link link-deep" href="https://www12.senado.leg.br/institucional/carta-de-servicos/en/carta-de-servicos">ENGLISH</a><a class="link link-deep" href="https://www12.senado.leg.br/institucional/carta-de-servicos/es/carta-de-servicos">ESPAÑOL</a><a class="link link-deep" href="https://www12.senado.leg.br/institucional/carta-de-servicos/fr/carta-de-servicos">FRANÇAIS</a> </div> </div> <div class="divider my-2"></div> <div class="Triad Triad--stackable"> <div class="my-2"> <a class="link link-deep" href="https://intranet.senado.leg.br" title="Intranet"><i class="fas fa-lock mr-1"></i> Intranet</a> </div> <div class="Rail Rail--fenced Rail--stackable my-2"> <a class="link link-deep" href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Servidor efetivo</a><a class="link link-deep" href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Servidor comissionado</a><a class="link link-deep" href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Servidor aposentado</a><a class="link link-deep" href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Pensionista</a>', '')
    texto3 = texto3.replace('</div> <div class="my-2"> <a class="link link-deep" href="https://www12.senado.leg.br/institucional/falecomosenado" title="fale com o Senado"><i class="fas fa-phone u-flip-x mr-1"></i> Fale com o Senado</a> </div> </div> <div class="divider my-2"></div> <div class="d-flex justify-content-xl-center"> <span class="my-2">Senado Federal - Praça dos Três Poderes - Brasília DF - CEP 70165-900 | <span class="text-nowrap">Telefone: 0800 0 61 2211</span> </span> </div> </div> </footer> </div> </div> <script src="https://www25.senado.leg.br/senado-theme/js/jquery-1.11.1.js" type="text/javascript"></script> <script src="https://www25.senado.leg.br/senado-theme/js/bootstrap.js" type="text/javascript"></script> <script src="https://www25.senado.leg.br/senado-theme/js/bootstrap-hover-dropdown.js" type="text/javascript"></script> <script src="https://www25.senado.leg.br/senado-theme/js/bootstrap-datepicker.js" type="text/javascript"></script> <script src="https://www25.senado.leg.br/senado-theme/js/locales/bootstrap-datepicker.pt-BR.min.js" type="text/javascript"></script> <script type="text/javascript"\n\t\tsrc="https://www.senado.leg.br/inc/essencial-2020/js/essencial.js"></script> <script src="https://www25.senado.leg.br/atividade-portlet/js/escriba.js?browserId=other&amp;minifierType=js&amp;languageId=pt_BR&amp;b=6205&amp;t=1633127543000" type="text/javascript"></script> <script src="https://www25.senado.leg.br/notifications-portlet/notifications/js/main.js?browserId=other&amp;minifierType=js&amp;languageId=pt_BR&amp;b=6205&amp;t=1633127519000" type="text/javascript"></script> <script type="text/javascript">Liferay.Util.addInputFocus();</script> <script type="text/javascript">Liferay.Portlet.onLoad({canEditTitle:false,columnPos:0,isStatic:"end",namespacedId:"p_p_id_escriba_WAR_atividadeportlet_",portletId:"escriba_WAR_atividadeportlet",refreshURL:"\\x2fc\\x2fportal\\x2frender_portlet\\x3fp_l_id\\x3d43404\\x26p_p_id\\x3describa_WAR_atividadeportlet\\x26p_p_lifecycle\\x3d0\\x26p_t_lifecycle\\x3d0\\x26p_p_state\\x3dnormal\\x26p_p_mode\\x3dview\\x26p_p_col_id\\x3dcolumn-1\\x26p_p_col_pos\\x3d0\\x26p_p_col_count\\x3d1\\x26p_p_isolated\\x3d1\\x26currentURL\\x3d\\x252Fweb\\x252Fatividade\\x252Fnotas-taquigraficas\\x252F-\\x252Fnotas\\x252Fr\\x252F10292\\x26_escriba_WAR_atividadeportlet_cr\\x3d10292"});AUI().use("aui-base","liferay-menu","liferay-notice","liferay-poller","liferay-session",function(a){(function(){Liferay.Util.addInputType();Liferay.Portlet.ready(function(b,c){Liferay.Util.addInputType(c)});if(a.UA.mobile){Liferay.Util.addInputCancel()}})();(function(){new Liferay.Menu();var b=Liferay.Data.notices;for(var c=1;c<b.length;c++){new Liferay.Notice(b[c])}})();(function(){Liferay.Session=new Liferay.SessionBase({autoExtend:true,sessionLength:30,redirectOnExpire:false,redirectUrl:"https\\x3a\\x2f\\x2fwww25\\x2esenado\\x2eleg\\x2ebr\\x2fweb\\x2fguest",warningLength:1})})()});</script> <script src="https://www25.senado.leg.br/senado-theme/js/main.js?browserId=other&amp;minifierType=js&amp;languageId=pt_BR&amp;b=6205&amp;t=1633127526000" type="text/javascript"></script> <script type="text/javascript"></script> </body> </html> ', '')
    texto3 = texto3.replace('</b>','')
    texto3 = texto3.replace('<span>', '')
    partes3 = texto3.split('<b>')
    for item in partes3[1:]:
      partes4 = item.split('</b>')
      fala.append(partes4)

coleta_notas(lista2)

import pandas as pd

df = pd.DataFrame(fala, columns=['fala'])
dados = df.to_csv('cpi.csv', index=False)

s =','.join([str(item) for item in fala])

for char in """-.,\n?![]<>:;"'""":
    s = s.replace(char, ' ')
s = s.lower()ower()
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

word_count(palavras)

a_file = open("contagem.csv", "w")

writer = csv.writer(a_file)
for key, value in counts.items():
    writer.writerow([key, value])

a_file.close()
