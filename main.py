import sys

#########################################################
# part for checking immediate NO
def hasNumberIn(stringa):
    numeri = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numeri)):
         numeri[i] = str(numeri[i])
    for numero in numeri:
        if numero in stringa:
            print("NO")
            exit()
def checkTestLineNumber(text):
    rows = int(text[0])
    without = 0
    for i in range(2,len(text)):
        if ":" not in text[i]:
            without+=1
    if without!=rows:
        print("NO")
        exit()
def checkNumber(testLines):
    numeri = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numeri)):
         numeri[i] = str(numeri[i])
    for test in testLines:
        for numero in numeri:
            if numero in test:
                print("NO")
                exit()
def chechNumberDict(dict):
    keys = list(dict.keys())
    numeri = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numeri)):
        numeri[i] = str(numeri[i])
    for key in keys:
        for numero in numeri:
            if numero in key:
                print("NO")
                exit()
def checkIntoInto(dict):
    for key in dict:
        if len(key)>1:
            print("NO")
            exit()
        lista = dict[key]
        for elemento in lista:
            if elemento.isupper():
                print("NO")
                exit()
def emptyDict(dict):
    for key in dict:
        if dict[key][0]!='':
            return False
    return True
def nested(dict):
    for key in dict:
        if len(key)>1:
            print("NO")
            exit()
        if key.isupper()!=True:
            print("NO")
            exit()
        for elemento in dict[key]:
            if elemento in dict:
                print("NO")
                exit()
def double(dict):
    for key in dict:
        lista = dict[key]
        copia = set(lista)
        if len(lista)!=len(copia):
            print("NO")
            exit()
def sEmpty(myString,dict,testLines):
    flag=True
    if myString=="":
        for key in dict:
            if key.islower()==True:
                print("NO")
                exit()
            if dict[key]!=['']:
                flag=False
    else:
        flag=False
    if flag==True:
        keys = list(dict.keys())
        keys.sort()
        for key in keys:
            string = key + ":"
            print(string)
        exit()
def checkDictInTestline(testLines,dict):
    for testLine in testLines:
        for element in testLine:
            if element.isupper()==True:
                if element not in dict:
                    print("NO")
                    exit()
#########################################################

##########################################################
#this part of the code read the input and fills the data structures
def readInput(testLines, dict):
    text = []
    for line in sys.stdin:
        if len(text)==0 and line.strip().isnumeric()==False:
            print("NO")
            exit()
        if line == "\n" and text[-1].isnumeric()==False:
            break
        else:
            text.append(line.strip())
    myString=text[1]
    if len(text)==0:
        print("NO")  
        exit()
    if text[0].isnumeric()==False:
        print("NO")
        exit()
    rows = int(text[0])
    myString = text[1]
    if rows<0:
        print("NO")
        exit()
    
    checkTestLineNumber(text)
    for i in range(2,2+rows):
        testLines.append(text[i].strip())
    
    for i in range(2+rows,len(text)):
        if ":" not in text[i]:
            print("NO")
            exit()
        linea = text[i]
        linea = linea.strip().split(":")
        key = linea[0]
        if key.isupper()==False:
            print("NO")
            exit()
        hasNumberIn(key)
        values = linea[1].split(",")
        if key in dict:
            print("NO")
            exit()
        dict[key] = values
    
    rows = int(text[0])
    myString = text[1]
    nested(dict)
    fillWithLower(dict,testLines)
    if rows==0:
        keys = list(dict.keys())
        keys.sort()
        for key in keys:
            if key.islower()==False:
                string = key + ":"+dict[key][0]
                print(string)
        exit()
    
    if myString=="" or myString=="\n" or myString.isalpha()==False:
        if emptyDict(dict)==True:
            keys = list(dict.keys())
            for key in keys:
                string = key + ":"
                print(string)
            exit()
    double(dict)
    checkDictInTestline(testLines,dict)
    checkIntoInto(dict)
    checkNumber(testLines)
    chechNumberDict(dict)
    sEmpty(myString,dict,testLines)
    return rows,myString
