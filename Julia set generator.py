# Copyright 2025 Daniel Nicholson
# If using my code, please credit me

import math
import cmath
import time

from PIL import Image

#variables
width = 2000
height = 2000
domain = 1.6
maxI = 1000
c = complex(-0.835, -0.2321)

#keeping track of how long the program took to run
startTime = time.perf_counter()

#iterates the function and returns how long it took to diverge
def f(z):
  for i in range(maxI):
    z = z*z + c
    mod = abs(z)
    if mod >= 2 or math.isnan(mod): break
  return i

#function to generate colour gradient
def interpolate(r1,g1,b1,r2,g2,b2,t):
  red = round((r2-r1)*t + r1)
  green = round((g2-g1)*t + g1)
  blue = round((b2-b1)*t + b1)
  return red,green,blue

#generating a blank image
image = Image.new("RGB", (width, height))

#iterating through every pixel of the image
for x in range(width):
  for y in range(height):

    #converts pixel coordinates to cartesian
    posx = 2*x*domain/width - domain
    posy = 2*(height-y)*domain/height - domain

    #runs the function on the pixel coordinates and sets the
    #colour of the pixel to the iterations until it diverges
    i = f(complex(posx,posy))
    if i == maxI-1:
      image.putpixel((x,y),(0,0,0))
    else:
      i = i/maxI
      if i <= 0.05:
        red,green,blue = interpolate(7,4,23,25,14,89,i/0.05)
      elif i <= 0.2:
        red,green,blue = interpolate(25,14,89,191,80,63,i/0.15)
      elif i <= 0.5:
        red,green,blue = interpolate(191,80,63,254,221,159,i/0.3)
      else:
        red,green,blue = interpolate(254,221,159,0,0,0,i/0.5)
      image.putpixel((x,y),(red,green,blue))

#displaying how long the program took to run
print(f"program finished in {(time.perf_counter()-startTime):.3f}s")

#displaying final image
image.show()

