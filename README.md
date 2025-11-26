1. Instalação

Para executar o projeto, é necessário ter Python 3.8+ instalado.

Instale as dependências:

pip install numpy matplotlib


Clone ou baixe o repositório e mantenha estes arquivos juntos na mesma pasta:

config.py
model.py
main.py

2. Como usar
Executar a simulação

Basta rodar o arquivo:

python main.py


Isso irá:

Rodar a simulação SEIR em autômatos celulares 2D

Gerar os gráficos das curvas S, E, I e R

Salvar automaticamente os gráficos em /plots/

Exibir o resultado final da grade (heatmap opcional, se você habilitar depois)

Saída padrão gerada:

📁 plots/

curvas_seir.png — gráfico temporal S/E/I/R

heatmap_final.png — estado final da grade (opcional)

evolucao_infectados.png — evolução isolada do número de infectados

Você pode usar essas imagens diretamente no seu artigo ou GitHub.

3. Requisitos

Python 3.8+

Bibliotecas Python:

NumPy

Matplotlib

Instale com:

pip install numpy matplotlib