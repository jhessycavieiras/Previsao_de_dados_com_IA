'''Tratamento dos dados'''

import pandas as pd
import os
import glob 


# definir caminho para ler os arquivos
folder_path = 'src\\data\\raw'

# definir caminho para saida 
output_path =  os.path.join('src', 'data', 'processed', 'processed.csv')

# listar todos os arquivos csv
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Tratamento 
if not csv_files:
    print("Nenhum arquivo encontrado")
    
else:
# dataframe  = tabela na memória para guardar os conteúdos dos arquivos
    dataframe = []
    
    for csv_file in csv_files:
        
        try:
            # ler arquivo 
            dfs_temp = pd.read_csv(csv_file) 
           
            # ler nome do arquivo excel
            file_name = os.path.basename(csv_file)
           
            # criar column com nome do arquivo de origem
            dfs_temp['origin_file'] = file_name
            
            # remove dados nulos se houver
            dfs_temp.dropna()
            
            # verificar se temos valores vazios ou valores reconhecidos em formato errado
            print(dfs_temp.info())
            print(dfs_temp.columns)
            
            # usar a lib sklearn para transformar as colunas de texto em números. OBS.: só não aplicamos na coluna de score_credito que é o nosso objetivo
            from sklearn.preprocessing import LabelEncoder
            encoder = LabelEncoder()
           
            for column in dfs_temp.columns:
                if  dfs_temp[column].dtype == "object" and column != "score_credito":
                    dfs_temp[column] = encoder.fit_transform(dfs_temp[column])
                    # verificar se as colunas foram alteradas
                    print(dfs_temp)
                    
            dataframe.append(dfs_temp)

        except Exception as e:
            print(f"Erro ao ler arquivo {file_name}: {e}")
            

 # Se o  dataframe não estiver vazio
    if dataframe:
        #concatena todas as tabelas salvas no dfs em uma unica tabela
        result = pd.concat(dataframe, ignore_index=True)
        #caminho de saída
        output_file = output_path
        
        #salvar a planilha na pasta indicada
        result.to_csv(output_file, index=False)  
        
    else:
        print("nenhum dado for processado")













# calculamos as previsoes

# comparamos as previsoes com o y_teste
# esse score queremos o maior (maior acuracia, mas tb tem que ser maior do que o chute de tudo Standard)