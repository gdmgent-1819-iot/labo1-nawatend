from sense_hat import SenseHat
import random
import time

sense = SenseHat()



message = "Hello! We are New Media Development :)"
while True:
  c_text = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  c_bg = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  sense.show_message(message,text_colour=c_text, back_colour = c_bg)



