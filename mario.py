from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
sense = SenseHat()


O = [255, 255, 255]  # White
r = [255, 0, 0]
b = [0, 0, 255]
y = [255, 255 , 0]
br = [165,42,42]
bl = [0,0,0]


mario = [
O, O, O, r, r, r, O, O,
O, O, br, y, y, y, O, O,
O, O, br, y, y, bl, y, O,
O, O, r, r, r, r, O, O,
O, r, r, b, b, r, r, O,
O, O, O, b, b, O, O, O,
O, O, b, O, O, b, O, O,
O, br, br, O, O, br, br, O
]

mario_up = [
O, O, O, r, r, r, O, O,
O, O, br, y, y, y, O, O,
O, O, br, y, y, bl, y, O,
O, O, r, r, r, r, O, O,
O, r, r, b, b, r, r, O,
br, O, O, b, b, O, O, br,
O, br, b, O, O, b, br, O,
O, O, O, O, O, O, O, O
]



        
def pushed_up():    
  sense.set_pixels(mario_up)
        



while True:
  sense.set_pixels(mario)
  sense.stick.direction_up = pushed_up
  time.sleep(1)




