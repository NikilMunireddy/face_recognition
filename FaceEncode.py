import face_recognition
import cv2

known_face_encodings=[]
def initialize():
    file=open('filenames.txt','r')
    i=0
    listn=[]
    for listnames in file:
        listn.append(listnames)
        i=i+1
        print('Encoding',i,":",listnames.strip('\n'))

    for filename in listn:
        filepath='knownfaces/'+filename.strip('\n')
        image = face_recognition.load_image_file(filepath)
        image_encoding= face_recognition.face_encodings(image)[0]
        known_face_encodings.append(image_encoding)
    file.close()

def get_encodings():
    return known_face_encodings

def get_face_names():
    known_face_names=[]
    file=open('filenames.txt','r')
    for facenames in file:
        known_face_names.append(facenames.split('.')[0])
    file.close()
    return known_face_names
    
 #just an practice
 
