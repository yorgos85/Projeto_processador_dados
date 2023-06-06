from arquivo import carrega_arquivo,salvar_arquivo #IMPORTANDO AS FUNCOES
from processamento import localiza,filtrar,projetar #IMPORTANDO AS FUNCOES AS 2

alunos, cabecalho = carrega_arquivo('dados/alunos.csv', ',', [str,int,str,float,float,int,float,bool])
 
#linhas = localiza(alunos, 500)

alunos_pedro_ii = filtrar(alunos,'escola','Pedro II','==')
print(len(alunos_pedro_ii))

alunos_pedro_ii_monitoria = filtrar(alunos_pedro_ii,'monitoria',True,'==')
print(len(alunos_pedro_ii_monitoria))


salvar_arquivo('dados/alunos_filtrados.csv',',',alunos_pedro_ii_monitoria, cabecalho)












  



    
    
    
    
    


