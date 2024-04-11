''' Usa modelo de IA para novas previsões'''

import pandas as pd
import glob
import  os

# definir caminho para saida 
output_path =  os.path.join('src', 'data', 'ready', 'new_clients.csv')

# definir caminho para ler os arquivos treinamento IA
folder_path = 'src\\data\\processed'

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
         
            # escolhendo quais colunas vamos usar para treinar o modelo
            # x vai todas as colunas que vamos usar para prever o score de credito, não vamos usar a coluna id_cliente porque ela é um numero qualquer que nao ajuda a previsao
            # y é a coluna que queremos que o modelo calcule
            x = dfs_temp.drop(["score_credito", "id_cliente",  'origin_file'], axis=1)  
            y = dfs_temp["score_credito"]
            
            from sklearn.model_selection import train_test_split
            # separamos os dados em treino e teste. Treino vamos dar para os modelos aprenderem e teste vamos usar para ver se o modelo aprendeu corretamente
            x_train, x_test,  y_train, y_test = train_test_split(x, y , test_size=0.3, random_state=1)
           
            # importar os modelos de IA
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.neighbors import KNeighborsClassifier
           
            # modelo arvore de decisao
            forest_model = RandomForestClassifier()
           
            # modelo do KNN (nearest neighbors - vizinhos mais proximos)
            neighbors_model = KNeighborsClassifier()
           
            # treinando os modelos
            forest_model.fit(x_train,y_train)
            neighbors_model.fit(x_train,y_train)
           
            # se o nosso modelo chutasse tudo "Standard", qual seria a acurácia do modelo?
            count_score = dfs_temp["score_credito"].value_counts()
            print(f"Quantidade de Score Standard qtd total de score: ",count_score['Standard']/ sum(count_score)) 
           
            # importa sklearn.metrics e calcular a acurácia
            from sklearn.metrics import accuracy_score
            
            # calcula as previsões
            pred_forest = forest_model.predict(x_test)
            pred_knn = neighbors_model.predict(x_test)
            
            # Compara as previsões com o teste
            print(f"A acurácia do modelo arvore é:",accuracy_score(y_test, pred_forest))
            print(f"A acurácia do modelo KNN é: ",accuracy_score(y_test, pred_knn))
            
             # usar a lib sklearn para transformar as colunas de texto em números. OBS.: só não aplicamos na coluna de score_credito que é o nosso objetivo
            from sklearn.preprocessing import LabelEncoder
            encoder = LabelEncoder()
                       
            # Nova previsão
            for new_client_file in glob.glob(os.path.join('src\\data\\new','*.csv')):
                new_clients = pd.read_csv(new_client_file)
                print(new_clients)
                
                for column in new_clients.columns:
                    if new_clients[column].dtype == "object" and column != "score_credito":
                        new_clients[column] = encoder.fit_transform(new_clients[column])
                
                predict =  forest_model.predict(new_clients)
                print(predict)
                
                new_clients['score_credito'] = predict
                
                dataframe.append(new_clients)
                
        except Exception as e:
            print(f"Erro ao ler arquivo {csv_file}: {e}") 
           
 
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

        
