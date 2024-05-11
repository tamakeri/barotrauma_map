import re
import time
def man(idk):
    say=0
    aa=""
    re.search
    for i in range(len(idk)):
        if(re.findall("identifier=\"[A-Za-z0-9]+\" ID=\"[0-9]+\"",str(idk[i]))!=[]):   
            say=say+1
    print(say)

patern_ident="( identifier=\"([A-Za-z0-9]+)\" ID=\"([0-9]*)\" )" #get group 2 3
patern_name="(<[A-Za-z0-9]+ name=\"(.*)\">)" #get group 2
patern_link="(<link w=\"([0-9]*)\" i=\"([0-9]*)\" \/>)" #get group 23
durum=0

def get_names():
    with open("here_is_the list.xml") as file:
            for line in file:
                line=str(line)
                a=re.search(patern_ident,line);     b=re.search(patern_name,line);      c=re.search(patern_link,line)
                if a!=None:durum=1
                if b!=None:durum=2
                if c!=None:durum=3
                if(a==None&b==None&c==None):durum=0
                match durum:
                    case 0:
                        #wrap it uo
                        pass
                    case 1:#idnetfiear  and id
                        print(a.group(2))
                        print(a.group(3))
                        pass
                    case 2:#input/autpuname
                        print(b.group(2))
                    case 3:#linkto  and type
                        print(c.group(2))
                        print(c.group(3))
                        pass
                    case 0:
                        print("dansoz")
                        pass
                durum=0
                time.sleep(2)


cars = []


cars.append(["first",["ilk","iki"]])
cars.append(["second","offcier balls"])


cars [0].append(["uno","dos"])
print(cars[0][2][0])

print(cars)







get_names()


#
## read line

## determine type with regex
##find start
#
#