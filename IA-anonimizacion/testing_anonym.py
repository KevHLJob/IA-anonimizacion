import cv2


# variable que obtiene datos entrenados de opencv
cl='haarcascade_frontalface_default.xml'

# imagen de prueba
image_test= 'portugal.jpg'
# lectura de la imagen
image = cv2.imread(image_test)
# conversion a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
# carga del clasificador obtenido de OpenCV
face_cascade = cv2.CascadeClassifier(cl)

# deteccion de rostros
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    face=image[y:y+h, x:x+w]
    blur_face = cv2.resize(cv2.resize(face, (w//10, h//10)), (w, h))
    image[y:y+h, x:x+w] = blur_face

    cv2.imshow('Faces Detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()