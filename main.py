import cv2
import numpy as np

class ImageData:
    def __init__(
        self,
        original=None,
        gray=None,
        equalized=None,
        saturated=None,
        brightness_contrast=None,
        resized_half=None,
        resized_double=None,
        rotated=None,
        flipped=None,
        cropped=None,
        binarized=None
    ):
        self.original = original
        self.gray = gray
        self.equalized = equalized
        self.saturated = saturated
        self.brightness_contrast = brightness_contrast
        self.resized_half = resized_half
        self.resized_double = resized_double
        self.rotated = rotated
        self.flipped = flipped
        self.cropped = cropped
        self.binarized = binarized

def salvar_imagem(caminho, imagem):
    cv2.imwrite(caminho, imagem)

def carregar_imagem(caminho: str):
    imagem = cv2.imread(caminho)
    if imagem is None:
        raise FileNotFoundError(f"Imagem não encontrada em: {caminho}")
    return imagem

def mostrar_imagem(titulo: str, imagem):
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def converter_cinza(imagem):
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    salvar_imagem("resultados/cinza.png", cinza)
    return cinza

def equalizacao(imagem_cinza):
    equalizada = cv2.equalizeHist(imagem_cinza)
    salvar_imagem("resultados/equalizada.png", equalizada)
    return equalizada

def converter_hsv_saturacao(imagem, fator=1.3):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * fator, 0, 255)
    saturada = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    salvar_imagem("resultados/converter_hsv_saturacao.png", saturada)
    return saturada

def ajustar_contraste_brilho(imagem, brilho=50, contraste=1.2):
    ajustada = cv2.convertScaleAbs(imagem, alpha=contraste, beta=brilho)
    salvar_imagem("resultados/ajustar_contraste_brilho.png", ajustada)
    return ajustada

def metade_tamanho(imagem):
    redimensionada = cv2.resize(imagem, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    salvar_imagem("resultados/metade_tamanho.png", redimensionada)
    return redimensionada

def redimensionar_maior(imagem):
    redimensionada = cv2.resize(imagem, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    salvar_imagem("resultados/200%_tamanho.png", redimensionada)
    return redimensionada

def girar_imagem(imagem, angulo=45):
    (h, w) = imagem.shape[:2]
    centro = (w // 2, h // 2)
    matriz = cv2.getRotationMatrix2D(centro, angulo, 1.0)
    girada = cv2.warpAffine(imagem, matriz, (w, h))
    salvar_imagem("resultados/girada.png", girada)
    return girada

def espelhada(imagem):
    espelho = cv2.flip(imagem, 1)
    salvar_imagem("resultados/espelhada.png", espelho)
    return espelho

def recortar(imagem, largura=300, altura=300):
    h, w = imagem.shape[:2]
    inicio_x = w // 2 - largura // 2
    inicio_y = h // 2 - altura // 2
    recortada = imagem[inicio_y:inicio_y + altura, inicio_x:inicio_x + largura]
    salvar_imagem("resultados/recortada.png", recortada)
    return recortada

def binarizacao(imagem_cinza):
    _, binaria = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    salvar_imagem("resultados/binarizacao.png", binaria)
    return binaria

def main():
    # 1 - Leitura da imagem
    imagem = carregar_imagem("input/imagem_exame.png")
    mostrar_imagem("Imagem Original", imagem)

    data = ImageData(original=imagem)

    # 2 - Pré-processamento
    data.gray = converter_cinza(data.original)
    data.equalized = equalizacao(data.gray)

    # 3 - Modificação de Cores
    data.saturated = converter_hsv_saturacao(data.original)

    # 4 - Brilho e Contraste
    data.brightness_contrast = ajustar_contraste_brilho(data.original)

    # 5 - Redimensionamentos
    data.resized_half = metade_tamanho(data.original)
    data.resized_double = redimensionar_maior(data.original)

    # 6 - Transformações Geométricas
    data.rotated = girar_imagem(data.original)
    data.flipped = espelhada(data.original)
    data.cropped = recortar(data.original)

    # 7 - Binarização
    data.binarized = binarizacao(data.equalized)

    print("Processamento finalizado")

if __name__ == "__main__":
    main()
