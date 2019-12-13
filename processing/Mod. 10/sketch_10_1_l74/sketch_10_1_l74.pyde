def setup():
    global img1, img2, img0, img3
    smooth()
    size(1800,1200)
    img0 = loadImage("data/000.jpeg")
    img1 = loadImage("data/001.png")
    img2 = loadImage("data/002.png")
    img3 = loadImage("data/003.png")
    
    
def draw():
    background(100)
    image(img0, 0, 0)
    image(img1, mouseX*0.7 - 150, 100)
    image(img2, 500,300)
    image(img3,width - mouseX*1.5,35)
