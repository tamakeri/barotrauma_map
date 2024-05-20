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

solution=r' (.*<[A-Za-z]+ name=".*">\n)(.*<link w="[0-9]+" i="\d" \/>\n)*(.*<link w="[0-9]+" i="\d" \/>)+\n.*\/[A-Za-z]+>'
name_id="(identifier=\"[A-Za-z0-9]+\" ID=\"[0-9]+\" )"
links="(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)"
input_name="<[A-Za-z]+t name=\".*\">"
#whole_idk="(<[A-Za-z]+t name=\".*\">)\n *(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>\n *)*(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)"
whole_idk="(      <[A-Za-z]+t name=\".*\">)(\n *)((<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)*(\n *)*)*"


some_flag=False
# this block for getting the id's
for i in range(len (real_arr)):
        some_flag=False
        if(re.findall(name_id, real_arr[i])!=[] and re.findall(links, real_arr[i])!=[]):
            anan=re.search(name_id, real_arr[i])
            
            newarr.append(anan.group(1))
            
            some_flag=True
        else:some_flag=False
        temp_=""
        #upper dondişton must bew met to desceond into loop
        flagone=False
        flagtwo=False
        if(some_flag):
            a=str (real_arr[i])
            b=a.split("\n")
            flagone=False
            flagtwo=False
    
            for i in range (len(b)):

            
                if((b[i].find("<output") >0 or b[i].find("<input")>0) and b[i].find("/>")<1):
                    flagone=True
                    
                    temp_=""

                if(b[i].find("</output") >0 or b[i].find("</input")>0):
                    flagtwo=True
                    pass
                if(flagone):
                    temp_=temp_+b[i]
                if(flagone and flagtwo):

                    into=temp_.split(">")
                    for i in range(len(into)-1):
                        a=(str(into[i]))
                        if(len(a)>0):
                            a=a+">"

                        newarr.append(a)
                        
                    flagone=False;flagtwo=False
                    pass



                    
                    
                    
                    
                    
                

'''
        if(re.findall(solution, real_arr[i])!=[]):
            b=re.findall(solution, real_arr[i])
            newarr.append(b)
'''


f = open("wires.xml", "w")
for i in range(len (wire_id)):

    f.write(str(wire_id[i]))
    f.write("\n")
f.close()


f = open("here_is_the list.xml", "w")
for i in range(len (newarr)):


                f.write(newarr[i])
                f.write("\n")

                



with open("here_is_the list.xml") as my_file:
    newarr = my_file.readlines()



f.close()

#import a

#a.get_names(newarr)
import html_maker
html_maker.main(newarr,wire_id)

