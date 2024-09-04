"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json
import os

NOME_ARQUIVO = "dados.json"
LOCAL_ARQUIVO = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)
menor_faturamento = 0
maior_faturamento = 0
media_faturamento = 0
quantidade_dias = 0


with open(LOCAL_ARQUIVO, "r") as arquivo:
    dados = json.load(arquivo)

    for dado in dados:
        media_faturamento += dado["valor"]
        if dado["valor"] > 0:
            quantidade_dias += 1

    valores_no_mes = [dado["valor"] for dado in dados if dado["valor"] > 0]
    media_faturamento = media_faturamento / quantidade_dias

    dias_media_superior = [
        dado["dia"] for dado in dados if dado["valor"] > media_faturamento
    ]
    menor_faturamento = min(valores_no_mes)
    maior_faturamento = max(valores_no_mes)

print(f"O MAIOR FATURAMENTO DO MÊS FOI DE: {maior_faturamento}")
print(f"O MENOR FATURAMENTO DO MÊS FOI DE: {menor_faturamento}")
print(f"O FATURAMENTO MENSAL FOI DE: {media_faturamento}")
print(f"OS DIAS EM QUE O FATURAMENTO FOI ACIMA DA MÉDIA MENSAL: {dias_media_superior}")
