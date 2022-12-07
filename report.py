import os,time
i=1
inFiles=[]
inContents=[]
outFiles=[]
outContents=[]
modDates=[]
outOfFiles=False
try:
    while(outOfFiles==False):
        inName=f"in/in{i}.txt"
        inFile=open(inName, "r")
        if(inFile.read()!=""):
            inFiles.append(inName)
            inFile.seek(0)
            inNums=inFile.read().split("\n")
            inString=""
            for num in inNums:
                inString+=num+" "
            inString=inString[:-1]
            inContents.append(inString)
        outName = f"out/out{i}.txt"
        outFile = open(outName, "r")
        if (outFile.read() != ""):
            outFiles += [outName]
            outFile.seek(0)
            outContents += [outFile.read()]
            modDates+=[time.ctime(os.path.getmtime(outName))]
        if(inFile.read()!="" and outFile.read() != ""):
            outOfFiles=True
        i+=1
except IOError:
    ...
backup=open('backup.txt',"w")
backup.write("List of files:\n")
for i in range(len(inFiles)):
    if(i<len(outFiles)):
        print(f"{inFiles[i]} ({inContents[i]}) -> {outFiles[i]} ({outContents[i]})  Last Modified: {modDates[i]}")
        backup.write(f"{inFiles[i]} ({inContents[i]}) -> {outFiles[i]} ({outContents[i]})  Last Modified: {modDates[i]}\n")
    else:
        print(f"{inFiles[i]} ({inContents[i]})")
        backup.write(f"{inFiles[i]}\n")
report=open("report.html","w")
content=f"<!DOCTYPE html>" \
    f"\n<html>" \
    f"\n<head>" \
        f'\n<link rel="stylesheet" type="text/css" href="style.css">' \
        f"\n</head>" \
        f"\n<body>" \
    f"\n<h1>List of files:</h1>" \
    f"\n<div>" \
    f'\n<table>'\
     f"\n<tr>"\
     f"\n<th>Input File</th>" \
        f"\n<th>Input Data</th>" \
        f"\n<th>Output File</th>" \
        f"\n<th>Output Data</th>" \
        f"\n<th>Creation Date</th>"\
     f"\n</tr>"
print(f"inFiles: {len(inFiles)} inContents: {len(inContents)} outFiles: {len(outFiles)} outContents: {len(outContents)} ModDates: {len(modDates)}")
for i in range(len(inFiles)):
    content+=f"\n<tr>"
    if(i<len(outContents)):
        content+=f"\n<td>{inFiles[i]}</td>"
        content += f"\n<td>{inContents[i]}</td>"
        content +=f"\n<td>{outFiles[i]}</td>"
        content += f"\n<td>{outContents[i]}</td>"
        content +=f"\n<td>{modDates[i]}</td>"
    else:
        content+=(f"\n<td>{inFiles[i]}</td>")
        content += f"\n<td>{inContents[i]}</td>"
    content+=f"\n</tr>"
content+=f"\n</table>"\
        f"\n</div>" \
        f"\n</body>" \
        f"\n</html>"
report.write(content)
