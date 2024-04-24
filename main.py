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

arr=[]
for i in f:
    print(i)



    #literaly  line arıyor daha iyi bir wire  aram a yöntemi bul
    time.sleep(5)
    if(i.find("wire")>0):


        
        arr.append(i)
        arr.append("|||")
    

print(arr[1])