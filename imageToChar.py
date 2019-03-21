import cv2
import random
img = cv2.imread('pictures/quotes.jpg')
img = cv2.resize(img,(200,200)) #Resize the image se per the image requirements
width, height = img.shape[:2]
print(height,width)
array = []
for i in range(width):
	line = []
	for j in range(height):
		if(img[i,j][0] <230):
			line +=[[i,j]]
	if(len(line)!=0):
		array +=line

colors =["91","92","93","94","95","96"] #For printing characters in random colored


#40,width-40 have beed used to remove the extra space from the visual
for i in range(40,width-40):
	for j in range(height):
		if([i,j] in array):
			print("\33[5m"+"\33[90m"+"`"+"\33[0m",end="")
		else:
			print("\33["+random.choice(colors)+"m"+"*"+"\33[0m",end="")
	print("")