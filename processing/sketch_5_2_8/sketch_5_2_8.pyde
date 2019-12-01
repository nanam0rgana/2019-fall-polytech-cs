def setup ():
    size (500, 500)
    smooth ()
    background (255)
    noStroke ()
    noLoop ()
def draw ():
    for i in range(10):
        for k in range(10):
            if i%2==0:
                fill(k*20)
                rect(k*40+50 , 50 + 40*i, 35, 35)
            else:
                fill(220-k*20)
                rect(k*40+50 , 50 + 40*i, 35, 35)
                
