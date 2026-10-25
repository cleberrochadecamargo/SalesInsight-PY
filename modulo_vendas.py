    # Importar a biblioteca .csv, que permite ler e escrever arquivos CSV.
import csv 

    # Importa uma biblioteca que permite gerar valores aleatórios.
import random

    # -from pathlib -> indica de qual módulo queremos importar.
    # -import Path -> importa a classe Path, utiliza para trabalhar
    # com caminhos dde arquivos e pastas. 
from pathlib import Path

  
   ## GERA UM ARQUIVO .CSV FICTÍCIO PARA A ANÁLISE.
def gerar_dataset_sintetico(caminho="vendas.csv", quantidade=120):

    # def = criar função;
    # gerar_dataset_sintetico = nome que escolhemos para a função;
    # caminho = a onde o salvar o arquivo;
    # vendas.csv = nome do arquivo gerado;
    # quantidade = quantidade de registros que queremos criar;
    # ':' = indica o início do bloco da função;
    # Os valores entre parênteses são chamados de parâmetros. Eles
    # permitem configurar a função quando a chamarmos.
    
    categorias = ["Eletrônicos", "Alimentos", "Roupas", "Casa"]
    regioes = ["Sul", "Sudeste", "Norte", "Nordeste", "Centro-Oeste"]

    with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
        
        # with open (...) as arquivo:
        # open = anre um arquivo;
        # caminho = nome do arquivo que queremos abrir (vendas.csv);
        # mode="w" = siginifica write;
        # new line="" = evita linhas em branco;
        #encoding="utf-8" = permite escrever os caracteres ç e ã;
        # as arquivo = guarda a referência ao arquivo aberto na variável arquivo;
        # with = garante que o arquivo seja fechado automaticamente.

        escritor = csv.writer(arquivo)
        #csv.writer(...) = cria um objeto capaz de escrever linhas no CSV;
        # escritor = o nome da variável que guarda esse objeto.

        escritor.writerow([
            "id_venda",
            "id_cliente",
            "produto",
            "categoria",
            "regiao",
            "quantidade",
            "preco_unitario"
        ])

        # riterow()  = escreve uma linha no arquivo, o cabeçalho,
        # id_venda, produto, caregoria ...


        for numero in range(1, quantidade + 1):

            # for = indica um laço de repetição;
            # numero = variavel que recebe o valor de cada repetição;
            # in = indica da onde vem os valores;
            # gange(...): gera os nº de 1 até quantidade solicitada,
            # quantidede vale 120, executará 120 vezes o laço, variando de 1 a 120.

            produto = f"Produto {numero}"
            categoria = random.choice(categorias)
            regiao = random.choice(regioes)
            id_cliente = random.randint(1, 30)
            quantidade_vendida = random.randint(1, 20)
            preco = round(random.uniform(10, 1000), 2)
            quantidade_csv = quantidade_vendida
            preco_csv = preco

            # produto = criar nome do produto;
            # f = permite inserir o valor de uma variável dentro do texto;
            # random.choice(...) = seleciona aleatoriamente um elemento da lista 
            # categorias / regiao;
            # random.randint(1, 30) = atribui cada venda a um dos 30 clientes fictícios.
            # random.randint(1, 20) = gera quantidade vendida entre 1 e 20;
            # random.uniform(10, 1000) gera um valor decimal entre 10 e 1.000;
            # round(..., 2) arredonda o resultado para duas casas decimais;
            # quantidade_csv = quantidade_vendida = inicialmente, guarda a quantidade gerada;
            # preco_csv = preco = inicialmente, guarda o preço gerado.

            if random.random() <0.05:
                quantidade_csv = ""

            if random.random() <0.05:
                preço_csv = ""            

            # random.random() = gera um número decimal entre 0 e 1,
            # < 0.05 = tem aproximadamente 5% de chance de ser verdadeiro;
            # = "" = substitui o valor por um campo vazio.    
         
            escritor.writerow([
                numero,
                id_cliente,
                produto,
                categoria,
                regiao,
                quantidade_csv,
                preco_csv
            ])
            # writerow(...) = grava uma linha no CSV com os seis valores da venda
            # atual. Cada vez que o for se repetir, uma nova linha será gravada.

    print(f"Arquivo criado: {caminho}")
    print(f"Quantidade de registros: {quantidade}")
        # print(...) = exibe uma informação no terminal;
        # f"..." = permite inserir valores de variáveis diretamente no texto;
        # {caminho}: mostra o nome ou caminho do arquivo criado;
        # {quantidade}: mostra quantos registros foram gerados.


    ## EXIBE INFORMAÇÕES BÁSICAS SOBRE O ARQUIVO DE VENDAS.
