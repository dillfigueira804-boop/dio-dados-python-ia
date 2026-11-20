import math

# 1. DADOS DE TREINO (Histórico real: [distancia_km, peso_kg, status])
historico = [
    [15, 2, "No Prazo"],     # Perto e leve -> No Prazo
    [25, 5, "No Prazo"],     # Perto e leve -> No Prazo
    [120, 40, "Atrasado"],   # Longe e pesado -> Atrasado
    [350, 80, "Atrasado"],   # Muito longe e pesado -> Atrasado
    [40, 10, "No Prazo"],    # Perto e leve -> No Prazo
    [200, 65, "Atrasado"]    # Longe e pesado -> Atrasado
]

# 2. FUNÇÃO DE IA: Calcula a "distância" matemática entre a nova entrega e o histórico
def prever_entrega(nova_distancia, novo_peso):
    menor_distancia_matematica = float("inf")
    previsao = ""
    
    for dist_hist, peso_hist, status_hist in historico:
        # Fórmula da Distância Euclidiana (base de muitos algoritmos de IA)
        diferenca = math.sqrt((nova_distancia - dist_hist)**2 + (novo_peso - peso_hist)**2)
        
        # A IA encontra o caso do passado mais parecido com o pedido atual
        if diferenca < menor_distancia_matematica:
            menor_distancia_matematica = diferenca
            previsao = status_hist
            
    return previsao

# 3. TESTANDO A IA COM NOVOS PEDIDOS
pedido_1 = [20, 4]    # 20 km, 4 kg
pedido_2 = [180, 55]  # 180 km, 55 kg

print("--- PREVISÕES DA IA ---")
print(f"Pedido 1 (20km, 4kg)   -> Previsão: {prever_entrega(pedido_1[0], pedido_1[1])}")
print(f"Pedido 2 (180km, 55kg) -> Previsão: {prever_entrega(pedido_2[0], pedido_2[1])}")
