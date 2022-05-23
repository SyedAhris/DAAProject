#test data is a csv file starting with the maximum capacity, and then followed by the weights.
#data01 is not random and is the P08 from this website. https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
import random



for i in range (1,23):
    weights= []
    capacity = random.randint(10,10000)
    values = random.randint(5,1000)
    if (i == 1):
        values = 1
        weights.append(random.randint(0,capacity)) # 1 item but weight under capacity
    elif (i == 2):
        weight = random.randint(0,capacity)
        for x in range (0,values):
            weights.append(weight) # same weight for all items.
    elif (i == 3):
        for x in range(0,values):
            weights.append(1) # all items having weight of 1
    else:
        for j in range (0,values):
            if j<(1/3 * capacity):
                weight = random.randint(0,5000)
            else: 
                weight = random.randint(5000,20000)
            weights.append(weight)
    

    #writing to file
    if i < 10:
        filename = 'data0' + str(i) + '.csv'
    else: filename = 'data' + str(i) + '.csv'

    f = open(filename, 'w')

    writeString = str(capacity)
    for k in weights:
        writeString = writeString + ',' + str(k)


    f.write(writeString)


