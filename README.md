# Simulação Espacial da Transmissão da Monkeypox com SEIR em Autômatos Celulares

Este projeto implementa um modelo SEIR usando Autômato Celular 2D para simular a transmissão espacial da Monkeypox.
A população é distribuída em uma grade, com clusters sociais que aumentam a transmissibilidade em regiões específicas.

O objetivo é permitir experimentos epidemiológicos simples, visualização de curvas S–E–I–R e análise da influência de aglomerações na propagação da doença.

## 🛠️ 1. Instalação

Clone o repositório e entre no diretório:

git clone https://github.com/SEU_USUARIO/monkeypox-AC-SEIR.git
cd monkeypox-AC-SEIR


Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows


Instale as dependências:

pip install -r requirements.txt


Arquivo requirements.txt recomendado:

numpy
matplotlib

## ▶️ 2. Como usar

Execute a simulação com:

python main.py


Isso irá:

✔ Rodar o modelo SEIR em uma grade 2D

✔ Gerar curvas S, E, I e R

✔ Salvar automaticamente os gráficos em /output/

Estrutura esperada:

├── main.py

├── model.py

├── config.py

├── output/
│   ├── curva_SEIR.png
│   ├── heatmap_final.png

├── README.md

## 📌 3. Requisitos

Python 3.8+

NumPy

Matplotlib

Esses pacotes são usados para:

Representar a grade da população

Processar a evolução temporal do autômato

Gerar e salvar gráficos automaticamente

## 📊 Exemplos de saídas
🔹 Curva SEIR

Mostra a evolução temporal dos estados Suscetível, Exposto, Infectado e Recuperado.

🔹 Heatmap da grade final

Visualiza a epidemia no espaço ao final da simulação.

