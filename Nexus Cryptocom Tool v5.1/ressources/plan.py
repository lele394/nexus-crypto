import ressources.matrix as m


def plan(key, i):
  planNumber = key[i%len(key)]
  while(0==0): #control loop for plan escape mode
  #---------  Z  ----------
    if planNumber == 11:
      plan = m.z1
      planName = "z1"
      break
    if planNumber == 12:
      plan = m.z2
      planName = "z2"
      break
    if planNumber == 13:
      plan = m.z3
      planName = "z3"
      break
    if planNumber == 14:
      plan = m.z4
      planName = "z4"
      break
    if planNumber == 15:
      plan = m.z5
      planName = "z5"
      break
    if planNumber == 16:
      plan = m.z6
      planName = "z6"
      break
    #---------  Y  ----------
    if planNumber == 17:
      plan = m.y1
      planName = "y1"
      break
    if planNumber == 18:
      plan = m.y2
      planName = "y2"
      break
    if planNumber == 19:
      plan = m.y3
      planName = "y3"
      break
    if planNumber == 20:
      plan = m.y4
      planName = "y4"
      break
    if planNumber == 21:
      plan = m.y5
      planName = "y5"
      break
    if planNumber == 22:
      plan = m.y6
      planName = "y6"
      break
  return plan
   