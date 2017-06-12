import time, sys
import numpy as np

def run(x):
    if (x < 1): x =1
    groupA = np.array([x])
    groupB = np.array([x])
    groupC = np.array([x])

    for a in range(0,x):
        groupA.itemset(x) = (a+1)
    
    i = 0
    for a in groupA:
        groupB.item(x) = (a**2)
        i+=1

    i = 0
    for a in groupA:
        for b in groupB:
            i += 1
            groupC.item(x) = (a/b)

x = int(sys.argv[1])
step = 100
for xx in range(0 , x+step, step):
    now = time.process_time()
    run(xx)
    print (xx , ",", time.process_time() - now)
print (x , ",", time.process_time(), ", total")
