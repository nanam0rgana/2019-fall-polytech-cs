add_library("sound")

img = 0
pointSize = 10

def setup():
  global img, song
  size(900,900)
  background(255)
  noStroke()
  println("Starting loading song...")
  song = SoundFile(this, "song.mp3")
  println("Song loaded!")
  img = loadImage("pic.jpg")
  song.play()
  
def draw():
  for i in range(500):
    loc = int(random(img.width*img.height))

    fill(color(img.pixels[loc]), 100)
    ellipse((loc%img.width),(loc/img.width),pointSize,pointSize)
    
