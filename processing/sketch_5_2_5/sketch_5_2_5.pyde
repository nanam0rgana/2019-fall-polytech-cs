def setup ():
 size (500, 500)
 smooth ()
 background (255)
 strokeWeight (30)
 noLoop ()
def draw ():
    stroke (20,100)
    i=1
    while i < 8:
        line(i*50, 200, 150 + (i-1)*50, 300)
        line(i*50 + 100, 200, 50 + (i-1)*50, 300)
        i+=2
