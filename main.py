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

"""
            # needd to make new array
            wire_array=[]




            for i in range(len (real_arr)):
                if(re.search(a, real_arr[i])):
                    wire_array.append(real_arr[i])






            wire_id=[]
            wire_reg="ID=\"([^\"]*)\""
            # this block for getting the id's
            for i in range(len (wire_array)):
                    wire_id.append(re.search(wire_reg, wire_array[i]).group(1))





"""




newarr=[]


name_id="( identifier=\"[A-Za-z]+\" ID=\"[0-9]+\" )"
links="(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)"

# this block for getting the id's
for i in range(len (real_arr)):
        if(re.findall(name_id, real_arr[i])!=[] and re.findall(links, real_arr[i])!=[]):
            newarr.append(re.findall(name_id, real_arr[i]))
            
        
        if(re.findall(links, real_arr[i])!=[]):
            newarr.append(re.findall(links, real_arr[i]))







#this block is writing the xml for testing 
f = open("here_is_the list.xml", "w")
for i in range(len (newarr)):

    f.write(str(newarr[i]))
    f.write("\n")
f.close()










#open and read the file after the appending:
