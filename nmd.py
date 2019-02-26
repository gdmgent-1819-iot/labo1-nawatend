from sense_hat import SenseHat
import random
import time

sense = SenseHat()



while True:
  for i in ("N", "M","D"):
    c = (random.randint(1,256),random.randint(1,256),random.randint(1,256))
    sense.show_letter(str(i),text_colour=c)
    time.sleep(1)
  time.sleep(2)