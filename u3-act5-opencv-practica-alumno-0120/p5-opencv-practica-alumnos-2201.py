import cv2
# Ejemplo de código:
# Leer la imagen del archivo
image = cv2.imread( 'cornecarro.jpeg' ) 
# Mostrar la imagen en una ventana
cv2.imshow( 'Ejemplo de codigo Nicole Robles 0120' , image) 

# Conversión entre espacios de color
# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0) 
cv2.destroyAllWindows()
# Cargar la imagen
image = cv2.imread( 'cornecarro.jpeg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Guardar la imagen en escala de grises
cv2.imwrite( 'gray_image.jpg' , gray_image)

# Cambiar el tamaño de una imagen
# Cargar la imagen
image = cv2.imread( 'cornecarro.jpeg' ) 
# Redimensionar la imagen a 300x200
resized_image = cv2.resize(image, (300, 200)) 
# Guardar la imagen redimensionada
cv2.imwrite( 'resized_image.jpg' , resized_image)

# Rotar una imagen
# Cargar la imagen
image = cv2.imread('cornecarro.jpeg') 
# Obtener la altura y el ancho de la imagen
(h, w) = image.shape[:2] 
# Definir el centro de la imagen
center = (w // 2, h // 2) 
# Matriz de rotación
matrix = cv2.getRotationMatrix2D(center, 90, 1.0) 
# Realizar la rotación
rotated_image = cv2.warpAffine(image, matrix, (w, h)) 
# Guardar la imagen rotada
cv2.imwrite('rotated_image.jpg', rotated_image)

# Desenfoque de una imagen
# Cargar la imagen
image = cv2.imread( 'cornecarro.jpeg' ) 
# Aplicar desenfoque gaussiano
blured_image = cv2.GaussianBlur(image, (15, 15), 0) 
# Guardar la imagen desenfocada
cv2.imwrite( 'blurred_image.jpg' , blured_image)

# Detección de bordes mediante el algoritmo de Canny
# Cargar la imagen
image = cv2.imread( 'cornecarro.jpeg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100 , 200 ) 
# Guardar la imagen de bordes
cv2.imwrite( 'edges.jpg' , edges)

# Dibujar formas y añadir texto
# Cargar la imagen
image = cv2.imread( 'cornecarro.jpeg' ) 
# Dibujar un rectángulo
cv2.rectangle(image, ( 50 , 50 ), ( 200 , 200 ), ( 255 , 0 , 0 ), 3 ) 
# Agregar texto a la imagen
cv2.putText(image, 'OpenCV' , ( 60 , 40 ), cv2.FONT_HERSHEY_SIMPLEX, 1 , ( 0 , 255 , 0 ), 2 ) 
# Guardar la imagen de salida
cv2.imwrite( 'output_image.jpg' , image)

# Umbralización
# Cargar la imagen
image = cv2.imread( 'cornecarro.jpeg' , 0 ) 
# Aplicar umbralización
_, thresh_image = cv2.threshold(image, 127 , 255 , cv2.THRESH_BINARY) 
# Guardar la imagen umbralizada
cv2.imwrite( 'threshold_image.jpg' , thresh_image)

# Detección de contornos
# Cargar la imagen
image = cv2.imread('cornecarro.jpeg')
# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Encontrar bordes
edges = cv2.Canny(gray_image, 100, 200)
# Encontrar contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Dibujar contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# Guardar la imagen de salida con contornos
cv2.imwrite('contours_image.jpg', image)
print("-----Nicole Robles NC 0120----")