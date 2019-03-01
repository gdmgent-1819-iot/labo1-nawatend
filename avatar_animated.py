from sense_hat import SenseHat
import time
import random


sense = SenseHat()





def randomAvatar():
  x = [0, 0, 0]  # empty
  a = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  avatar = [
  x,x,x,x,x,x,x,x,
  x,x,x,x,x,x,x,x,
  x,x,x,x,x,x,x,x,
  x,x,x,x,x,x,x,x,
  x,x,x,x,x,x,x,x,
  x,x,x,x,x,x,x,x,
  x,x,x,x,x,x,x,x,
  x,x,x,x,x,x,x,x,
  ]

  for i in range(0,8):
    for n in range(0,4):
      rSwitch = random.randint(0,1)
      if(rSwitch == 0):
        avatar[i*8+n] = x
        avatar[i*8+abs(n-7)] = x 
      else:
        avatar[i*8+n] = a
        avatar[i*8+abs(n-7)] = a
  sense.set_pixels(avatar)
  time.sleep(1)
  sense.clear(0,0,0)
  randomAvatar()


randomAvatar()