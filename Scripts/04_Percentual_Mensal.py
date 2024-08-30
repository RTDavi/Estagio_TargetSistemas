"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP = R$67.836,43
• RJ = R$36.678,66
• MG = R$29.229,88
• ES = R$27.165,48
• Outros = R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que 
cada estado teve dentro do valor total mensal da distribuidora.
"""

dados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53,
}


valor_total = 0
for estado, valor_estado in dados.items():
    valor_total += valor_estado

for estado, valor_estado in dados.items():

    porcentagem_estado = (valor_estado / valor_total) * 100
    dados[estado] = porcentagem_estado
    print(f"A PORCENTAGEM DO ESTADO {estado} FOI DE: {porcentagem_estado:.2f}%")
