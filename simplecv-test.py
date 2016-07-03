#!/usr/bin/env python

from SimpleCV import Color,Display,Image

display = Display() 

while(display.isNotDone()):
 
    img = Image('example.jpg')
    barcode = img.findBarcode() #finds barcode data from image

    if(barcode is not None): #if there is some data processed
        barcode = barcode[0] 
        result = str(barcode.data)
        print result #prints result of barcode in python shell
        barcode = [] #reset barcode data to empty set

    img.save(display) #shows the image on the screen
