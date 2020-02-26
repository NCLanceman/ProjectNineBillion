import itertools
import timeit
import os

_length = 9
_maxRepeats = 3
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if not os.path.exists('Book of Names'):
    os.makedirs('Book of Names')

def nameTest(testArray):
    result = 0
    for i in range(len(testArray)-1):
        a = testArray [i]
        b = testArray[i+1]
        if (a == b):
            result += 1
        if (result >= _maxRepeats):
            return False    
    return True

def nameRun(nameLength, nameRepeats):
    answers = ""
    tabulatedAnswers = ""
    counter = 0
    miniCount = 0
    megaCount = 0
    startTime = timeit.default_timer()
    for t in itertools.product(alphabet, repeat=nameLength):
        if (nameTest(t) == True):
            counter += 1
            miniCount += 1
            tabulatedAnswers += ''.join(t) + "\n"
            if (counter / 1000000 == 1):
                fName = "result{}.txt".format(miniCount / 1000000)
            
                megaCount += 1
                megaResult = ''.join(t)
                
                printSignal = "{} millionth result: {}, Current Time: {}"
                currentTime = (timeit.default_timer()) - startTime
                printSignal = printSignal.format(megaCount,megaResult, currentTime)
                answers += printSignal 
                print(printSignal)
                counter = 0
                
                with open(os.path.join("Book of Names", fName), 'w') as f:
                    f.write(tabulatedAnswers)
                    f.close()
                tabulatedAnswers = ""
            
    endTime = timeit.default_timer()
    totalTime = endTime - startTime
    totalNames = miniCount
    
    result = """NAMES OF GOD
    \nLENGTH OF GOD: {} 
    \nREPEATS: {} 
    \nTotal Names of God: {}
    \nTotal Time Taken: {}\n\n"""
    result = result.format(nameLength, nameRepeats, totalNames, totalTime)
    
    return result + answers

f = open("resultOverview.txt", "w")
result = nameRun(_length, _maxRepeats)
f.write(result)
f.close()