def inspecionar_dados(caminho="vendas.csv"):
    # def inspecionar_dados(...)= cria uma função para analisar o CSV.

    with open(caminho, mode="r", newline="", encoding="utf-8") as arquivo:
    # def inspecionar_dados(...)= cria uma função para analisar o CSV.
            
        leitor = csv.DictReader(arquivo)
    # csv.DictReader(arquivo)= lê cada linha como um dicionário, usando os nomes das colunas como chaves.

        registros = list(leitor)
    # len(registros)= conta quantos registros existem.

    print("\n--- INSPEÇÃO DOS DADOS ---")
    print(f"Total de registros: {len(registros)}")

    if registros:
        print(f"Colunas encontradas: {list(registros[0].keys())}")
    # registros[0].keys()= obtém os nomes das colunas do primeiro registro.

        campos_vazios = {}
    # campos_vazios = {}: cria um dicionário para armazenar a quantidade de campos vazios por coluna.

        for coluna in registros[0].keys():
            quantidade_vazios = sum(
                1 for registro in registros
                if not str(registro.get(coluna, "")).strip()
            )
                # registro[coluna].strip()= remove espaços nas extremidades do texto;
                # se restar uma string vazia, o campo é considerado vazio.
                # sum(...)= soma quantas vezes a condição de campo vazio é verdadeira.
            campos_vazios[coluna] = quantidade_vazios

        print(f"Campos vazios por coluna: {campos_vazios}")


    ## LIMPA E CONVERTE OS DADOS DO ARQUIVO DE VENDAS.
