# Copyright 2024 Daniel Nicholson
# If using my code, please credit me

import cmath
import math
import time

from PIL import Image

# variables
width = 250
height = 250
domain = 3

# keeping track of how long the program took to run
startTime = time.time()

# the function that is being mapped
def f(posx,posy):
  z = complex(posx,posy)
  z = (2*z - 5) / (3*z - 2)
  return z.real,z.imag,abs(z)

# generating a blank image
image = Image.new("RGB", (width, height))

# iterating through every pixel of the image
for x in range(width):
  for y in range(height):

    # converts pixel coordinates to cartesian
    posx = 2*x*domain/width - domain
    posy = 2*(height-y)*domain/height - domain

    # runs the function on the pixel coordinates and saves the ouput
    posfx,posfy,mod = f(posx,posy)

    # converts the x,y of the output into a colour
    # (using precomputed values for sine and cosine)
    mod = 81.1875*mod*0.25
    red = min(int(abs(math.atan2(posfy*0.866-posfx*0.5,posfx*-0.866-posfy*0.5))*mod), 255)
    green = min(int(abs(math.atan2(posfy*-0.866-posfx*0.5,posfx*0.866-posfy*0.5))*mod), 255)
    blue = min(int(abs(math.atan2(posfx,posfy))*mod), 255)

    # fills in the pixel the colour of the output
    image.putpixel((x,y),(red,green,blue))

# displaying how long the program took to run
print("program finished in",str(round(time.time()-startTime,3))+"s")

#displaying final image
image.show()

