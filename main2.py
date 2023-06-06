from arquivo import carrega_arquivo,salvar_arquivo #IMPORTANDO AS FUNCOES
from processamento import localiza,filtrar,projetar,agrupar #IMPORTANDO AS FUNCOES AS 2

alunos, cabecalho = carrega_arquivo('dados/alunos.csv', ',', [str,int,str,float,float,int,float,bool])

agrupamento = agrupar(alunos,'escola', 'faltas')

print(agrupamento)