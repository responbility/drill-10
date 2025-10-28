from pico2d import load_image

class Ball:

    image = None

    def __init__(self, 400, 300, velocity(1)):
           if Ball.image is None:
                Ball.image = load_image('ball21x21.png')
              self.x , self.y ,self.velocity = x , y , velocity




    def draw (self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x

        if self.x < 0 or self.x > 800:
            self.velocity = -self.velocity
