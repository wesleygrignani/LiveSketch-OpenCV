# Nome: Wesley Grignani

import cv2
import sketch

# Webcam é inicializada pelo VideoCapture
# Contem uma variável booleana para indicar se foi possivel realizar a captura (ret)
# Variável (frame) contem imagem capturada
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Live Sketcher', sketch.processar_imagem(frame))
    if cv2.waitKey(1) == 13:  # 13 é a tecla Enter
        break

# Desliga webcam e fecha as janelas
cap.release()
cv2.destroyAllWindows()