def generate_combinations(sub_string, substitutions, current_combination, valid_combinations): # called from the function generate_combinations(secondString, dict, [], valid_combinations)
    if not sub_string:
        valid_combinations.append(tuple(current_combination))
    else:
        char, *rest = sub_string # it means it assign to char the first char of the string and assign the remaining part of the string to *rest
        if char in substitutions:
            for substitution in substitutions[char]:
                generate_combinations(rest, substitutions, current_combination + [substitution], valid_combinations)   # recursive function to find the different substring
        else: 
            generate_combinations(rest, substitutions, current_combination + [char], valid_combinations) # case where we have lower-case letter in our testLine

def character_positions(input_string):  # function explained where we call it
    char_positions = {}
    for index in range(len(input_string)):
        char = input_string[index]
        if char in char_positions:
            char_positions[char].append(index)
        else:
            char_positions[char] = [index]

    return char_positions


file = open("tests/test01.swe","r")   # reading file test01.swe for testing

rows = int(file.readline())   # number of testLines
myString = file.readline()   # our goal string
dict={} # we will save inside A: ['asd', 'b', 'c'] etc
testLines = list()   # 'ABD' 'DDE' etc
result_dict = {} # we will save a map with our testLines as keys and our possible combinations as values

# Herer we get our testLines
while rows!=0:
    line = file.readline().strip()
    rows-=1
    testLines.append(line)

# Here we populate our dictionary
for line in file:
    line = line.strip().split(":")
    values = line[1].split(",")
    dict[line[0]] =values


print("\nThis is myString: ", myString)
print("\nThese are our testLines: ", testLines)

print("\nThe dict has the following values: ")
for key in dict:
    print(key , "  " , dict[key])

for secondString in testLines:
    # Create a list to store the valid combinations as tuples
    valid_combinations = []

    # Generate combinations as tuples - function written at the beginning of the file
    generate_combinations(secondString, dict, [], valid_combinations)

    # First process of filtration to combine and join our substring results
    filtered_valid_combinations = []
    for combination in valid_combinations:
        if ''.join(combination) in myString:
            filtered_valid_combinations.append(combination)

    valid_combinations = filtered_valid_combinations

    # Second process of filtration - still have to filter "same letters"/"duplicates" in the way that A has only one corresponding value, so we check for duplicates
    valid_combinations_duplicate_case = []
    input_string = secondString
    char_positions = character_positions(input_string) # Here I'll have a map with letter as key and indexes of that letter as values, for example 'DEDF' will create the map {D: [0,2], E: [1], F: [3]}
    for char, positions in char_positions.items():
        if (len(positions)) > 1:   # means if there's a duplicate char, so in the example used before the positions will be [0,2] because D is a duplicate letter in our string
            for m in range(len(valid_combinations)):
                for i in range(len(positions)-1):
                    if valid_combinations[m][positions[i]] == valid_combinations[m][positions[i+1]]:
                        valid_combinations_duplicate_case.append(valid_combinations[m]) # we just put the duplicate case if it's present and delete the other cases which would lead to an error
                        

        else:
            pass  # in this case our string does not contain duplicate letters

    if len(valid_combinations_duplicate_case)>0: # --> if our testLine contains duplicate letters:
        valid_combinations = valid_combinations_duplicate_case
    
    print("\nFor the testLine "+ secondString + " the valid combinations are: ")
    print(valid_combinations)
    
    result_dict[secondString] = valid_combinations

# Finally, we check for common sets:
#print(result_dict)