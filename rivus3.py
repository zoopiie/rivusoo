import os
import random
from tkinter import *

g = ['https://ykob.github.io/sketch-threejs/sketch/glitch.html', 'https://dataf.org/en/', 'https://deathofmygeneration.fun/','https://64yogini.in/', 'https://www.heavensgate.com/','http://planecrashinfo.com/lastwords.htm','http://fondationscp.wikidot.com/scp-1078']

t = random.randint(0,6)

h = g[t]

sd = "%s%s" % ('start \"\" ', h)

os.system(sd)

