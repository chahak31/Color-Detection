import pandas as pd
import cv2

img_path = 'pic2.jpg'
csv_path = 'colors.csv'

#Create headers
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
#create a dataframe & read a csv file
df = pd.read_csv(csv_path, names=index, header=None)

"""
#Prints first 5 rows
print(df.head(5))

#prints total number of rows
print(len(df))
#prints a particular row(here row=1)
print(df.loc[1])
#prints a particular column from a row
print(df.loc[1,'R'])
"""

#Read an image 
img = cv2.imread(img_path)
#prints image as array of pixels
#print(img)
img = cv2.resize(img, (800,600))

clicked = False
r = g = b = xpos = ypos = 0

def get_color_name(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i,'color_name']
    return cname

#print(get_color_name(0,0,0))

def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #co-ordinates of a particular point in that image
        print(x,y)
        global clicked, r, g, b, xpos, ypos
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y,x]
        print(b,g,r)
        #converting uint into int
        b = int(b)
        r = int(r)
        g = int(g)

#create a window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow('image',img)
    if clicked:
        cv2.rectangle(img,(20,20),(600,60),(b,g,r),-1)
        text = get_color_name(r,g,b) + 'R='+str(r)+'G='+str(g)+'B='+str(b)
        cv2.putText(img, text, (50,50), 2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b>=600:
            cv2.putText(img, text, (50,50), 2,0.8,(0,0,0),2,cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