def limpar_dados(caminho="vendas.csv"):
    # def limpar_dados(...) = cria uma função que recebe o caminho do arquivo.
    # caminho="vendas.csv" = define o arquivo padrão caso nenhum outro caminho
    # seja informado.

    with open(caminho, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        registros = list(leitor)
    # open(..., mode="r") = abre o arquivo para leitura.
    # encoding="utf-8" = permite ler corretamente caracteres como os acentos
    # de “Eletrônicos”.
    # csv.DictReader(arquivo) = interpreta cada linha como um dicionário,
    # usando os nomes das colunas como chaves.
    # list(leitor) = transforma os registros lidos em uma lista para que
    # possam ser percorridos mais de uma vez.

    registros_limpos = []

    for registro in registros:
        registro = {
            coluna: valor.strip()
            for coluna, valor in registro.items()
        }
        # valor.strip() = percorre cada campo do registro e remove espaços, no início
        # e no fim do texto e campo contendo apenas espaços passa a ser uma string
        # vazia, "".

        if any(valor == "" for valor in registro.values()):
            continue
        # registro.values() = obtém os valores do dicionário.
        # valor == "" = verifica se um valor está vazio.
        # any(...) = verifica se pelo menos uma condição é verdadeira.
        # continue = pula o registro atual e passa para o próximo.

        try:
            registro["id_venda"] = int(registro["id_venda"])
            registro["id_cliente"] = int(registro["id_cliente"])
            registro["quantidade"] = int(registro["quantidade"])
            registro["preco_unitario"] = float(registro["preco_unitario"])
        except ValueError:
            continue
        # try/except = tenta fazer as conversões. Se algum valor não puder ser convertido,
        # gera um ValueError e impede que um valor inválido interrompe todo o programa.
        # Converter os valores para números.
        # int() = converte a quantidade para inteiro.
        # float() = converte a quantidade para inteiro.
        
        registros_limpos.append(registro)
        # Se o registro passou pelas verificações e conversões, ele é adicionado à lista
        # registros_limpos 

    print("\n--- LIMPEZA DOS DADOS ---")
    print(f"Registros originais: {len(registros)}")
    print(f"Registros válidos: {len(registros_limpos)}")
    print(f"Registros descartados: {len(registros) - len(registros_limpos)}")
    # print() = mostram a quantidade de registros originais, válidos e descartados.

    return registros_limpos 
    # Devolve a lista limpa para que outras funções possam utilizá-la posteriormente.


    ## CALCULA A RECEITA TOTAL E A FAIXA DE PREÇO DE CADA VENDA.
def calcular_metricas(registros):
    # Define uma função chamada calcular_metricas que recebe uma lista de vendas.

    for registro in registros:
        receita = registro["quantidade"] * registro["preco_unitario"]
        registro["receita_total"] = round(receita,2)
    # for registro in registros = percorre essa lista, analisando uma venda por vez.
    # registro = representa um dicionário com os dados de uma venda, como quantidade,
    # preço e categoria.
    # registro["quantidade"] * registro["preco_unitario"] = multiplica a quantidade
    # pelo preço unitário.
    # registro["receita_total"] = adiciona ao dicionário o campo receita_total.
    # round(receita, 2) = arredonda o resultado para duas casas decimais.
    
        if receita < 500:
            registro["faica_preco"] = "Baixo"

        elif receita <= 2000:
            registro["faica_preco"] = "Médio"

        else:
            registro["faica_preco"] = "Alto"
    # if, elif e else = classificam a venda em uma das três faixas.
    # se if verdadeiro = "Baixo"; se if falso e elif verdadeiro = "Médio";
    # se nenhuma condição antetior for verdadeira, classifica como "Alto".           

    print("\n--- CÁLCULO DAS MÉTRICAS ---")
    print(f"Vendas processadas: {len(registros)}")
    # print() = exibe uma mensagem no terminal.
    # len(registros) = informa quantas vendas foram processadas.

    return registros
    # return registros = devolve os registros atualizados, agora com receita_total e faixa_preco. 


    ##  CALCULA A RECEITA POR CATEGORIA, REGIÃO E NO TOTAL GERAL.
def resumir_vendas(registros):
    

    receita_categoria = {}
    receita_regiao = {}
    receita_geral = 0
    # receita_categoria = {} = cria um dicionário para acumular a receita de cada categoria.
    # receita_regiao = {} = faz o mesmo para cada região.
    # receita_geral = 0 = inicia o acumulador total.

    for registro in registros:
        categoria = registro["categoria"]
        regiao = registro["regiao"]
        receita = registro["receita_total"]

        receita_categoria[categoria] = (
            receita_categoria.get(categoria, 0) + receita
        )
    # .get(categoria, 0) = recupera a receita acumulada; se a categoria ainda 
    # não existir, começa em zero.    

        receita_regiao[regiao] = (
            receita_regiao.get(regiao, 0) + receita
        )

        receita_geral += receita
    # adiciona a receita da venda ao total.

    print("\n--- RESUMO DE VENDAS ---")

    print("\nReceita por categoria:")
    for categoria, receita in receita_categoria.items():
        print(f"{categoria}: R$ {receita:.2f}")

    print("\nReceita por região:")
    for regiao, receita in receita_regiao.items():
        print(f"{regiao}: R$ {receita:.2f}")

    print(f"\nReceita geral: R$ {receita_geral:.2f}")

    # :.2f apresenta o número com duas casas decimais.

    return receita_categoria, receita_regiao, receita_geral



    ## CLASSIFICAR CLIENTES CONFORME O GASTO ACUMULADO.
def segmentar_clientes(registros):
    

    gastos_clientes = {}

    for registro in registros:
        id_cliente = registro["id_cliente"]
        receita = registro["receita_total"]

        gastos_clientes[id_cliente] = (
            gastos_clientes.get(id_cliente, 0) + receita
        )
    # Se o cliente já tiver realizado outras compras, a receita
    # da nova venda será somada ao valor anterior. Se for a primeira
    # compra dele, o acumulador começa em zero.

    segmentos = {}

    for id_cliente, gasto in gastos_clientes.items():
        if gasto < 3000:
            segmento = "Bronze"
        elif gasto <= 8000:
            segmento = "Prata"
        else:
            segmento = "Ouro"

        segmentos[id_cliente] = {
            "gasto_acumulado": round(gasto, 2),
            "segmento": segmento
        }
    # Classificação dos clientes por gasto acumulado, usa receita_total
    # de cada venda, e não apenas o preço unitário.

    print("\n--- SEGMENTAÇÃO DE CLIENTES ---")

    for id_cliente, dados in segmentos.items():
        print(
            f"Cliente {id_cliente}: "
            f"R$ {dados['gasto_acumulado']:.2f} - "
            f"{dados['segmento']}"
        )

    return segmentos


    ## EXPORTAR OS RESUMOS DE RECEITA PARA UM ARQUIVO CSV.
def exportar_metricas_csv(
        receita_categoria,
        receita_regiao,
        receita_geral,
        caminho="outputs/metricas_resumo.csv"
):
    # A função recebe os resultados calculados anteriormente e o caminho
    # onde salvará o arquivo.
    
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    # Path(caminho) = representa o caminho do arquivo.
    # .parent = obtém a pasta que contém o arquivo, neste caso outputs.
    # mkdir(...) = cria essa pasta, se necessário.
    # exist_ok=True = evita erro caso a pasta já exista.

    with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["tipo", "nome", "receita"])
    # Define as três colunas, escrever o cabeçalho.

        for categoria, receita in receita_categoria.items():
            escritor.writerow(["categoria", categoria, round(receita, 2)])

        for regiao, receita in receita_regiao.items():
            escritor.writerow(["regiao", regiao, round(receita, 2)])

        escritor.writerow(["geral", "Total", round(receita_geral, 2)])
    # Os laços "for" percorrem os dicionários de categorias e regiões. Depois,
    # a última linha registra a receita geral.

    print(f"\nArquivo CSV exportado: {caminho}")


    ## EXPORTAR AS ESTATÍSTICAS DE VENDAS PARA UM ARQUIVO JSON.
