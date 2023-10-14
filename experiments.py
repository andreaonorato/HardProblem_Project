# FILE CREATED JUST FOR EXPERIMENTs FOR THE SINTAX
input_string = 'DDE'
list_of_tuples = [('a', 'b', 'c'), ('d', 'd', 'e'), ('e', 'e', 'd'), ('c', 'd', 'e')]

filtered_tuples = []

for tup in list_of_tuples:
    if all(char in ''.join(tup) for char in input_string):
        filtered_tuples.append(tup)

print(filtered_tuples)
