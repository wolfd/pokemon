#!/usr/local/bin/python3

# This work is licensed under the Creative Commons Attribution 3.0 United 
# States License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by/3.0/us/ or send a letter to Creative
# Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.

# from http://oranlooney.com/make-css-sprites-python-image-library/ 
# Orignial Author Oran Looney <olooney@gmail.com>

#mods by Josh Gourneau <josh@gourneau.com> to make one big horizontal sprite JPG with no spaces between images
import os
from PIL import Image
import glob
from collections import Counter
from pprint import pprint
import json

start_dir = "images/pokemonParts/body/"

iconmap = os.listdir(start_dir)

#print(len(iconmap))
master = Image.new(
    mode='RGBA',
    size=(50, 19), #50 px for color rows, 151 pokemon
    color=(0,0,0,0))  # fully transparent

newdata = []

listdata = []

pokenumber = 0
for filename in iconmap:
  pokenumber += 1
  listdata.append((pokenumber, [])) # add (2, []) to the list
  image = Image.open(start_dir+filename) 

  data = image.getdata()
  colors = Counter()

  for item in data:
    colors[item] += 1

  total=0

  for color, num in sorted(colors.items(), key=lambda x: x[1], reverse=True):
    newdata.append(color)

    if color[3] != 0:
      listdata[pokenumber-1][1].append(color)
    #pprint(color)
    total += 1

  #print(total)

  for i in range(50-total): #transparent pixels
    newdata.append((255,255,255,0))
    total += 1

  #print(total)

  #pprint(("pokenumber",pokenumber))

print(json.dumps(listdata, indent=4))
master.putdata(newdata)

#print( "saving master.jpg...")
master.save("colormap.png")
#print( "saved!")

