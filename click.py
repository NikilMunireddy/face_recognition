import cv2

camera = cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        picname=input('What is your name?')
        file=open('filenames.txt','a')
        file.write(picname+".jpg\n")
        file.close()
        cv2.imwrite('knownfaces/'+picname+'.jpg',image)
        break

camera.release()
cv2.destroyAllWindows()