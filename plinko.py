import random
import csv

def Plinko(n):
  i = 0
  j = 0
  sol = []
  r=[]
  otherr=[]
  hashmap = {}
  old = []
  cur = [1]
  for numRows in range(n):
      while i < numRows -1:
          while j < len(old)- 1:
              cur.append(old[j]+old[j+1])
              j += 1
          cur.append(1)
          j = 0
          sol = cur
          old = cur
          cur = [1]
          i += 1
      r.append(sol)
  new = []
  for i in r:
      for num in i:
          new.append(num/ 2**(len(i)-1))
      otherr.append(new)
      new = []
  otherr[1] = [1]
  otherr.pop(0)
  with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(otherr)
  return otherr
