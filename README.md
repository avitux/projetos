
# Projeto de Cognitive Environments

A QuantumFinance tem um canal de atendimento via chat e precisa classificar os assuntos dos atendimentos para melhorar as tratativas dos chamados dos clientes. O canal recebe textos abertos dos clientes relatando o problema e/ou dúvida e depois é direcionado para algum uma área especialista no assunto para uma melhor tratativa. 

Crie um modelo classificador de assuntos aplicando técnicas de NLP, que consiga classificar através de um texto o assunto conforme disponível na base de dados para treinamento e validação do modelo seu modelo.

O modelo precisar atingir um score na métrica F1 Score superior a 75%. Utilize o dataset para treinar e testar o modelo, separe o dataset em duas amostras (75% para treinamento e 25% para teste). Utilize somente plataformas de machine learning baseado em cloud para desenvolver sua solução.

## Índice

- [Visão Geral](#visão-geral)
- [Pastas](#pastas)

## Visão Geral

Utilizamos o S3 para armazenar os dados (localizados na pasta "dados") e o Amazon Comprehend para treinar um modelo de classificação NLP, obtendo um F1 Score de 89%. Em seguida, criamos uma função Lambda e um endpoint na AWS para possibilitar a conexão via API, utilizando o StreamLit para a realização de testes.


## Pastas

### Dados

Contém os dataframes de treino e teste:
- Treino: tickets_reclamacoes_classificados_treino.csv
- Teste: Com a categoria (tickets_reclamacoes_classificados_teste.csv) e sem categoria (tickets_reclamacoes_classificados_teste2.csv).

### Notebook

Contém o arquivo TratamentoDadosCategoriaReclamacao.ipynb que trata os dados e exporta para .csv para o treinamento do modelo.

### Resultado

Contém a imagem do F1 Score do modelo e o output do dataframe de teste.

### AWS

Contém o arquivo Lambda_Function.py que recebe uma chamada HTTP (POST) e retorna um JSON com o resultado da análise do modelo.

### StreamLit

Contém o arquivo Classificar_Texto.py que cria o site utilizando o StreamLit.

