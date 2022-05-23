from greedyAlgorithm import greedyAlgorithm
from dynamicProgramming import dynamicProgramming
import time

outputFileName = 'output.csv'
outputFile = open(outputFileName, 'w')
#data number , greedyAns, greedyTime, DPans, DPTime
outputFile.write('Dataset,GreedyAnswer,GreedyTimeTaken,DPAnswer, DPTimeTaken, Maximum Capacity, Special Case\n')

for i in range(1,23):
    if i < 10:
        filename = 'data0' + str(i) + '.csv'
    else: filename = 'data' + str(i) + '.csv'

    f = open(filename, 'r')
    inputStr = f.readline()
    inputList = inputStr.split(',')
    capacity = inputList.pop(0)
    totalTime = 0
    for sd in range(0,len(inputList)):
        inputList[sd] = int(inputList[sd])
    for a in range(5):
        startTime = time.time()
        ansGreedy = greedyAlgorithm(inputList, len(inputList), int(capacity))
        endTime = time.time()
        timeTaken =  endTime - startTime
        totalTime = totalTime + timeTaken
    avgGreedyTime = totalTime/5

    

    totalTime = 0
    for a in range(5):
        startTime = time.time()
        ansDP = dynamicProgramming(inputList, len(inputList), int(capacity))
        endTime = time.time()
        timeTaken =  endTime - startTime
        totalTime = totalTime + timeTaken
    avgDPTime = totalTime/5

    
    outputFile.write(str(i) + ',' + str(ansGreedy) + ',' + str(avgGreedyTime) + ',' + str(ansDP) + ',' + str(avgDPTime) + ',' + str(capacity))


    if (i == 1):
        outputFile.write(',1 Single item\n') # 1 item but weight under capacity
    elif (i == 2):
        outputFile.write(',Same Weights for all items\n') # same weight for all items.
    elif (i == 3):
        outputFile.write(',All items having weight of 1\n') # all items having weight of 1
    else:
        outputFile.write(',None\n')


    print('Done with Test Data '+str(i))
    

