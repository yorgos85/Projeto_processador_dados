#funcao para converter os dados.

def converte_dados(dado, tipo):
    dado_convertido = None
    if tipo == int:
        dado_convertido = int(dado)
    elif tipo == float:
        dado_convertido = float(dado)   
    elif tipo == bool:
        if dado == 'True':
            dado_convertido = True
        else:
            dado_convertido = False 
    else:
            dado_convertido = dado   
             
    return dado_convertido 
    
    




#funcao para carregar o arquivo.

def carrega_arquivo(nome_arquivo,separador, tipos):
    f = open(nome_arquivo, 'r') #ABRINDO ARQUIVO
    linhas = f.readlines() #LENDO AS LINHAS
    cabecalho = linhas[0].replace('\n','').split(separador)
    alunos = []
    
    #percorre as linhas
    for linha in linhas[1:]:
      dados_linha = linha.replace('\n','').split(separador)
      
      aluno = {}
      
      
      
      #percorre as colunas de cada linha
      for coluna, tipo in enumerate(tipos):
          
          campo = cabecalho[coluna]
          
          aluno[campo] = converte_dados(dados_linha[coluna], tipo)
      
      alunos.append(aluno) 
        
    return alunos, cabecalho
     
#funcao de salvamento de dados.

def salvar_arquivo(nome_arquivo,separador, dados, cabecalho = None):
    f = open(nome_arquivo, 'w') #Abrindo arquivo modo escrita
    
    cabecalho_str = ''
    
    for coluna in cabecalho:
        cabecalho_str += coluna 
        if coluna != cabecalho[-1]:
           cabecalho_str += separador  
    cabecalho_str += '\n' 
    
    f.write(cabecalho_str) 
    
    for linha in dados:
         linha_str = ''
         for coluna, valor in linha.items():
             linha_str += str(valor) 
             if coluna != cabecalho[-1]:
                 linha_str += separador
         linha_str += '\n'
         f.write(linha_str)        
    
          
    f.close()  
            
    
    
    
   
    
    