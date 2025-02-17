import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

classifier_path = r'C:\Users\raul2\OneDrive\Escritorio\semestre-OCT24-MAR25\aplicaciones basadas\tercer parcial\reconocer objetos\reconocer objetos\cascade.xml'
grootClassif = cv2.CascadeClassifier(classifier_path)

# Verificar si el clasificador se cargó correctamente
if grootClassif.empty():
    print("Error: No se pudo cargar el clasificador.")
    exit()

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = grootClassif.detectMultiScale(gray,
    scaleFactor = 5,
    minNeighbors = 78,
    minSize=(80,50))

    for (x,y,w,h) in toy:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(frame,'Groot',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()