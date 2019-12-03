def setup ():
    size (500, 500)
    background (0)
def draw ():
    colorMode(HSB , width , height , 100)
    stepX = mouseX +2
    stepY = mouseY +2
    for gridY in range(height):
        for gridX in range (width):
            stroke(gridX , height -gridY , 100)
            strokeWeight(stepX)
            line(gridX , gridY , stepX+gridX , stepY+gridY
