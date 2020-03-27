
from itertools import permutations
from collections import deque
import time

convinced = 0
loopcounter = 0
potential_case = False
f= open("output.txt","w+")

message = ""
investors = ["1","2","3","4","5","6","7"]

investors_perm = permutations(investors)
no_funding_arrangement=[]

for case in investors_perm:

  message = "Rotating permutation number:" + str(loopcounter)+"\n"
  print(message)
  f.write(message)
  loopcounter +=1
  dcase = deque(case) 

  for i in range(1,8): #does 7 rotations

    dcase.rotate(1) #rotate the perm for 1, then for 2 etc..
    print(dcase)
    f.write(str(dcase)+"\n")
    convinced = 0 #this rotation hasn convinced anybody yet

    for j in range(7): #compare elements loop

      if dcase[j] == investors[j]: #see if any elements match
        convinced+=1
        if convinced > 1: #check if already found 2
          message = "Failed perm! "+str(convinced)+" investors Convinced \n"
          print(message)
          f.write(message)
          break #break the loop that compares elements
          #dont compare anymore

    if convinced > 1: #convinced 2 investors in this rotation
      print("Skipping this case...\n")
      potential_case = False #not a potential case anymore
      break #dont rotate this perm anymore because we failed already
    else: #couldn't convince more than 1 yet so we keep rotating
      potential_case = True

  #here we rotated this perm 7 times

  if potential_case: #if it still remains a pot_case it is now one
    message = "Found it! You get no funding if arrangement is:\n" + str(case) + " \n"
    print(message)
    f.write(message)
    no_funding_arrangement.append(case)
  
message="\n Results \n These cases give you no funding:\n"
print(message)
f.write(message)
for arr in no_funding_arrangement:
  message = str(arr)+"\n"
  print(message)
  f.write(message)
f.close()
    