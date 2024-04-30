import re

def man(idk):
    say=0
    aa=""
    for i in range(len(idk)):
        if(re.findall("identifier=\"[A-Za-z0-9]+\" ID=\"[0-9]+\"",str(idk[i]))!=[]):   
            say=say+1

    print(say)


