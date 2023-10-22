ds1 = [-1, -3, 0, -100, -100]

ds1.sort() 
minSum = 0;
for i in range(0, len(ds1)):
  while minSum > minSum + ds1[i]: 
    minSum = minSum + ds1[i];
    i+=1;
  break;

print(minSum)