##########################################################

##########################################################
#this part of the code prints the solution YES/NO
def createDict(testLine,solution):
    dict = {}
    i=0
    for letter in testLine:
        dict[letter] = solution[i]
        i+=1
    return dict

    for line in text:
        if ":" not in line and ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0") not in line or "," not in line:
            print("NO")
            exit() 
def giveOutput(dict,testLines,solutions):
    testLine = testLines[0]
    search = solutions[testLine] #here I have the solution
    for solution in search:
        confronto = createDict(testLine,solution) 
        giveOutputRecursive(dict,testLines[1::],solutions,confronto)
    print("NO")
    exit()
def createSolution(dict,confronto):
    for key in dict:
        if key not in confronto:
            confronto[key]=dict[key][0]  
def giveOutputRecursive(dict,testLines,solutions,confronto):
    if len(testLines)==0:
        createSolution(dict,confronto)
        chiavi = list(confronto.keys())
        chiavi.sort()
        for chiave in chiavi:
            if chiave.islower()==False:
                stringa = chiave + ":" + confronto[chiave]
                print(stringa)
        exit()
    else:
        search = solutions[testLines[0]]
        for solution in search:
            check = createDict(testLines[0],solution)
            keys1 = list(confronto.keys())
            keys2 = list(check.keys())
            commons = common_member(keys1,keys2)
            flag = checkMerge(confronto,check,commons) 
            if flag == True:
                merged = confronto | check
                giveOutputRecursive(dict,testLines[1::],solutions,merged)           
def checkMerge(dict1,dict2, keys):
    for key in keys:
        if dict1[key]!=dict2[key]:
            return False
    return True
def common_member(a, b):    
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return list(a_set.intersection(b_set))  
    else:
        return []
##########################################################

##########################################################
# part of the code for the solutions of each testLine
def fillWithLower(dict,testLines):
    for line in testLines:
        for element in line:
            if element.islower():
                dict[element] = element
def findSolutions(myString, testLine, dict):
    used = {}    #this dict register the value choosen for each set key=setName value=elementOfAlphabet
    result = []
    values = dict[testLine[0]]  # A : [a,b,c,d,e,f,dd]
    for element in values:
        # this function gives as an output a list with all the indexes where the element is found
        indexes = find_all(myString, element)
        
        while len(indexes) != 0:
            index = indexes.pop(0)     # popping the first element it's possible to know where the substring starts
            sol = [element]            # start building the solution
            used[testLine[0]]=element  # save the choice of which element the set has
            # this is a recursive function that gives a substring of myString starting at index + len(element)
            # from testLine remove the first set
            findSolutionsRecursive(myString[index + len(element)::], testLine[1::], dict, sol, result ,used)
            del used[testLine[0]] #backTrack
    return result
def find_all(myString, sub):
    if myString=="" and sub=="":
        return [0]
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
# this is the function that explores all the possible branches of the tree
def findSolutionsRecursive(myString , testLine , dict , sol , results , used):

    # if testLine is the empty string the recursion is finished
    if len(testLine)==0:
        if sol not in results:
            results.append(sol.copy())
        return
    else:
        # if the Set is in used it means that it has a value that it has to have
        if testLine[0] in used:
            element = used[testLine[0]]    # take the element that is used before
            value = myString.find(element) # search if that elment is at the beginning of myString (trimmed)
            if value==0:
                sol.append(element)
                findSolutionsRecursive(myString[len(element)::],testLine[1::],dict,sol ,results,used) #continue the exploration
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
                    findSolutionsRecursive(myString[len(element)::], testLine[1::], dict, sol, results , used)
                    del used[testLine[0]] #backTrack
                    sol.pop(-1)           #backTrack
            return
    return
##########################################################

##########################################################                
def main():
    testLines = []
    dict = {}
    rows,myString=readInput(testLines,dict)
    solutions = {}
    fillWithLower(dict,testLines)
    for line in testLines:
        solutions[line] = findSolutions(myString,line,dict)
    giveOutput(dict,testLines,solutions)
    
main()