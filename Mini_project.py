# Nome: Wesley Grignani

# Biblioteca OpenCV
import cv2

# Função de sketch
def sketch(imagem):
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


# Webcam é inicializada pelo VideoCapture
# Contem uma variável booleana para indicar se foi possivel realizar a captura (ret)
# Variável (frame) contem imagem capturada
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13:  # 13 é a tecla Enter
        break

# Desliga webcam e fecha as janelas
cap.release()
cv2.destroyAllWindows()