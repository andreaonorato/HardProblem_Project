file = open("test01.swe","r")


rows = int(file.readline())
myString = file.readline()
dict={}  #ABC , DDS , FDS
solutions = {}
testLines = set()
while rows!=0:
    line = file.readline().strip()
    rows-=1
    testLines.add(line)
    #solutions[line] =[] # --> [ (sol1) , (sol2) ... ]
    


dict={}
for line in file:
    line = line.strip().split(":")
    values = line[1].split(",")
    dict[line[0]] =values


print("This is myString: ", myString)
print("This is our testLines: ", testLines)

print("The dict has the following values: ")
for key in dict:
    print(key , "  " , dict[key])

grammar = {}
# grammar [ABD] = [(sol1),(sol2)]
for test in testLines:
    
    grammar[test] = [ (a,b,d), (b,d,d) ]

# abdde
# controlla se in A non ci sono lettere abdde output NO

    

    
# Un dizionario con come keys 'ABd' e le altre testLines e come values una lista di tuple [ (a,b,d), (b,d,d) ]

#capiamo per ogni parola quali sono i suoi set approvati
#ad esempio per ABD posso accettare [(a,b,d) , (b,d,a) ,(...)  ]
#dopo che l'ho fatto per per tutti cerco set simili