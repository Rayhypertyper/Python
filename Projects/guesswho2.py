traits = ["Eyes", "Ears", "Horns", "Color", "Nose", "Hair", "Fins", "Hat", "Eyebrows"]
creaturesdict = {"Jason":["2", "y", "y", "purple", "y", "y", "n", "y", "y"], 
                 "Violet":["2", "n", "n", "yellow", "n", "n", "y", "n", "y"], 
                 "Bernie":["2", "n", "y", "beige", "y", "n", "n", "n", "n"], 
                 "Lawrence":["1", "n", "n", "blue", "n", "n", "n", "n", "y"], 
                 "Edith":["3", "n", "n", "green", "n", "n", "n", "n", "n"], 
                 "Umberto":["4", "n", "n", "purple", "n", "n", "n", "y", "y"], 
                 "Eve":["4", "n", "n", "blue", "n", "n", "n", "n", "n"], 
                 "Walter":["2", "n", "n", "green", "n", "y", "n", "y", "y"], 
                 "Telly":["1", "n", "n", "purple", "y", "n", "n", "n", "n"], 
                 "Opus":["2", "n", "n", "green", "n", "n", "n", "y", "y"], 
                 "Zed":["2", "n", "n", "yellow", "n", "n", "y", "n", "n"], 
                 "Petrovo":["2", "y", "n", "beige", "n", "n", "n", "n", "n"], 
                 "Richard":["4", "n", "y", "green", "n", "n", "n", "n", "n"], 
                 "Celia":["4", "n", "n", "purple", "y", "y", "n", "n", "y"],
                 "Hakem":["3", "n", "n", "yellow", "n", "n", "n", "n", "n"], 
                 "Boris":["1", "y", "n", "blue", "n", "n", "n", "y", "n"],
                 "Albert":["1", "n", "n", "beige", "y", "n", "y", "n", "y"], 
                 "Gina":["3", "y", "n", "green", "n", "y", "n", "n", "n"],
                 "Molly":["3", "y", "y", "blue", "n", "y", "n", "n", "y"], 
                 "Peter":["3", "n", "y", "yellow", "n", "y", "n", "n", "y"],
                 "Finnian":["1", "n", "n", "green", "n", "n", "n", "n", "n"],
                 "Sam":["2", "n", "n", "purple", "n", "n", "y", "n", "y"], 
                 "Edgar":["4", "n", "n", "blue", "n", "n", "n", "n", "n"],
                 "Quill":["2", "n", "n", "beige", "n", "n", "y", "n", "y"]}

#dictionary of questions. could change this to if the options are numbers, they ask how many, else ask what ... is it.
# ques = {"Eyes": "How many eyes does it have?", "Color": "What color is it?"}

#finds all traits with more than 2 options
chartraits = {}
b = list(creaturesdict.values())[0] #.values gets the values of the dictionary, and turns it into list. WE take first index of this 2d list, as the length of all the values are all the same. 
for i in range(len(b)):
  sit = set()
  boo = False #set as not number question as default
  for j in range(len(creaturesdict)):
    val = (list(creaturesdict.values()))[j][i]
    sit.add(val)
  if len(sit) > 2:
    for k in sit: #checks if the elements have numbers in them so it can ask questions accordingly
      if not k.isnumeric():
        boo = True
        break
    if boo:
      x = input(f"What {traits[i]} is it?? ")
      while x not in sit:
        x = input(f"Invalid input! Please enter a valid choice of {traits[i]}")
    else:
      x = input(f"How many {traits[i]} does it have?")
    while x not in sit:
      x = input(f"Invalid input! Please enter a valid number of {traits[i]}")
    chartraits[traits[i]] = x #assign the input to a trait. adds traits given by user to a dict

#remove options not fitting description. Makes new dict newopts with matching possibilites
newopts = []
mewopts = []
for key,value in creaturesdict.items():
  boo = False
  for cey, walue in chartraits.items():
    #because in the traits dictionary its stored in {"feature":"value"}
    #so by searching through traits list to find index of the feature in the values to comepare with walue
    if value[traits.index(cey)] == walue:
      pass
    else:
      boo = True
      break
  if not boo:
    newopts.append([key, value])

#yes no part
#also by this point, it is only yes and noes left
#loop through all the options, and see which .count y and .count n have the same amounts, or closests
#records the index
#do this in a while len(newopts) = 1

print(newopts)

while len(newopts) > 1:  
  lowest = float('inf')
  lindex = 0
  for i in range(len(newopts[0][1])):
    aa = newopts[0][0]
    ncount = 0
    ycount = 0
    boole = False
    for j in range(len(newopts)):
      aaa = newopts[j][1][i]
      if newopts[j][1][i] == 'y':
        ycount+=1
      elif newopts[j][1][i] == 'n':
        ncount+=1
      else:
        boole = True
        break 
    if boole:
      continue #after break statement, we don want it to continue in this loop
    if abs(ycount-ncount) < lowest:
      lowest = abs(ycount-ncount)
      lindex = i
  a = input(f'Does it have {traits[lindex]}? (y/n)')
  newopts = [newopts[i] for i in range(len(newopts)) if newopts[i][1][lindex] == a]
print(newopts[0][0])# possible test cases beige w 2 eyes, blue with 1 eye
  # for i in range(len(newopts)):
  #   if newopts[i][1][lindex] == a:
      
    
        
  # newopts = [newopts[l] for l in range(len(newopts)) if any(newopts[l][1][k] != a for k in range(len(newopts[0][0])))]

  # for k in range(len(newopts[0][1])):
  #   for l in range(len(newopts)):
  #     aaa = newopts[l][1][k] 
  #     if newopts[l][1][k] == a:
  #       mewopts.append(newopts[l])
        
        
  # newopts = [l for k in range(len(newopts[0][1])) for l in range(len(newopts)) if newopts[l][1][k] == a]
  # pass
  # pass
    #used list comprehsnion, so I can use newopts agian isntead of creating new variable
#     newopts = [newopts[l] for l in range(len(newopts)) if newopts[l][1][k] == a]
# print(f'your character is {newopts[0][0]}')

    
        #make a new list with them
      
  

      


    
      
        
    
  


    
  
    
    
# diversity = {}
# element = 0
# biggest = 0
# #adds each element of all the characters to a set
# for _, value in creaturesdict:
#   for i in range(len(value)):
#     sets[i].add(value[i])
# #in the set, we see which one is the longest, to see which one is most diverse
# for i in range(len(sets)):
#   if len(sets[i]) > biggest:
#     biggest = len(sets[i])
#     element = i
# if element == 1:
#   x = input("How many eyes does it have")
# elif element == 5:
#   x = input("What color is it")
  

# make dictionary for all possible traits and questions for them
# finds all traits with more than two options, so we can ask how many questions
# after asking these, we compile a list of possible candidates
# We are left with yes and no questions, make sure the question im asking has half or more than half the options.
# Once the quesiton is asked, loop through the matching characters and remove ones with the non option. 
# keep on going until length of list is 1


