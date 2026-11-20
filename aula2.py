import csv

total_frete = 0.0
qtd_atrasos = 0
valor_atrasos = 0.0

with open("entregas.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        valor = float(linha["valor_frete"])
        total_frete += valor
        
        if linha["status"] == "Atrasado":
            valor_atrasos += valor
            qtd_atrasos += 1
            print(f"⚠️ Alerta: Entrega {linha['id_entrega']} para {linha['cidade']} está atrasada!")

print("\n--- RESUMO LOGÍSTICO ---")
print(f"Faturamento total de fretes: R$ {total_frete:.2f}")
print(f"Total de entregas atrasadas: {qtd_atrasos}")
print(f"Valor retido em atrasos: R$ {valor_atrasos:.2f}")
