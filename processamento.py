from funcoes import media,somatorio # Importando as funcoes

#funcao para localizar os dados.

def localiza(dados,linha):
    quantidade_registro = len(dados)
    if linha < quantidade_registro:
        return dados[linha]
    else:
        print('Indice superior a quantidade registro')
        return {} #retorna dicionario vazio




#funcao para filtrar os dados.

def filtrar(dados,campo, valor, operacao):
    dados_filtrados = []
    for linha in dados:
        if operacao == '==':
            if linha[campo] == valor: 
              dados_filtrados.append(linha)
            elif operacao == '>':
              if linha[campo] > valor: 
                dados_filtrados.append(linha)
            elif operacao == '<':
              if linha[campo] < valor: 
                dados_filtrados.append(linha)
            elif operacao == '>=':
              if linha[campo] >= valor: 
                dados_filtrados.append(linha)
            elif operacao == '<=':
              if linha[campo] <= valor: 
                dados_filtrados.append(linha)
            elif operacao == '!=':
              if linha[campo] != valor: 
                dados_filtrados.append(linha)                
            
        
        
    return dados_filtrados         
    
    
#funcao para projetar os dados.    
    
def projetar(dados,colunas):  
   dados_projetados = []
   for linha in dados:
     linha_projetada = {}
     for campo,valor in linha.items():
       if campo in colunas:
         linha_projetada[campo] = valor 
     dados_projetados.append(linha_projetada)  
   return dados_projetados  
 
 
#funcao para agrupar os dados.

def agrupar(dados, coluna, coluna2):
   dados_agrupados = {}
   for linha in dados:
     valor_celula = linha[coluna]
     if dados_agrupados.get(linha[coluna]) == None:
        dados_agrupados[valor_celula] = []
     dados_agrupados[valor_celula].append(linha)
   
   for chave, lista in dados_agrupados.items():
     
     dados_agrupados[chave] = somatorio(lista,coluna2)   
       
   return dados_agrupados
   
   