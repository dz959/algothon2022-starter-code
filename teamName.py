import numpy as np

nInst=100
currentPos = np.zeros(nInst)

def getMyPosition(prcSoFar):
  global currentPos

  days = len(prcSoFar[0])
  if days > 10:
    
    product = 0
    while product < 100: 
      j = 0
      counter = 0
      total = 0
      while j < days - 1:
          total += prcSoFar[product][j]
          j += 1
          counter += 1
      avg = total / counter
  
      p = days - 3
      counter2 = 0
      total2 = 0
      while p < days - 1: 
          total2 += prcSoFar[product][p]
          p += 1
          counter2 += 1
      avg2 = total2 / counter2

      u = days -4
      counter3 = 0
      total3 = 0
      while u < days - 1:
          total3 += prcSoFar[product][u]
          u += 1
          counter3 += 1
      avg3 = total3 / counter3

      max_position = 10000//prcSoFar[product][days-1]
  
      q = days - 5
      counter4 = 0
      total4 = 0
      while q < days - 1:
          total4 += prcSoFar[product][q]
          q += 1
          counter4 += 1
      avg4 = total4 / counter4

      t = days - 6
      counter5 = 0
      total5 = 0
      while t < days - 1:
          total5 += prcSoFar[product][t]
          t += 1
          counter5 += 1
      avg5 = total5 / counter5

      total10 = 0
      counter10 = 0
      k = days - 11

      while k < days - 1: 
          total10 += prcSoFar[product][k]
          k += 1
          counter10 += 1
      avg10 = total10 / counter10

      

      #if price is going up
      if prcSoFar[product][days-1] > avg2 > avg3> avg4 > avg5 > avg10:
        if currentPos[product] == 0 :
          currentPos[product] += max_position//1.1

        elif currentPos[product] < max_position:
            
            #stock increases more than 1.1 times yesterday
            if prcSoFar[product][days-1]  > 1.05 * prcSoFar[product][days-2]:
              currentPos[product] = max_position
            elif prcSoFar[product][days-1]  < prcSoFar[product][days-2]:
              pass

      #if price is going down - sell
      elif avg10> avg5 > avg4 >avg3> avg2 > prcSoFar[product][days-1]:
        if currentPos[product] == 0:
          currentPos[product] -= max_position//1.1

          #stock increases less than yesterday
        elif currentPos[product]<max_position:
          if prcSoFar[product][days-1]  < 0.97 * prcSoFar[product][days-2]:
            currentPos[product] -= max_position

          elif prcSoFar[product][days-1]  > prcSoFar[product][days-2]:
            pass

      product += 1
  else:
    pass
  return currentPos
