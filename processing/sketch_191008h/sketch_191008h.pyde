points = ((80,300,300), (50,200,300), (30,300,200), (10,200,200))

def setup(): 
 size(500, 500)
 noLoop()
 
def draw():
 smooth();
 background(100);
 stroke(255);
 for x in points:
  strokeWeight(x[0])
  point(x[1], x[2])
