
# Projeto de Cognitive Environments

A QuantumFinance tem um canal de atendimento via chat e precisa classificar os assuntos dos atendimentos para melhorar as tratativas dos chamados dos clientes. O canal recebe textos abertos dos clientes relatando o problema e/ou dúvida e depois é direcionado para algum uma área especialista no assunto para uma melhor tratativa. 

Crie um modelo classificador de assuntos aplicando técnicas de NLP, que consiga classificar através de um texto o assunto conforme disponível na base de dados para treinamento e validação do modelo seu modelo.

O modelo precisar atingir um score na métrica F1 Score superior a 75%. Utilize o dataset para treinar e testar o modelo, separe o dataset em duas amostras (75% para treinamento e 25% para teste). Utilize somente plataformas de machine learning baseado em cloud para desenvolver sua solução.

## Índice

- [Visão Geral](#visão-geral)

## Visão Geral

Utilizamos o S3 para armazenar os dados (que estão na pasta dados) e Amazon Comprehend para treinar um modelo de classificação NLP obtivemos um f1-Score de XX.XX%
A pasta notebook possui o arquivo TratamentoDadosCategoriaReclamacao que trata os dados e faz a exportação para .csv para treinamento do modelo.
