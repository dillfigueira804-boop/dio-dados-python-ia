import csv

faturamento_por_cidade = {}

with open("entregas.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        cidade = linha["cidade"]
        valor = float(linha["valor_frete"])
        
        if cidade not in faturamento_por_cidade:
            faturamento_por_cidade[cidade] = 0.0
            
        faturamento_por_cidade[cidade] += valor

print("--- FATURAMENTO POR CIDADE (GRÁFICO) ---\n")

for cidade, total in faturamento_por_cidade.items():
    tamanho_barra = int(total / 20)
    barra = "█" * tamanho_barra
    print(f"{cidade:<12} | {barra} R$ {total:.2f}")
