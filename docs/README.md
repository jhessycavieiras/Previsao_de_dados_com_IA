# Documentação:

## 🧰 Recursos usados:
1. Python (versão 3.12.0)
2. Pip
3. Bibliotecas necessárias:
   - pandas (`pip install pandas`)
   - scikit-learn (`pip install scikit-learn`)
   - glob (`modulo built-in`)
   - os.path(`modulo built-in`)
4. Ambiente virtual:
    - venv (`python -m venv venv`)
    - ativar o venv (`venv/scripts/activate`)

## Estrutura de Diretórios:

* `docs/`: Documentação do projeto.
*  `src/`: Contém todos os arquivos fontes do projeto, como as funções e classes principais.
    * `data`: 
        * `raw/`: Arquivos originais dos dados.
         * `processed/`: Dados processados.
        * `new/`: Novos dados utilizados para as previsões da IA
        * `ready/`: Dados finalizados com as previsões feitas pela IA
        
    * `script/`: Scripts que rodam as funcionalidades do projeto.
        * `main.py`: Faz as predições da IA, após treinar os modelos.
        * `pre_processing.py`: Faz o pré-processamento dos dados.
        


## Dados raw

Os dados utilizados no projeto são fictícios e gerados com o [ChatGPT](=https://chat.openai.com/). Segue os dados do arquivo ".csv":

````
"id_cliente","mes","idade","profissao","salario_anual","num_contas","num_cartoes","juros_emprestimo","num_emprestimos","dias_atraso","num_pagamentos_atrasados","num_verificacoes_credito","mix_credito","divida_total","taxa_uso_credito","idade_historico_credito","investimento_mensal","comportamento_pagamento","saldo_final_mes","score_credito","emprestimo_carro","emprestimo_casa","emprestimo_pessoal","emprestimo_credito","emprestimo_estudantil"
1,"janeiro",23.0,"cientista",19114.12,3.0,4.0,3.0,4.0,3.0,7.0,4.0,"Bom",809.98,26.822619623699016,265.0,21.465380264657146,"alto_gasto_pagamento_baixos",312.49408867943663,"Good",1,1,1,1,0
2,"fevereiro",35.0,"engenheiro",50000.0,4.0,2.0,2.5,3.0,8.0,6.0,5.0,"Ruim",5500.0,55.0,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Poor",0,1,1,1,0
3,"março",40.0,"médico",80000.0,5.0,3.0,2.0,3.0,6.0,5.0,5.0,"Médio",7500.0,93.75,750.0,200.0,"alto_gasto_pagamento_alto",1500.0,"Excellent",1,1,1,1,0
4,"abril",28.0,"advogado",60000.0,3.0,2.0,3.0,2.0,4.0,4.0,4.0,"Bom",4500.0,64.28571428571429,600.0,100.0,"alto_gasto_pagamento_alto",1000.0,"Good",0,1,0,1,0
5,"maio",45.0,"professor",55000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5000.0,50.0,700.0,150.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
6,"junho",33.0,"psicólogo",48000.0,3.0,3.0,2.0,3.0,5.0,5.0,4.0,"Médio",4000.0,66.66666666666667,650.0,120.0,"alto_gasto_pagamento_baixos",1300.0,"Good",1,1,1,1,0
7,"julho",38.0,"arquiteto",70000.0,4.0,2.0,2.5,2.0,6.0,6.0,5.0,"Bom",6000.0,60.0,700.0,140.0,"alto_gasto_pagamento_alto",1400.0,"Excellent",1,0,0,1,0
8,"agosto",47.0,"autônomo",55000.0,5.0,3.0,2.0,3.0,8.0,7.0,6.0,"Ruim",5000.0,45.45454545454545,720.0,160.0,"baixo_gasto_pagamento_alto",1600.0,"Poor",0,1,1,1,0
9,"setembro",30.0,"estudante",0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,"Médio",0.0,0.0,0.0,0.0,"não_aplicável",0.0,"Standard",0,0,0,0,1
10,"outubro",34.0,"vendedor",48000.0,3.0,2.0,3.0,2.0,6.0,5.0,5.0,"Bom",4200.0,58.333333333333336,600.0,110.0,"alto_gasto_pagamento_baixos",900.0,"Good",1,0,0,1,0
11,"novembro",43.0,"consultor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5700.0,65.45454545454545,750.0,160.0,"baixo_gasto_pagamento_baixos",1400.0,"Excellent",1,1,1,1,0
12,"dezembro",25.0,"analista",40000.0,3.0,2.0,2.5,2.0,5.0,5.0,4.0,"Bom",3000.0,50.0,550.0,100.0,"alto_gasto_pagamento_alto",1000.0,"Good",0,1,0,1,0
13,"janeiro",31.0,"enfermeiro",45000.0,3.0,3.0,2.0,3.0,6.0,6.0,5.0,"Bom",3500.0,58.333333333333336,600.0,110.0,"alto_gasto_pagamento_baixos",900.0,"Good",1,0,0,1,0
14,"fevereiro",20.0,"estagiário",10000.0,1.0,1.0,3.5,1.0,3.0,2.0,2.0,"Ruim",1000.0,100.0,300.0,50.0,"alto_gasto_pagamento_alto",800.0,"Poor",0,1,0,1,0
15,"março",50.0,"jardineiro",30000.0,2.0,1.0,4.0,1.0,5.0,4.0,3.0,"Médio",3000.0,60.0,500.0,80.0,"baixo_gasto_pagamento_alto",600.0,"Standard",1,0,0,1,0
16,"abril",39.0,"pintor",35000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
17,"maio",28.0,"cozinheiro",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_alto",400.0,"Poor",0,1,1,1,0
18,"junho",42.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"baixo_gasto_pagamento_baixos",1000.0,"Good",1,1,1,1,0
19,"julho",27.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,7.0,6.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_baixos",800.0,"Standard",1,0,0,1,0
20,"agosto",37.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_alto",400.0,"Poor",0,1,0,1,0
21,"setembro",31.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_baixos",500.0,"Poor",0,1,0,1,0
22,"outubro",24.0,"mecânico",28000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2200.0,40.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Good",1,1,0,1,0
23,"novembro",29.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_alto",600.0,"Poor",0,1,1,1,0
24,"dezembro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
25,"janeiro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
26,"fevereiro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
27,"março",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
28,"abril",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
29,"maio",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
30,"junho",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
31,"julho",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
32,"agosto",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
33,"setembro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
34,"outubro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
35,"novembro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
36,"dezembro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
37,"janeiro",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
38,"fevereiro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
39,"março",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
40,"abril",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
41,"maio",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
42,"junho",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
43,"julho",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
44,"agosto",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
45,"setembro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
46,"outubro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
47,"novembro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
48,"dezembro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
49,"janeiro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
50,"fevereiro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
51,"março",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
52,"abril",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
53,"maio",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
54,"junho",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
55,"julho",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
56,"agosto",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
57,"setembro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
58,"outubro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
59,"novembro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
60,"dezembro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
61,"janeiro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
62,"fevereiro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
63,"março",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
64,"abril",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
65,"maio",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
66,"junho",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
67,"julho",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
68,"agosto",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
69,"setembro",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
70,"outubro",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
71,"novembro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
72,"dezembro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
73,"janeiro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
74,"fevereiro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
75,"março",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
76,"abril",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
77,"maio",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
78,"junho",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
79,"julho",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
80,"agosto",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
81,"setembro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
82,"outubro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
83,"novembro",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
84,"dezembro",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
85,"janeiro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
86,"fevereiro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
87,"março",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
88,"abril",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
89,"maio",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
90,"junho",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
91,"julho",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
92,"agosto",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
93,"setembro",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
94,"outubro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
95,"novembro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
96,"dezembro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
97,"janeiro",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
98,"fevereiro",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
99,"março",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
100,"abril",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
101,"maio",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
102,"junho",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
103,"julho",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
104,"agosto",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
105,"setembro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
106,"outubro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
107,"novembro",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
108,"dezembro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
109,"janeiro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
110,"fevereiro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
111,"março",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
112,"abril",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
113,"maio",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
114,"junho",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
115,"julho",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
116,"agosto",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
117,"setembro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
118,"outubro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
119,"novembro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
120,"dezembro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
121,"janeiro",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
122,"fevereiro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
123,"março",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
124,"abril",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
125,"maio",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
126,"junho",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
127,"julho",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
128,"agosto",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
129,"setembro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
130,"outubro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
131,"novembro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
132,"dezembro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
133,"janeiro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
134,"fevereiro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
135,"março",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
136,"abril",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
137,"maio",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
138,"junho",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
139,"julho",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
140,"agosto",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
141,"setembro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
142,"outubro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
143,"novembro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
144,"dezembro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
145,"janeiro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
146,"fevereiro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
147,"março",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
148,"abril",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
149,"maio",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
150,"junho",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
151,"julho",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
152,"agosto",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
153,"setembro",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
154,"outubro",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
155,"novembro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
156,"dezembro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
157,"janeiro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
158,"fevereiro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
159,"março",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
160,"abril",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
161,"maio",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
162,"junho",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
163,"julho",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
164,"agosto",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
165,"setembro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
166,"outubro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
167,"novembro",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
168,"dezembro",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
169,"janeiro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
170,"fevereiro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
171,"março",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
172,"abril",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
173,"maio",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
174,"junho",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
175,"julho",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
176,"agosto",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
177,"setembro",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
178,"outubro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
179,"novembro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
180,"dezembro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
181,"janeiro",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
182,"fevereiro",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
183,"março",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
184,"abril",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
185,"maio",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
186,"junho",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
187,"julho",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
188,"agosto",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
189,"setembro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
190,"outubro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
191,"novembro",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
192,"dezembro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
193,"janeiro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
194,"fevereiro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
195,"março",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
196,"abril",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
197,"maio",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
198,"junho",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
199,"julho",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
200,"agosto",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
201,"setembro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
202,"outubro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
203,"novembro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
204,"dezembro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
205,"janeiro",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
206,"fevereiro",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
207,"março",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
208,"abril",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
209,"maio",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
210,"junho",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
211,"julho",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
212,"agosto",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
213,"setembro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
214,"outubro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
215,"novembro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
216,"dezembro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
217,"janeiro",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
218,"fevereiro",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
219,"março",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
220,"abril",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
221,"maio",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
222,"junho",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
223,"julho",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
224,"agosto",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
225,"setembro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
226,"outubro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
227,"novembro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
228,"dezembro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
229,"janeiro",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
230,"fevereiro",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
231,"março",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
232,"abril",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
233,"maio",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
234,"junho",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
235,"julho",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
236,"agosto",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
237,"setembro",47.0,"atendente",25000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2000.0,50.0,400.0,60.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,1,1,0
238,"outubro",26.0,"engenheiro",38000.0,2.0,2.0,3.0,2.0,7.0,6.0,4.0,"Bom",3200.0,45.714285714285715,500.0,90.0,"baixo_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
239,"novembro",42.0,"jardineiro",35000.0,2.0,1.0,4.0,1.0,9.0,8.0,3.0,"Ruim",2800.0,40.0,550.0,90.0,"alto_gasto_pagamento_baixos",700.0,"Good",1,0,0,1,0
240,"dezembro",29.0,"pintor",30000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2500.0,35.714285714285715,500.0,80.0,"alto_gasto_pagamento_alto",600.0,"Good",1,1,1,1,0
241,"janeiro",38.0,"cozinheiro",28000.0,1.0,1.0,4.5,1.0,8.0,7.0,3.0,"Ruim",2200.0,55.0,450.0,70.0,"baixo_gasto_pagamento_alto",700.0,"Poor",0,1,0,1,0
242,"fevereiro",43.0,"designer",55000.0,3.0,2.0,2.5,2.0,5.0,4.0,4.0,"Bom",4500.0,75.0,620.0,120.0,"alto_gasto_pagamento_baixos",1000.0,"Good",1,0,1,1,0
243,"março",28.0,"engenheiro",40000.0,2.0,1.0,3.0,1.0,6.0,5.0,2.0,"Ruim",3500.0,58.333333333333336,550.0,100.0,"alto_gasto_pagamento_alto",800.0,"Standard",1,0,0,1,0
244,"abril",34.0,"estagiário",15000.0,1.0,1.0,4.0,1.0,4.0,3.0,2.0,"Médio",1200.0,80.0,250.0,40.0,"alto_gasto_pagamento_baixos",400.0,"Poor",0,1,0,1,0
245,"maio",49.0,"garçom",20000.0,1.0,1.0,4.5,1.0,9.0,8.0,3.0,"Ruim",1800.0,60.0,300.0,50.0,"alto_gasto_pagamento_alto",500.0,"Poor",0,1,1,1,0
246,"junho",23.0,"mecânico",25000.0,2.0,2.0,3.0,2.0,6.0,5.0,4.0,"Bom",2000.0,28.571428571428573,350.0,60.0,"baixo_gasto_pagamento_alto",600.0,"Good",1,0,0,1,0
247,"julho",31.0,"pedreiro",22000.0,1.0,1.0,4.0,1.0,10.0,9.0,3.0,"Ruim",1800.0,60.0,350.0,60.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
248,"agosto",46.0,"professor",60000.0,4.0,3.0,2.0,3.0,7.0,7.0,5.0,"Bom",5500.0,61.111111111111114,680.0,130.0,"baixo_gasto_pagamento_alto",1200.0,"Standard",1,0,0,1,0
249,"setembro",32.0,"secretário",35000.0,2.0,1.0,3.5,1.0,7.0,6.0,2.0,"Ruim",3000.0,50.0,500.0,80.0,"alto_gasto_pagamento_baixos",600.0,"Poor",0,1,0,1,0
250,"outubro",36.0,"analista",48000.0,3.0,2.0,2.5,2.0,6.0,5.0,4.0,"Bom",4000.0,57.142857142857146,600.0,110.0,"alto_gasto_pagamento_alto",900.0,"Good",1,0,0,1,0
````

## Dados de novos clientes:

Gerados com [ChatGPT](=https://chat.openai.com/). Segue os dados do arquivo ".csv":


````
mes,idade,profissao,salario_anual,num_contas,num_cartoes,juros_emprestimo,num_emprestimos,dias_atraso,num_pagamentos_atrasados,num_verificacoes_credito,mix_credito,divida_total,taxa_uso_credito,idade_historico_credito,investimento_mensal,comportamento_pagamento,saldo_final_mes,emprestimo_carro,emprestimo_casa,emprestimo_pessoal,emprestimo_credito,emprestimo_estudantil
janeiro,31.0,empresario,19300.34,6.0,7.0,17.0,5.0,52.0,19.0,7.0,Ruim,2430.21,29.934185732751413,218.0,44.50950984607408,baixo_gasto_pagamento_baixo,312.4876885895601,1,1,0,0,0
fevereiro,28.0,advogado,21000.67,5.0,6.0,15.0,4.0,45.0,16.0,6.0,Bom,1980.67,31.025842743695635,195.0,39.20593058277934,alto_gasto_pagamento_alto,500.3678219421687,0,1,0,1,0
março,35.0,médico,25000.0,4.0,5.0,12.0,3.0,40.0,13.0,5.0,Bom,2900.0,32.0,210.0,50.0,alto_gasto_pagamento_baixo,700.0,1,0,0,1,0
abril,26.0,engenheiro,18000.0,3.0,4.0,10.0,2.0,35.0,10.0,4.0,Excelente,1800.0,30.0,185.0,35.0,baixo_gasto_pagamento_alto,400.0,0,0,0,1,0
maio,30.0,professor,22000.0,5.0,6.0,14.0,4.0,48.0,18.0,6.0,Muito Ruim,2500.0,34.0,200.0,45.0,alto_gasto_pagamento_baixo,600.0,0,1,0,0,0
junho,33.0,contador,20000.0,4.0,5.0,11.0,3.0,38.0,14.0,5.0,Bom,2100.0,32.0,190.0,40.0,alto_gasto_pagamento_baixo,500.0,1,0,0,1,0
julho,29.0,enfermeiro,21000.0,3.0,4.0,9.0,2.0,36.0,11.0,4.0,Excelente,2200.0,33.0,195.0,38.0,baixo_gasto_pagamento_alto,450.0,0,0,1,0,0
agosto,32.0,designer,18000.0,4.0,5.0,10.0,2.0,33.0,12.0,4.0,Bom,1900.0,29.0,180.0,36.0,alto_gasto_pagamento_baixo,430.0,1,1,0,1,0
setembro,27.0,analista,24000.0,5.0,6.0,13.0,4.0,42.0,15.0,5.0,Muito Bom,2600.0,31.0,205.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
outubro,34.0,gerente,28000.0,6.0,7.0,16.0,5.0,50.0,17.0,6.0,Ruim,3000.0,32.0,225.0,47.0,baixo_gasto_pagamento_alto,600.0,1,0,1,0,0
novembro,31.0,tecnico,19000.0,3.0,4.0,11.0,3.0,39.0,13.0,5.0,Bom,1800.0,26.0,195.0,35.0,alto_gasto_pagamento_baixo,400.0,0,0,1,1,0
dezembro,26.0,estudante,0.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,Bom,0.0,0.0,0.0,0.0,baixo_gasto_pagamento_alto,0.0,0,0,0,0,1
janeiro,40.0,autonomo,24000.0,4.0,5.0,12.0,3.0,36.0,14.0,5.0,Bom,2500.0,31.0,210.0,40.0,alto_gasto_pagamento_baixo,550.0,1,0,0,1,0
fevereiro,29.0,vendedor,20000.0,3.0,4.0,10.0,2.0,34.0,11.0,4.0,Ruim,2100.0,30.0,185.0,38.0,alto_gasto_pagamento_baixo,480.0,0,0,1,0,0
março,32.0,advogado,28000.0,5.0,6.0,14.0,4.0,45.0,16.0,6.0,Muito Ruim,2800.0,32.0,215.0,43.0,baixo_gasto_pagamento_alto,600.0,1,1,0,1,0
abril,27.0,médico,32000.0,6.0,7.0,18.0,5.0,55.0,20.0,7.0,Bom,3500.0,34.0,230.0,50.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
maio,30.0,engenheiro,26000.0,4.0,5.0,13.0,3.0,42.0,15.0,5.0,Bom,3100.0,33.0,200.0,45.0,alto_gasto_pagamento_baixo,600.0,1,0,1,0,0
junho,33.0,professor,29000.0,5.0,6.0,15.0,4.0,48.0,18.0,6.0,Bom,3200.0,34.0,210.0,48.0,baixo_gasto_pagamento_alto,650.0,0,0,0,1,0
julho,28.0,contador,23000.0,4.0,5.0,12.0,3.0,40.0,14.0,5.0,Bom,2700.0,32.0,195.0,42.0,alto_gasto_pagamento_baixo,580.0,1,0,1,1,0
agosto,31.0,enfermeiro,22000.0,3.0,4.0,10.0,2.0,35.0,12.0,4.0,Bom,2400.0,30.0,190.0,38.0,alto_gasto_pagamento_baixo,500.0,0,1,0,0,0
setembro,36.0,designer,25000.0,5.0,6.0,14.0,4.0,43.0,16.0,6.0,Bom,2800.0,31.0,205.0,45.0,baixo_gasto_pagamento_alto,600.0,1,0,1,0,0
outubro,29.0,analista,27000.0,6.0,7.0,16.0,5.0,48.0,18.0,6.0,Bom,2900.0,33.0,220.0,48.0,alto_gasto_pagamento_baixo,650.0,0,1,0,1,0
novembro,34.0,gerente,30000.0,7.0,8.0,18.0,6.0,52.0,20.0,7.0,Muito Ruim,3200.0,34.0,235.0,50.0,baixo_gasto_pagamento_alto,700.0,1,0,1,0,0
dezembro,30.0,tecnico,22000.0,4.0,5.0,13.0,3.0,39.0,14.0,5.0,Bom,2500.0,31.0,200.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
janeiro,25.0,estudante,0.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,Bom,0.0,0.0,0.0,0.0,baixo_gasto_pagamento_alto,0.0,0,0,0,0,1
fevereiro,39.0,autonomo,26000.0,5.0,6.0,13.0,4.0,36.0,15.0,5.0,Bom,2800.0,32.0,210.0,40.0,alto_gasto_pagamento_baixo,600.0,1,1,0,1,0
março,30.0,vendedor,21000.0,4.0,5.0,11.0,3.0,38.0,12.0,4.0,Ruim,2200.0,30.0,185.0,38.0,alto_gasto_pagamento_baixo,480.0,0,0,1,0,0
abril,35.0,advogado,29000.0,6.0,7.0,15.0,5.0,47.0,17.0,6.0,Ruim,2900.0,32.0,225.0,44.0,baixo_gasto_pagamento_alto,650.0,1,0,1,1,0
maio,28.0,médico,33000.0,7.0,8.0,18.0,6.0,55.0,21.0,7.0,Bom,3600.0,35.0,240.0,50.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
junho,31.0,engenheiro,28000.0,5.0,6.0,14.0,4.0,43.0,16.0,6.0,Bom,3200.0,33.0,210.0,48.0,alto_gasto_pagamento_baixo,650.0,1,0,1,0,0
julho,34.0,professor,30000.0,6.0,7.0,16.0,5.0,50.0,19.0,7.0,Bom,3400.0,34.0,220.0,48.0,baixo_gasto_pagamento_alto,700.0,0,1,0,1,0
agosto,29.0,contador,24000.0,4.0,5.0,12.0,3.0,38.0,14.0,5.0,Bom,2900.0,32.0,200.0,45.0,alto_gasto_pagamento_baixo,600.0,1,0,1,0,0
setembro,36.0,enfermeiro,23000.0,3.0,4.0,10.0,2.0,36.0,12.0,4.0,Bom,2500.0,31.0,195.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
outubro,27.0,designer,26000.0,5.0,6.0,13.0,4.0,42.0,15.0,5.0,Bom,3000.0,33.0,205.0,45.0,baixo_gasto_pagamento_alto,650.0,1,0,1,0,0
novembro,32.0,analista,28000.0,6.0,7.0,15.0,5.0,48.0,18.0,6.0,Bom,3200.0,34.0,220.0,48.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
dezembro,35.0,gerente,32000.0,7.0,8.0,17.0,6.0,52.0,20.0,7.0,Muito Ruim,3400.0,35.0,235.0,50.0,baixo_gasto_pagamento_alto,750.0,1,0,1,0,0
janeiro,30.0,tecnico,23000.0,4.0,5.0,14.0,3.0,39.0,13.0,5.0,Bom,2700.0,32.0,205.0,42.0,alto_gasto_pagamento_baixo,600.0,0,1,0,1,0
fevereiro,26.0,estudante,0.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,Bom,0.0,0.0,0.0,0.0,baixo_gasto_pagamento_alto,0.0,0,0,0,0,1
março,40.0,autonomo,27000.0,5.0,6.0,13.0,4.0,35.0,15.0,5.0,Bom,3000.0,32.0,215.0,40.0,alto_gasto_pagamento_baixo,600.0,1,1,0,1,0
abril,28.0,vendedor,22000.0,4.0,5.0,12.0,3.0,37.0,12.0,4.0,Ruim,2400.0,30.0,190.0,38.0,alto_gasto_pagamento_baixo,500.0,0,0,1,0,0
maio,33.0,advogado,31000.0,6.0,7.0,16.0,5.0,50.0,18.0,6.0,Ruim,3100.0,33.0,225.0,45.0,baixo_gasto_pagamento_alto,650.0,1,0,1,1,0
junho,26.0,médico,35000.0,7.0,8.0,18.0,6.0,54.0,21.0,7.0,Bom,3800.0,35.0,240.0,50.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
julho,31.0,engenheiro,29000.0,5.0,6.0,15.0,4.0,45.0,17.0,6.0,Bom,3400.0,34.0,210.0,48.0,alto_gasto_pagamento_baixo,650.0,1,0,1,0,0
agosto,34.0,professor,32000.0,6.0,7.0,17.0,5.0,52.0,19.0,7.0,Bom,3600.0,35.0,220.0,48.0,baixo_gasto_pagamento_alto,700.0,0,1,0,1,0
setembro,28.0,contador,25000.0,4.0,5.0,11.0,3.0,38.0,14.0,5.0,Bom,2900.0,32.0,200.0,45.0,alto_gasto_pagamento_baixo,600.0,1,0,1,0,0
outubro,35.0,enfermeiro,24000.0,3.0,4.0,10.0,2.0,35.0,12.0,4.0,Bom,2600.0,31.0,195.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
novembro,30.0,designer,27000.0,5.0,6.0,14.0,4.0,42.0,15.0,5.0,Bom,3200.0,33.0,205.0,45.0,baixo_gasto_pagamento_alto,600.0,1,0,1,0,0
dezembro,33.0,analista,30000.0,6.0,7.0,16.0,5.0,48.0,18.0,6.0,Bom,3500.0,34.0,220.0,48.0,alto_gasto_pagamento_baixo,650.0,0,1,0,1,0
janeiro,38.0,gerente,33000.0,7.0,8.0,17.0,6.0,52.0,20.0,7.0,Muito Ruim,3600.0,35.0,235.0,50.0,baixo_gasto_pagamento_alto,700.0,1,0,1,0,0
fevereiro,29.0,tecnico,24000.0,4.0,5.0,14.0,3.0,40.0,14.0,5.0,Bom,2800.0,32.0,205.0,42.0,alto_gasto_pagamento_baixo,600.0,0,1,0,1,0
março,27.0,estudante,0.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,Bom,0.0,0.0,0.0,0.0,baixo_gasto_pagamento_alto,0.0,0,0,0,0,1
abril,39.0,autonomo,28000.0,5.0,6.0,13.0,4.0,35.0,15.0,5.0,Bom,3000.0,32.0,210.0,40.0,alto_gasto_pagamento_baixo,600.0,1,1,0,1,0
maio,29.0,vendedor,23000.0,4.0,5.0,12.0,3.0,37.0,12.0,4.0,Ruim,2500.0,31.0,195.0,38.0,alto_gasto_pagamento_baixo,500.0,0,0,1,0,0
junho,34.0,advogado,32000.0,6.0,7.0,15.0,5.0,48.0,17.0,6.0,Ruim,3200.0,33.0,230.0,45.0,baixo_gasto_pagamento_alto,650.0,1,0,1,1,0
julho,28.0,médico,36000.0,7.0,8.0,18.0,6.0,54.0,21.0,7.0,Bom,3800.0,35.0,240.0,50.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
agosto,32.0,engenheiro,30000.0,5.0,6.0,15.0,4.0,45.0,17.0,6.0,Bom,3400.0,34.0,215.0,48.0,alto_gasto_pagamento_baixo,650.0,1,0,1,0,0
setembro,27.0,professor,33000.0,6.0,7.0,17.0,5.0,50.0,19.0,7.0,Bom,3700.0,35.0,225.0,48.0,baixo_gasto_pagamento_alto,700.0,0,1,0,1,0
outubro,35.0,contador,26000.0,4.0,5.0,11.0,3.0,38.0,14.0,5.0,Bom,3000.0,32.0,205.0,45.0,alto_gasto_pagamento_baixo,600.0,1,0,1,0,0
novembro,31.0,enfermeiro,25000.0,3.0,4.0,10.0,2.0,35.0,12.0,4.0,Bom,2700.0,31.0,200.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
dezembro,26.0,designer,28000.0,5.0,6.0,14.0,4.0,42.0,15.0,5.0,Bom,3200.0,33.0,210.0,45.0,baixo_gasto_pagamento_alto,600.0,1,0,1,0,0
janeiro,32.0,analista,30000.0,6.0,7.0,16.0,5.0,48.0,18.0,6.0,Bom,3500.0,34.0,220.0,48.0,alto_gasto_pagamento_baixo,650.0,0,1,0,1,0
fevereiro,37.0,gerente,34000.0,7.0,8.0,17.0,6.0,52.0,20.0,7.0,Muito Ruim,3600.0,35.0,235.0,50.0,baixo_gasto_pagamento_alto,700.0,1,0,1,0,0
março,30.0,tecnico,25000.0,4.0,5.0,14.0,3.0,40.0,14.0,5.0,Bom,2900.0,32.0,210.0,42.0,alto_gasto_pagamento_baixo,600.0,0,1,0,1,0
abril,28.0,estudante,0.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,Bom,0.0,0.0,0.0,0.0,baixo_gasto_pagamento_alto,0.0,0,0,0,0,1
maio,41.0,autonomo,29000.0,5.0,6.0,13.0,4.0,35.0,15.0,5.0,Bom,3200.0,32.0,215.0,40.0,alto_gasto_pagamento_baixo,600.0,1,1,0,1,0
junho,28.0,vendedor,24000.0,4.0,5.0,12.0,3.0,37.0,12.0,4.0,Ruim,2600.0,31.0,195.0,38.0,alto_gasto_pagamento_baixo,500.0,0,0,1,0,0
julho,35.0,advogado,33000.0,6.0,7.0,15.0,5.0,48.0,17.0,6.0,Ruim,3200.0,33.0,225.0,45.0,baixo_gasto_pagamento_alto,650.0,1,0,1,1,0
agosto,29.0,médico,37000.0,7.0,8.0,18.0,6.0,54.0,21.0,7.0,Bom,3800.0,35.0,240.0,50.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
setembro,32.0,engenheiro,31000.0,5.0,6.0,15.0,4.0,45.0,17.0,6.0,Bom,3500.0,34.0,215.0,48.0,alto_gasto_pagamento_baixo,650.0,1,0,1,0,0
outubro,27.0,professor,34000.0,6.0,7.0,17.0,5.0,50.0,19.0,7.0,Bom,3700.0,35.0,225.0,48.0,baixo_gasto_pagamento_alto,700.0,0,1,0,1,0
novembro,32.0,contador,27000.0,4.0,5.0,11.0,3.0,38.0,14.0,5.0,Bom,3100.0,32.0,205.0,45.0,alto_gasto_pagamento_baixo,600.0,1,0,1,0,0
dezembro,36.0,enfermeiro,26000.0,3.0,4.0,10.0,2.0,35.0,12.0,4.0,Bom,2900.0,31.0,200.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
janeiro,31.0,designer,29000.0,5.0,6.0,14.0,4.0,42.0,15.0,5.0,Bom,3300.0,33.0,210.0,45.0,baixo_gasto_pagamento_alto,600.0,1,0,1,0,0
fevereiro,38.0,analista,31000.0,6.0,7.0,16.0,5.0,48.0,18.0,6.0,Bom,3600.0,34.0,220.0,48.0,alto_gasto_pagamento_baixo,650.0,0,1,0,1,0
março,31.0,gerente,34000.0,7.0,8.0,17.0,6.0,52.0,20.0,7.0,Muito Ruim,3800.0,35.0,235.0,50.0,baixo_gasto_pagamento_alto,700.0,1,0,1,0,0
abril,30.0,tecnico,26000.0,4.0,5.0,14.0,3.0,40.0,14.0,5.0,Bom,3000.0,32.0,210.0,42.0,alto_gasto_pagamento_baixo,600.0,0,1,0,1,0
maio,26.0,estudante,0.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,Bom,0.0,0.0,0.0,0.0,baixo_gasto_pagamento_alto,0.0,0,0,0,0,1
junho,40.0,autonomo,30000.0,5.0,6.0,13.0,4.0,35.0,15.0,5.0,Bom,3200.0,32.0,215.0,40.0,alto_gasto_pagamento_baixo,600.0,1,1,0,1,0
julho,27.0,vendedor,25000.0,4.0,5.0,12.0,3.0,37.0,12.0,4.0,Ruim,2700.0,31.0,195.0,38.0,alto_gasto_pagamento_baixo,500.0,0,0,1,0,0
agosto,34.0,advogado,34000.0,6.0,7.0,15.0,5.0,48.0,17.0,6.0,Ruim,3200.0,33.0,225.0,45.0,baixo_gasto_pagamento_alto,650.0,1,0,1,1,0
setembro,28.0,médico,38000.0,7.0,8.0,18.0,6.0,54.0,21.0,7.0,Bom,3800.0,35.0,240.0,50.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
outubro,33.0,engenheiro,32000.0,5.0,6.0,15.0,4.0,45.0,17.0,6.0,Bom,3500.0,34.0,215.0,48.0,alto_gasto_pagamento_baixo,650.0,1,0,1,0,0
novembro,28.0,professor,35000.0,6.0,7.0,17.0,5.0,50.0,19.0,7.0,Bom,3700.0,35.0,225.0,48.0,baixo_gasto_pagamento_alto,700.0,0,1,0,1,0
dezembro,33.0,contador,28000.0,4.0,5.0,11.0,3.0,38.0,14.0,5.0,Bom,3200.0,32.0,205.0,45.0,alto_gasto_pagamento_baixo,600.0,1,0,1,0,0
janeiro,38.0,enfermeiro,27000.0,3.0,4.0,10.0,2.0,35.0,12.0,4.0,Bom,2900.0,31.0,200.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
fevereiro,27.0,designer,30000.0,5.0,6.0,14.0,4.0,42.0,15.0,5.0,Bom,3300.0,33.0,210.0,45.0,baixo_gasto_pagamento_alto,600.0,1,0,1,0,0
março,32.0,analista,32000.0,6.0,7.0,16.0,5.0,48.0,18.0,6.0,Bom,3600.0,34.0,220.0,48.0,alto_gasto_pagamento_baixo,650.0,0,1,0,1,0
abril,37.0,gerente,35000.0,7.0,8.0,17.0,6.0,52.0,20.0,7.0,Muito Ruim,3800.0,35.0,235.0,50.0,baixo_gasto_pagamento_alto,700.0,1,0,1,0,0
maio,30.0,tecnico,27000.0,4.0,5.0,14.0,3.0,40.0,14.0,5.0,Bom,3100.0,32.0,210.0,42.0,alto_gasto_pagamento_baixo,600.0,0,1,0,1,0
junho,26.0,estudante,0.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,Bom,0.0,0.0,0.0,0.0,baixo_gasto_pagamento_alto,0.0,0,0,0,0,1
julho,40.0,autonomo,31000.0,5.0,6.0,13.0,4.0,35.0,15.0,5.0,Bom,3300.0,32.0,215.0,40.0,alto_gasto_pagamento_baixo,600.0,1,1,0,1,0
agosto,27.0,vendedor,26000.0,4.0,5.0,12.0,3.0,37.0,12.0,4.0,Ruim,2800.0,31.0,195.0,38.0,alto_gasto_pagamento_baixo,500.0,0,0,1,0,0
setembro,34.0,advogado,35000.0,6.0,7.0,15.0,5.0,48.0,17.0,6.0,Ruim,3300.0,33.0,225.0,45.0,baixo_gasto_pagamento_alto,650.0,1,0,1,1,0
outubro,28.0,médico,39000.0,7.0,8.0,18.0,6.0,54.0,21.0,7.0,Bom,3900.0,35.0,240.0,50.0,alto_gasto_pagamento_baixo,700.0,0,1,0,1,0
novembro,33.0,engenheiro,33000.0,5.0,6.0,15.0,4.0,45.0,17.0,6.0,Bom,3600.0,34.0,215.0,48.0,alto_gasto_pagamento_baixo,650.0,1,0,1,0,0
dezembro,27.0,professor,36000.0,6.0,7.0,17.0,5.0,50.0,19.0,7.0,Bom,3800.0,35.0,225.0,48.0,baixo_gasto_pagamento_alto,700.0,0,1,0,1,0
janeiro,32.0,contador,29000.0,4.0,5.0,11.0,3.0,38.0,14.0,5.0,Bom,3200.0,32.0,205.0,45.0,alto_gasto_pagamento_baixo,600.0,1,0,1,0,0
fevereiro,27.0,enfermeiro,28000.0,3.0,4.0,10.0,2.0,35.0,12.0,4.0,Bom,3000.0,31.0,200.0,42.0,alto_gasto_pagamento_baixo,550.0,0,1,0,1,0
março,33.0,designer,31000.0,5.0,6.0,14.0,4.0,42.0,15.0,5.0,Bom,3400.0,33.0,210.0,45.0,baixo_gasto_pagamento_alto,600.0,1,0,1,0,0
````