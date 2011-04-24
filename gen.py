import random

# define some constants
refLength = 10000

def generate():
  results = []
  last = int(random.random()*100)
  for num in range(0, refLength):
    if num > 0:
      last = results[num-1];
    chance = random.random()
    direction = int(random.random()*2)
    if chance < .9:
      if direction == 1 or last == 0 or num == 0:
        results.append(last + 1)
      else:
        results.append(last - 1)
    if chance >= .9:
      if chance < .95:
        results.append(int(random.random()*100))
      else: 
        if direction == 1 or last == 0 or num == 0:
           results.append(last + 2)
        else:
          results.append(last - 2)
  return results

def generateAdam():
    results = []
    for num in range(0, refLength):
        if random.random() < 0.9:
            # return something between 0 and 9
            results.append(int(random.random()*10))
        else:
            # pull something out of your butt
            results.append(int(random.random()*90)+10)
    return results

def stupid(ref, ResidentSetLimit):
  pFaults = 0
  resident = []
  for page in ref:
    # is the current page in the resident set?
    if page not in resident:
      if len(resident) < ResidentSetLimit:
        # just get it because we have room
        resident.append(page)
        pFaults+=1
      else: 
        # need to kick out a page, so which one?
        # pick one at random, that makes sense
        # eliminate from list_of_pages until one is left, kill that one
                thingToRemove = int(random.random()*len(resident)-1)
                del resident[:thingToRemove]
                resident.append(page)
                pFaults+=1
  return pFaults

def optimal(ref, ResidentSetLimit):
  pFaults = 0
  resident = []
  counter = 0
  for page in ref:
    # is the current page in the resident set?
    if page not in resident:
      if len(resident) < ResidentSetLimit:
        # just get it because we have room
        resident.append(page)
        pFaults+=1
      else: 
        # need to kick out a page, so which one?
        # find the page we are going to use last, knock it out
        list_of_pages = list(resident)
        # eliminate from list_of_pages until one is left, kill that one
        for todo in ref[counter:]:
          if len(list_of_pages) == 1:
            # we have found the one used the furthest in the future
            # remove it
            # add the new one, break
            break
          if todo in list_of_pages:
            list_of_pages.remove(todo)
        resident.remove(list_of_pages[0])
        resident.append(page)
        pFaults+=1
    counter+=1
  return pFaults

def lru(ref, ResidentSetLimit):
  pFaults = 0
  resident = []
  counter = 0
  for page in ref:
    if page not in resident:
      if len(resident) < ResidentSetLimit:
        # just get it because we have room
        resident.append(page)
        pFaults+=1
      else: 
        # need to kick out a page, so which one?
        list_of_pages = list(resident)
        # eliminate from list_of_pages until one is left, kill that one
        for todo in reversed(ref[:counter+1]):
          if len(list_of_pages) == 1:
            # we have found the one used the furthest in the future
            # remove it
            # add the new one, break
            break
          if todo in list_of_pages:
            list_of_pages.remove(todo)
        resident.remove(list_of_pages[0])
        resident.append(page)
        pFaults+=1
    counter+=1
  return pFaults
    
# main
# print the variables

print("time for testing")
OUTFILE = open("output.csv", 'w')
OUTFILE.write("ResSize, Aopt, Alru, Arand, Mopt, Mlru, Mrand\n")
reflist = generateAdam()
reflist2 = generate()
for resSize in range(1, 100):

  # print("Ref String Length: %i Resident Set Length: %i" % (ResidentSetLimit, refLength))
  # print("====================================\n")
  # print("using Adam's 90/10 rule")
  Aopt = optimal(reflist, resSize)
  Alru = lru(reflist, resSize)
  Arand = stupid(reflist, resSize)
  # print("optimal: %i " % (Aopt))
  # print("lru: %i" % (Alru))
  # print("random: %i" % (Arand))
  # print("====================================\n")
  Mopt = optimal(reflist2, resSize)
  Mlru = lru(reflist2, resSize)
  Mrand = stupid(reflist2, resSize)
  # print("using my 90/10 rule")
  # print("optimal: %i" % (Mopt))
  # print("lru: %i" % (Mlru))
  # print("random: %i" % (Mrand))
  line = str(resSize) + ", " + str(Aopt) + ", " + str(Alru) + ", " + str(Arand) + ", " + str(Mopt) + ", " + str(Mlru) + ", " + str(Mrand) + "\n"
  OUTFILE.write(line)
OUTFILE.close
