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
        



#this block is writing the xml for testing 
f = open("demofile2.xml", "w")
for i in range(len (real_arr)):
    f.write(real_arr[i])
f.close()

#open and read the file after the appending:
