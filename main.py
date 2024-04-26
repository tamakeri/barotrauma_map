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
temp=""
real_arr=[]



for i in range(len (s)):

    if (flag):
        temp=temp+s[i]
        


    if(s[i]=="<"):
        if(s[i:i+6]=="<Item "): 
            flag=True
            temp=temp+s[i]

        if(s[i:i+7]=="</Item>"): 
            flag=False
            temp=temp+s[i]
            real_arr.append(temp)
            temp=""
            

print(real_arr)



f = open("demofile2.txt", "a")
for i in range(len (real_arr)):
    f.write(real_arr[i])
f.close()

#open and read the file after the appending:
