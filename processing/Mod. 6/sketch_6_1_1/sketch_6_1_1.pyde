def setup():
    size(300,300)
    smooth()
    strokeWeight(3)
    background(0)

i = 0
k = 1

def draw():
    global i, k
    stroke(i,20)
    line(random(0,500),0,mouseX, mouseY)
    i +=k
    if i == 255:
        k=-1
    if i == 0:
        k=1

def keyPressed():
    if key == "s":
        saveFrame("meProcessing.png")
