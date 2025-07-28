import cmath
import math
import time

from PIL import Image

#variables
width = 250
height = 250
domain = 10

#keeping track of how long the program took to run
startTime = time.time()

#the function that is being mapped
def f(posx,posy):
  z = complex(posx,posy)
  z = z*z*z - 10
  return z.real,z.imag,abs(z)

#generating a blank image
image = Image.new("RGB", (width, height))

#iterating through every pixel of the image
for x in range(width):
  for y in range(height):

    #converts pixel coordinates to cartesian
    posx = 2*x*domain/width - domain
    posy = 2*(height-y)*domain/height - domain

    #runs the function on the pixel coordinates and saves the ouput
    posfx,posfy,mod = f(posx,posy)

    #converts the x,y of the output into a colour
    #(using precomputed values for sine and cosine)
    mod = 81.1875*min(mod*0.25,1)
    red = int(abs(math.atan2(posfy*0.866-posfx*0.5,posfx*-0.866-posfy*0.5))*mod)
    green = int(abs(math.atan2(posfy*-0.866-posfx*0.5,posfx*0.866-posfy*0.5))*mod)
    blue = int(abs(math.atan2(posfx,posfy))*mod)

    #fills in the pixel the colour of the output
    image.putpixel((x,y),(red,green,blue))

#displaying how long the program took to run
print("program finished in",str(round(time.time()-startTime,3))+"s")

#displaying final image
image.show()
