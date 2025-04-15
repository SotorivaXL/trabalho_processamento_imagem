Este projeto foi desenvolvido como parte de um desafio acadêmico para um laboratório de análise de imagens médicas. O objetivo principal foi criar um pipeline de tratamento e manipulação de imagens utilizando a biblioteca OpenCV, seguindo boas práticas de organização, como o padrão SOLID.

Objetivo Desenvolver um sistema em Python que realize uma sequência de transformações em imagens de exames, melhorando sua qualidade e facilitando a análise posterior por especialistas.

Estrutura do Projeto processamento_imagem/ ├── input/ # Imagem de entrada

├── resultados/ # Saída das transformações

├── model/ # Definição da estrutura de imagem

├── services/ # Lógica das transformações em módulos

├── utils/ # Funções auxiliares

├── main.py # Pipeline principal

├── requirements.txt # Dependências do projeto

└── README.md # Este relatório

Tecnologias utilizadas

Python 3.13+

OpenCV

NumPy

Execução

Instale os requisitos: pip install -r requirementos.txt

Execute o programa: python main.py

As imagens transformadas serão salvas automaticamente na pasta resultados/.

Etapas do Pipeline e Explicações

Leitura e Exibição Inicial

A imagem é lida da pasta input/ e exibida em tela com OpenCV.

Isso garante que o arquivo está correto e pronto para o processamento.

Pré-processamento

Conversão para Escala de Cinza: remove as cores, mantendo só a intensidade da luz. Ideal para reduzir a complexidade da análise.

Equalização de Histograma: aumenta o contraste, evidenciando regiões escuras ou apagadas da imagem.

Modificação de Cores

A imagem é convertida para o espaço de cores HSV.

O canal de saturação (S) é aumentado em 30%, tornando as cores mais intensas e melhorando a distinção visual entre regiões.

Ajuste de Brilho e Contraste

O brilho da imagem é aumentado em 50 unidades.

O contraste é ajustado com uma transformação linear (alpha=1.2).

Isso melhora a visualização de detalhes em regiões escuras ou com pouca diferenciação.

Redimensionamento e Interpolação

A imagem é reduzida para 50% usando interpolação bicúbica, que suaviza os pixels.

Depois, é aumentada para 200% usando interpolação linear, que é mais rápida, mas com qualidade inferior.

Essas etapas testam diferentes técnicas de reescala, úteis para exibição em sistemas com resoluções variadas.

Transformações Geométricas

Rotação de 45°: permite observar estruturas em diferentes ângulos.

Espelhamento horizontal: simula perspectiva inversa, usada para treinamentos de IA ou simulações.

Recorte Central (300x300): extrai uma área de interesse no centro da imagem, facilitando análises localizadas.

Binarização com Otsu

A imagem equalizada é convertida para preto e branco automaticamente, com base no método de Otsu.

Essa técnica é muito útil para segmentar estruturas e detectar contornos automaticamente.

Conclusão Esse projeto demonstrou, na prática, como aplicar um pipeline completo de processamento de imagens, utilizando OpenCV de forma modularizada e reaproveitável. A organização em camadas (services, model, utils) permite fácil manutenção e futura expansão.

O projeto está pronto para ser adaptado para outros tipos de exames médicos e pode servir como base para aplicações mais complexas como reconhecimento de padrões, uso de inteligência artificial ou automação de análises.
