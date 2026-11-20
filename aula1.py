vendas_brutas = [
    {"cliente": "  ana silva ", "produto": "Notebook", "valor": "3500.50"},
    {"cliente": "CARLOS SOUZA", "produto": "Mouse", "valor": "85.00"},
    {"cliente": " mariana lima", "produto": "Teclado", "valor": "150.00"},
    {"cliente": "ana silva", "produto": "Monitor", "valor": "900.00"},
    {"cliente": "dill", "produto": "Fone", "valor": "250.00"}
]

vendas_limpas = []
faturamento_total = 0.0

for venda in vendas_brutas:
    nome_limpo = venda["cliente"].strip().title()
    valor_numerico = float(venda["valor"])
    
    vendas_limpas.append({
        "cliente": nome_limpo,
        "produto": venda["produto"],
        "valor": valor_numerico
    })
    
    faturamento_total += valor_numerico

print("--- RELATÓRIO DE VENDAS (ACIMA DE R$ 200) ---")
for item in vendas_limpas:
    if item["valor"] > 200:
        print(f"Cliente: {item['cliente']} | Produto: {item['produto']} | R$ {item['valor']:.2f}")

print(f"\nFaturamento Total Geral: R$ {faturamento_total:.2f}")
