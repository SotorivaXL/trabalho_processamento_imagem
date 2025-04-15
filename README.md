README
Este projeto demonstra diversas operações de processamento de imagens usando a biblioteca OpenCV em Python. As operações incluem conversão para escala de cinza, equalização de histograma, aumento de saturação em HSV, ajuste de brilho e contraste, redimensionamentos, transformações geométricas (rotação, espelhamento, recorte) e binarização (limiarização pelo método Otsu).

Pré-requisitos
Python 3 instalado.

Biblioteca OpenCV (opencv-python) instalada.

Biblioteca NumPy instalada.

Você pode instalar as dependências executando:

bash
Copiar
Editar
pip install opencv-python numpy
Estrutura de Pastas
graphql
Copiar
Editar
.

├── input

│   └── imagem_exame.png      # Exemplo de imagem de entrada

├── resultados               # Onde as imagens resultantes serão salvas

│   ├── cinza.png

│   ├── equalizada.png

│   ├── converter_hsv_saturacao.png

│   ├── ajustar_contraste_brilho.png

│   ├── metade_tamanho.png

│   ├── 200%_tamanho.png

│   ├── girada.png

│   ├── espelhada.png

│   ├── recortada.png

│   └── binarizacao.png
└── processamento_imagens.py
Observação: As imagens processadas serão salvas automaticamente na pasta resultados. Certifique-se de criar essa pasta antes de rodar o script ou verifique se ela já existe.

Instruções para Rodar
Coloque a imagem que deseja processar na pasta input.

Abra um terminal ou prompt de comando na pasta raiz do projeto.

Execute o script principal:

bash
Copiar
Editar
python processamento_imagens.py
A imagem original será exibida em uma janela. Pressione qualquer tecla para fechar a janela e prosseguir com o restante do fluxo de processamento.

Ao final, verifique a pasta resultados/ para ver as imagens resultantes de cada etapa de processamento.
