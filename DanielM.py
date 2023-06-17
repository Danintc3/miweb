#!/usr/bin/env python
# coding: utf-8

# In[54]:


import cv2

vid = cv2.VideoCapture(1)
_,img = vid.read()

cv2.imshow("foto", img)
cv2.waitKey()
cv2.destroyAllWindows()

vid.release()


# In[43]:


#Guardar Imagen
cv2.imwrite("mifoto.png", img)

img2 = cv2.imread("mifoto.png")

cv2.imshow("foto", img2)
cv2.waitKey()
cv2.destroyAllWindows()

vid.release()


# In[103]:


import cv2
vid = cv2.VideoCapture(1)
salida = cv2.VideoWriter('Desktop/videoSalida.mp4',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while (vid.isOpened()):
  ret, imagen = vid.read()
  if ret == True:
    cv2.imshow('video', imagen)
    salida.write(imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
vid.release()
salida.release()
cv2.destroyAllWindows()


# In[ ]:




