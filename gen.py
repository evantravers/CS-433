import random
import sys

# define some constants
ResidentSetLimit = 10
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

def stupid(ref):
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
        # todo fix the horribleness that is below 
        # resident.remove(random.random()*(len(resident)-1))
				tmp = int(random.random()*len(resident)-1)
				resident = resident[0:tmp]+resident[tmp+1:]
				resident.append(page)
				pFaults+=1
        
  return pFaults


def optimal(ref):
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
    
# main
reflist = generate()
print "optimal: ", optimal(reflist)
print "random: ", stupid(reflist)
