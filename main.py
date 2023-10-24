import sys
def main():
    print("ciao")
    file = open("/Users/enricotuda/Documents/GitHub/HardProblem_Project1/tests/test02.swe", "r")  # reading file test01.swe for testing
    #devo fare con sys.stdin
    text = sys.stdin.readlines()
    
    rows = int(text[0].strip())
    myString = text[1].strip()
    text.pop(0)
    text.pop(0)




    #rows = int(file.readline())  # number of testLines
    #myString = file.readline()  # our goal string
    dict = {}  # we will save inside A: ['asd', 'b', 'c'] etc
    testLines = list()  # 'ABD' 'DDE' etc
    result_dict = {}  # we will save a map with our testLines as keys and our possible combinations as values
    print(dict)
    print(testLines)
    # Herer we get our testLines
    while rows != 0:
        testLines.append(text.pop(0).strip())
        #line = file.readline().strip()
        rows -= 1
        #testLines.append(line)

    # Here we populate our dictionary
    for line in text:
        line = line.strip().split(":")
        values = line[1].split(",")
        dict[line[0]] = values

    #testLines ha [ABC,BCD,eccccc]

    #this piece of code solve the problem of lowercase letters in the testlines
    for test in testLines:
        for character in test:
            if character.islower()==True:
                dict[character]=character   # I simply create a set named d: d which contains only itself



    results = {}


    totale={}
    for sequenza in testLines:
        totale[sequenza]=findResultsTestline(myString,sequenza,dict)


    for key in totale:
        if len(totale[key])==0:
            print("NO")
            exit(0)

    findSolution(totale)
    print("NO")






# this function given myString, one testline and the dict with [ nameSet : alphabet]
# gives as an output a table with all the valid combination of elements for each alphabet
def findResultsTestline(myString, testLine, dict):
    used = {}    #this dict register the value choosen for each set key=setName value=elementOfAlphabet
    result = []
    values = dict[testLine[0]]  # A : [a,b,c,d,e,f,dd]
    for element in values:
        # this function gives as an output a list with all the indexes where the element is found
        indexes = find_all(myString, element)
        while len(indexes) != 0:
            index = indexes.pop(0)    # popping the first element it's possible to know where the substring starts
            sol = [element]       # start building the solution
            used[testLine[0]]=element  # save the choice of which element the set has
            # this is a recursive function that gives a substring of myString starting at index + len(element)
            # from testLine remove the first set
            explore(myString[index + len(element)::], testLine[1::], dict, sol, result ,used)
            del used[testLine[0]] #backTrack
    return result

def find_all(myString, sub):
    result = []
    k = 0
    while k < len(myString):
        k = myString.find(sub, k)
        if k == -1:
            return result
        else:
            result.append(k)
            k += 1 #change to k += len(sub) to not search overlapping results
    return result

#this is the function that explore all the possible baraches of the tree
def explore(myString , testLine , dict , sol , results , used):
    # if testLine is the empty string the recursion is finished
    if len(testLine)==0:
        results.append(sol.copy())
        return
    else:
        # if the Set is in used it means that it has a value that it has to have
        if testLine[0] in used:
            element = used[testLine[0]]    # take the element that is used before
            value = myString.find(element) # search if that elment is at the beginning of myString (trimmed)
            if value==0:
                sol.append(element)
                explore(myString[len(element)::],testLine[1::],dict,sol ,results,used) #continue the exploration
                sol.pop(-1)  #bakctrack
                return
            else:
                return  # if it is not at the beginnig we know that's not a solution
        else:
            values = dict[testLine[0]] ## A : [a,b,c,d,e,f,dd]
            for element in values:
                value = myString.find(element)
                if value==0:  #if it's at the beginning
                    sol.append(element)
                    used[testLine[0]]=element # put in used the fact that the set X is using the element 'y'
                    explore(myString[len(element)::], testLine[1::], dict, sol, results , used)
                    del used[testLine[0]] #backTrack
                    sol.pop(-1)           #backTrack
            return
    return



# this function search for 1 solution
def findSolution(dict):
    used = {}
    #this checks if the dict is empty
    if len(dict.keys())==0:
        print("No")
        exit(0)
    keyList = list(dict.keys()) # find the "first" testLine of the dict
    first = keyList[0]
    for solution in dict[first]:
        fillAtBeginnning(first, solution, used) #this function fills used for every solution of the first testLine
        exploreSolutions(keyList[1::], used, dict) #don't consider the first testLine studied in this function
        used = {}                               #backTrack


def exploreSolutions(testLines , used , dict):
    # [GDCA, AD, ABC , ADGA...]
    # used--> {A : a , B:dd...}
    if len(testLines)==0: # all the testLines are finished so all respect the constrains
        
        keys = list(used.keys()) # lista [A;B;C;D]
        keys.sort()
        for key in keys:
            if key.islower()==False:
                print(key, ":", used[key][0])
        exit(1) #when one solution is Found exit
    else:
        solutions = dict[testLines[0]]

        #try every solution
        for solution in solutions:
            #if this function returns True it's possible to continue the exploration because all the constrains are respected
            ris = fillUsed(testLines[0], solution, used) # add constrins if required and check that the prevoious are respected
            if ris==True:
                exploreSolutions(testLines[1::], used, dict) # continue exploration
                emptyUsed(testLines[0], solution, used)      #backTrack

def fillAtBeginnning(testLine , solution , used ):
    for i in range(len(solution)):
        if testLine[i] in used:
            if used[testLine[i]]!=solution[i][0]:
                return False
        else:
            used[testLine[i]]=[solution[i],1]
    return True


def fillUsed(testLine, solution, used):
    for i in range(len(solution)):
        if testLine[i] in used:
            if solution[i]!=used[testLine[i]][0]:
                return False                         #to verify that all the constrains are respected
    for i in range(len(solution)):
        if testLine[i] in used:
            used[testLine[i]][1]+=1                  #increment the counter of how many times the set X compares
        else:
            used[testLine[i]]=[solution[i],1]        #say that the set X compares 1 time
    return True

def emptyUsed(testLine,solution, used):
    for i in range(len(solution)):
        if used[testLine[i]][1]==1:      #it means that we take out the constrain in set X
            del used[testLine[i]]
        else:
            used[testLine[i]][1]-=1







main()
