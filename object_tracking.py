import cv2
import time
import math

cestax = 530
cestay = 300
xao = []
yao = []

video = cv2.VideoCapture("bb3.mp4")

# Carregue o rastreador
tracker = cv2.TrackerCSRT_create()

# Leia o primeiro quadro do vídeo
returned, img = video.read()

# Selecione a caixa delimitadora na imagem
bbox = cv2.selectROI("Tracking", img, False)

# Inicialize o rastreador em img e na caixa delimitadora
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Rastreando",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

    xinho = x+ int(w/2)
    yinho = y+ int(h/2)
    cv2.circle(img, (xinho,yinho), 2,(0,0,255), 5)
    cv2.circle(img, (int(cestax),int(cestay)), 2,(180,105,255), 3)
    distence = math.sqrt(((xinho - cestax)**2)+((yinho - cestay)**2))
    print(distence)
    if(distence <= 20):
        cv2.putText(img,"o my god, three points!!",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    xao.append(xinho)
    yao.append(yinho)
    for i in range(len(xao) - 1):
         cv2.circle(img, (xao[i],yao[i]), 2,(0,0,255), 3)

while True:
    
    check, img = video.read()   

    # Atualize o rastreador em img e na caixa delimitadora
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Errou",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    goal_track(img, bbox)
    
    cv2.imshow("resultado", img)
            
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break

video.release()
cv2.destroyALLwindows()