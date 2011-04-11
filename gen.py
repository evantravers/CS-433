import random

# define some constants
WorkingSetLimit = 10
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
      results.append(int(random.random()*100))
  return results

def optimal(ref):
  pFaults = 0
  resident = []
  counter = 0
  for page in ref:
    # is the current page in the resident set?
    # TODO fix this shoddy workaround
    pageInResidentSet = False
    try:
      pageInResidentSet = resident.index(page)
    except ValueError:
      pass
      
      if not pageInResidentSet:
        if len(resident) <= WorkingSetLimit:
          # just get it because we have room
          resident.append(page)
          pFaults+=1
        else: 
          # need to kick out a page, so which one?
          # find the page we are going to use last, knock it out
          list_of_pages = resident
          # eliminate from list_of_pages until one is left, kill that one
          for todo in ref[counter:]:
            if len(list_of_pages) == 1:
              # we have found the one used the furthest in the future
              # remove it
              # add the new one, break
              resident.remove(list_of_pages[0])
              resident.append(page)
              pFaults+=1
              break
              
            # TODO fix this shoddy workaround
            pageUsed = False
            try:
              pageUsed = list_of_pages.index(todo)
            except ValueError:
              pass
              
            if pageUsed:
              list_of_pages.remove(todo)
    counter+=1
  return pFaults
    
# main
reflist = generate()

print optimal(reflist);
