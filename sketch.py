import cv2

# Funcao responsavel por receber a imagem da webcam
# e retornar a imagem somente com as bordas

def processar_imagem(imagem):
    # Convertendo a imagem em escala de cinza
    img_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicando Guassian Blur na imagem
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extraindo as bordas pelo método de Canny
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    # Invertendo a imagem binarizada
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    # retorna a imagem processada
    return mask
