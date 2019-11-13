def setup ():
    size (800, 800)
    smooth ()
    background (255)
    strokeWeight (30)
    noLoop ()
    stroke (0 ,50)
def draw ():
    translate(200,200)
    for i in range(8):
        for k in range(4):
            line(i*50, 100*k, 150 + (i-1)*50, 100 + 100*k)
            line(i*50 + 100, 100*k, 50 + (i-1)*50, 100 + 100*k)
