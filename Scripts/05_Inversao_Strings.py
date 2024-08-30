"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

print("------BEM VINDO AO PROGRAMA DE INVERSÃO DE FRASES/PALAVRAS------")
string = str(input("DIGITE UMA PALAVRA: "))
caracteres = []

for letra in string:
    caracteres.insert(0, letra)
    string_invertida = "".join(caracteres)

print(string_invertida)
