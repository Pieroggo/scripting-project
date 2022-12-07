def triangles(string):
    # spliting file contents into pieces, casting them to int and saving them in the list
    variables=string.split("\n")
    checkedVars=[]
    if(len(variables)==0):
        print("Empty file")
        return "Empty file"
    if(len(variables)==1 or len(variables)==2):
        print("Not enough elements in file")
        return "Insufficient number of elements"
    i=0
    while(variables[i]!="0"):
        try:
            checkedVars.append(int(variables[i]))
        except ValueError:
            print("Input was invalid")
            return
        i+=1
        if(i>=len(variables)):
            print("Input was invalid")
            return
# sorting the list
    checkedVars.sort()
    i=0
    while(i<len(checkedVars)-2):
        sum=checkedVars[i]+checkedVars[i+1]
        if(sum>checkedVars[i+2]):
            return(f"{checkedVars[i]} {checkedVars[i+1]} {checkedVars[i+2]}")
        i+=1
    return("NIE")
noMoreFiles=False
i=1
while(noMoreFiles==False):
    fInName="in/in"+str(i)+".txt"
    fOutName="out/out"+str(i)+".txt"
    try:
        fileIn = open(fInName, "r")
        contents = fileIn.read()
        variables = contents.split("\n")
        if(len(variables)>2):
            fileOut = open(fOutName, "w")
            c=triangles(contents)
            if(c!=None):
                fileOut.write(c)
            fileOut.close()
        fileIn.close()
    except FileNotFoundError:
        noMoreFiles=True
    i+=1


