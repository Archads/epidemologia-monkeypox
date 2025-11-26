import matplotlib.pyplot as plt
import numpy as np
from model import SEIRModel
from config import S, E, I, R, STEPS


# Função auxiliar para salvar cada frame do grid
def save_grid_frame(grid, step):
    plt.figure(figsize=(6, 6))
    cmap = plt.cm.get_cmap("viridis", 4)
    plt.imshow(grid, cmap=cmap, vmin=0, vmax=3)
    plt.title(f"Estado da grade – passo {step}")
    plt.colorbar(ticks=[0,1,2,3], label="Estado")
    plt.savefig(f"evolucao_infeccao_frame_{step}.png", dpi=300)
    plt.close()

model = SEIRModel()
history, final_grid = model.run()

plt.figure(figsize=(8,5))
plt.plot(history["S"], label="Suscetíveis")
plt.plot(history["E"], label="Expostos")
plt.plot(history["I"], label="Infectados")
plt.plot(history["R"], label="Recuperados")

plt.xlabel("Passos da simulação")
plt.ylabel("Número de indivíduos")
plt.title("Curvas SEIR da Monkeypox")
plt.legend()
plt.grid(True)
plt.savefig("curvas_SEIR.png", dpi=300)
plt.close()


#  Heatmap do estado final

plt.figure(figsize=(6,6))
plt.imshow(final_grid, cmap="viridis", vmin=0, vmax=3)
plt.title("Heatmap final do autômato")
plt.colorbar(ticks=[0,1,2,3], label="Estado")
plt.savefig("heatmap_final.png", dpi=300)
plt.close()


# 3) Mapa de clusters sociais
plt.figure(figsize=(6,6))
plt.imshow(model.cluster_map, cmap="coolwarm")
plt.title("Mapa de clusters sociais")
plt.colorbar(label="Cluster (1 = sim)")
plt.savefig("clustermap.png", dpi=300)
plt.close()


# 4) Frames espaçados da evolução da epidemia
frame_steps = np.linspace(0, STEPS-1, 10, dtype=int)

# precisamos simular novamente só para capturar os frames
model2 = SEIRModel()
for step in range(STEPS):
    if step in frame_steps:
        save_grid_frame(model2.grid, step)
    model2.step()

print("Simulação finalizada! Gráficos salvos no diretório atual.")