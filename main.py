definitions1 = "definitions.txt"
definitions = {}
file = open(definitions1, 'r')
lines = file.readlines()
file.close()
for line in lines:
    words = line.strip('\n').split('-')
    if len(words) == 2:
        definitions[words[0]] = words[1]


while True:
     input1 = input("input here:  ")
     history1 = open("history.txt", 'a')
     history1.write(input1 + "\n")
     history1.close()
     if input1 in definitions:
         print(definitions[input1])
     else:
        print("Word not in dictionary")

     continue1 = input("do you wish to continue? (y/n) ")
     if continue1 == "y":
        continue
     elif continue1 =="n":
           break
