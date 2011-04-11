import random
results = []

last = 1

for num in range(0, 10000):
  if num > 0:
    last = results[num-1];
  chance = random.random()
  direction = int(random.random()*2)
  if chance < .9:
    if direction == 1 or last == 0:
      results.append(last + 1)
    else:
      results.append(last - 1)
  if chance >= .9:
    results.append(int(random.random()*100))
  
print results    