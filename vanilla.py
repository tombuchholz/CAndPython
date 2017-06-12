import time, sys

def run(x):
    if (x < 1): x =1
    groupA = []
    groupB = []
    groupC = []

    for a in range(0,x):
        groupA.append(a+1)
        
    for a in groupA:
        groupB.append(a**2)
        
    for a in groupA:
        for b in groupB:
            groupC.append(a/b)

x = int(sys.argv[1])
step = 100
for xx in range(0 , x+step, step):
    now = time.process_time()
    run(xx)
    print (xx , ",", time.process_time() - now)
print (x , ",", time.process_time(), ", total")
