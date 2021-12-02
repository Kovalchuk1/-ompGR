from PIL import Image, ImageColor
from PIL import ImageDraw
from math import *
import numpy as np

ANGLE = radians(-10)
NewImage = Image.new("RGB", (960, 960))
PaintingImage = ImageDraw.Draw(NewImage)
Data = np.loadtxt("DS9.txt", delimiter=' ', skiprows=0, dtype=str)
for i in Data:
    p = lambda x: int(x.item()) - 480
    a = [p(i[0]), p(i[1])]
    AffineA = [a[0] * cos(ANGLE) - a[1] * sin(ANGLE) + 480,
               a[0] * sin(ANGLE) + a[1] * cos(ANGLE) + 480]
    PaintingImage.point((int(AffineA[0]), int(AffineA[1])), "white")
NewImage.save("AthenianTransformation.png", "PNG")
