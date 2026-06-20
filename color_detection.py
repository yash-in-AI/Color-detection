import argparse
import csv
from pathlib import Path

import cv2
import numpy as np
import pandas as pd

#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

csv_path = Path(__file__).with_name('colors.csv')

#Reading the image with opencv
img = cv2.imread(img_path)
if img is None:
    raise SystemExit(f"Could not read image: {img_path}")

#declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
if csv_path.exists() and csv_path.stat().st_size > 0:
    color_df = pd.read_csv(csv_path, names=index, header=None)
else:
    color_df = pd.DataFrame(columns=index)

#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):
    if color_df.empty:
        return "Unknown"
    minimum = 10000
    for i in range(len(color_df)):
        d = abs(R- int(color_df.loc[i,"R"])) + abs(G- int(color_df.loc[i,"G"]))+ abs(B- int(color_df.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = color_df.loc[i,"color_name"]
    return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):
    global b,g,r,xpos,ypos, clicked
    if event in (cv2.EVENT_LBUTTONDOWN, cv2.EVENT_LBUTTONDBLCLK):
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

        color_name = getColorName(r,g,b)
        hex_value = f"#{r:02X}{g:02X}{b:02X}"
        row = [color_name, color_name, hex_value, r, g, b]

        with csv_path.open('a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):

    cv2.imshow("image",img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
