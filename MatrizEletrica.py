

import pandas as pd

ctrl = int(input("Digite '1' para iniciar o programa: "))

while ctrl == 1: 
    
    """Fonte, porcentagem, produção em MW"""

    energia = [
        ["Hidrica", 59.9, 109276],
        ["Eolica", 9.4, 17131],
        ["Biomassa", 8.4, 15273],
        ["Gas Natural", 8.2, 14946],
        ["Petroleo", 5, 9178],
        ["Carvao Mineral", 2, 3583],
        ["Fotovoltaica", 1.6, 3093],
        ["Nuclear", 1.1, 1990],
        ["Importacao", 4.5, 8170]
    ]
    
    """Região, demanda residencial, demanda comercial, demanda industrial"""

    consumo = [
        ["Norte", 9.497, 15.204, 4.909],
        ["Nordeste", 27.059, 22.370, 17.255],
        ["Sudeste", 65.255, 88.828, 46.877],
        ["Sul", 21.247, 32.258, 14.969],
        ["Centro Oeste", 11.311, 8.737, 7.282]
    ]
    
    """Fonte, custo, imposto"""

    custos = [
        ["Hidrica", 7800, 40],
        ["Eolica", 4350, 180],
        ["Biomassa", 5500, 190],
        ["Gas Natural", 3400, 280],
        ["Petroleo", 5900, 280],
        ["Carvao Mineral", 10000, 620],
        ["Fotovoltaica", 3000, 150],
        ["Nuclear", 23500, 740],
        ["Importacao", 8580, 120]
    ]
    
    
    custoTotal = 0
    
    prodTotal = 0
    
    
    for i in range(len(custos)):
        
        
        custoProd = custos[i][1] + custos[i][2]
        
        
        if energia[i][0] == "Carvao Mineral":
            
            producao = energia[i][2] * 0.05
            custoTotal += custoProd * producao
            prodTotal += producao

    
        elif energia[i][0] == "Nuclear":
       
            producao = energia[i][2]
            custoTotal += custoProd * producao
            prodTotal += producao
    
        else:
       
            producao = energia[i][2]
            custoTotal += custoProd * producao
            prodTotal += producao


    custoMW = custoTotal / prodTotal


    def calculos(consumotb):
    
        consumotb["Custo Total"] = (
            consumotb["Residencial"] * custoMW +
            consumotb["Comercial"] * custoMW +
            consumotb["Industrial"] * custoMW)
        
        consumotb[["Custo Total"]] = consumotb[["Custo Total"]].round(2)
    

        return consumotb



    def processoDados(entrada):   

    
        if entrada == 'arquivo':
       
            arquivo = input("Digite o nome do arquivo (com extensão .txt ou .csv): ")
            demandasSM = pd.read_csv(arquivo)
        
        elif entrada == 'teclado':
       
            dados = []
            print("Digite os dados de consumo para cada região (formato: Região, Residencial, Comercial, Industrial). Digite 'fim' para encerrar.")
        
            while True:
            
                entrada = input()


                if entrada.lower() == 'fim':
                    
                    break

                dados.append(entrada.split(","))

            demandasSM = pd.DataFrame(dados, columns=["Região", "Residencial", "Comercial", "Industrial"])

            demandasSM[["Residencial", "Comercial", "Industrial"]] = demandasSM[["Residencial", "Comercial", "Industrial"]].astype(int)

        else:
       
            print("Tipo de entrada inválido.")
    
    
        consumotb = pd.DataFrame(consumo, columns=["Região", "Residencial", "Comercial", "Industrial"])


        for index, row in demandasSM.iterrows():
       
            consumotb.loc[consumotb["Região"] == row["Região"], ["Residencial", "Comercial", "Industrial"]] = row[["Residencial", "Comercial", "Industrial"]].values
    
    
        resultadotb = calculos(consumotb)


        return resultadotb



    def arquivo(tabela, formato):
    
        if formato == "tela":
        
            print(tabela)
    
        elif formato == "txt":
        
            tabela.to_csv("resultado.txt")
            print("Resultados salvos em resultado.txt")
   
        elif formato == "csv":
        
            tabela.to_csv("resultado.csv")
            print("Resultados salvos em resultado.csv")
   
        else:
       
            print("Formato de saída inválido.")



    entrada = input("Digite 'arquivo' para fornecer um arquivo .txt ou .csv, ou 'teclado' para entrada manual: ").lower()
    resultadotb = processoDados(entrada)



    if resultadotb is not None:
   
        formato = input("Digite o formato de saída ('tela', 'txt' ou 'csv'): ").lower()
        arquivo(resultadotb, formato=formato)
        
        

    ctrl = int(input("Digite '0' para finalizar ou '1' para fazer outra simulação: "))