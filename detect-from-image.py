#!/usr/bin/env python

import time
import sys
import cv2
import zbar
import Image

output = cv2.imread("./example.jpg")

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

# raw detection code
gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY, dstCn=0)
pil = Image.fromarray(gray)
width, height = pil.size
raw = pil.tostring()

# create a reader
image = zbar.Image(width, height, 'Y800', raw)
scanner.scan(image)

print image

# extract results
for symbol in image:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# show the frame
cv2.imshow("Barcode Detection", output)

# Wait for the magic key
keypress = cv2.waitKey(0)
if keypress == ord('q'):
    quit()

cv2.destroyAllWindows()