def exportar_estatisticas_json(
    receita_categoria,
    receita_regiao,
    receita_geral,
    segmentos,
    caminho="outputs/estatisticas.json"
):

    import json
    # Importa a biblioteca padrão que permite trabalhar com JSON.

    Path(caminho).parent.mkdir(parents=True, exist_ok=True)

    estatisticas = {
        "receita_por_categoria": {
            categoria: round(receita, 2)
            for categoria, receita in receita_categoria.items()
        },
        "receita_por_regiao": {
            regiao: round(receita, 2)
            for regiao, receita in receita_regiao.items()
        },
        "receita_geral": round(receita_geral, 2),
        "quantidade_clientes": len(segmentos),
        "segmentos_clientes": segmentos
    }
    # estatisticas = {...} = organiza os resultados em um dicionário.
    # len(segmentos) = conta quantos clientes foram segmentados.
    # categoria: round(receita, 2) = arredonda os valores para duas casas decimais.
    # for categoria, receita in receita_categoria.items()= percorre cada par de
    # categoria e receita do dicionário original.

    with open(caminho, mode="w", encoding="utf-8") as arquivo:
        json.dump(
            estatisticas,
            arquivo,
            ensure_ascii=False,
            indent=4
        )
    # json.dump(...) = grava os dados no arquivo.
    # ensure_ascii=False = preserva caracteres como Eletrônicos.
    # indent=4 = deixa o arquivo organizado e fácil de ler.

    print(f"Arquivo JSON exportado: {caminho}")
