import itertools
import timeit

length = 5
maxRepeats = 2
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def nameTest(testArray, nRepeat):
    result = 0
    for i in range(len(testArray)-1):
        a = testArray [i]
        b = testArray[i+1]
        if (a == b):
            result += 1
    
    if (result >= nRepeat):
        return False
    else:
        return True

def nameRun(nameLength, nameRepeats):
    answers = ""
    counter = 0
    megaCount = 0
    startTime = timeit.default_timer()
    for t in itertools.product(alphabet, repeat=nameLength):
        if (nameTest(t,nameRepeats) == True):
            counter += 1
            answers += ''.join(t) + "\n"
            if (counter / 1000000 == 1):
                megaCount += 1
                megaResult = ''.join(t)
                printSignal = "{} millionth result: {}"
                printSignal = printSignal.format(megaCount,megaResult) 
                print(printSignal)
                count = 0
    endTime = timeit.default_timer()
    totalTime = endTime - startTime
    totalNames = len(answers.split("\n"))
    
    result = """NAMES OF GOD
    \nLENGTH OF GOD: {} 
    \nREPEATS: {} 
    \nTotal Names of God: {}
    \nTotal Time Taken: {}\n\n"""
    result = result.format(nameLength, nameRepeats, totalNames, totalTime)
    
    return result + answers

f = open("results.txt", "w")
result = nameRun(length, maxRepeats)
f.write(result)
f.close()