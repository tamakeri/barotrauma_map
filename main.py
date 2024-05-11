"""import os
komut='\"C:\\Program Files\\7-Zip\.\\7z.exe\" e *.sub'
li1 = os.listdir()
result=os.system(komut)

li2 = os.listdir()
s = set(li1)
aranan_dosya = [x for x in li2 if x not in s]
"""
import time
f = open("thisss i", "r")

s=""
for i in f:
    s=s+i
flag=False
temp="\t"
real_arr=[]


# this block is for adding to array
for i in range(len (s)):
        if(s[i:i+7]=="</Item>"): 
            flag=False
            temp=temp+s[i:i+7]+"\n"
            real_arr.append(temp)
            temp="\t"
        if(s[i:i+10]=="<Item name"): 
                flag=True
        if (flag):
            temp=temp+s[i]
        







import re
# this block is not needed anym ore


# needd to make new arr


wire_id=[]
wire_reg="identifier=\"([a-z]*wire)\" ID=\"([0-9]*)\""
# this block for getting the id's

for i in range(len (real_arr)):
        a=re.search(wire_reg, real_arr[i])
        if(a!=None):
            b=a.group(1)+"  "+a.group(2)
            
            wire_id.append(b)








newarr=[]


name_id="( identifier=\"[A-Za-z0-9]+\" ID=\"[0-9]+\" )"
links="(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)"
input_name="<[A-Za-z]+t name=\".*\">"
#whole_idk="(<[A-Za-z]+t name=\".*\">)\n *(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>\n *)*(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)"
whole_idk="(      <[A-Za-z]+t name=\".*\">)(\n *)((<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)*(\n *)*)*"



# this block for getting the id's
for i in range(len (real_arr)):

        if(re.findall(name_id, real_arr[i])!=[] and re.findall(links, real_arr[i])!=[]):
            newarr.append(re.findall(name_id, real_arr[i]))

        if(re.findall(whole_idk, real_arr[i])!=[]):
            
            newarr.append(re.findall(whole_idk, real_arr[i]))
            

idk=[]


f = open("wires.xml", "w")
for i in range(len (wire_id)):

    f.write(str(wire_id[i]))
    f.write("\n")
f.close()


f = open("here_is_the list.xml", "w")
for i in range(len (newarr)):
    for item in newarr[i]:
        for items in item:
            if(items!="" and items!="\\n"):
                f.write(items)
                
                idk.append(items)
                
    f.write("\n")


with open("here_is_the list.xml") as my_file:
    newarr = my_file.readlines()



f.close()

#import a

#a.get_names(newarr)
import html_maker
html_maker.main(newarr,wire_id)

