import os
import re
os_command_for_extraction='\"C:\\Program Files\\7-Zip\.\\7z.exe\" e *.sub'
list1 = os.listdir()
result=os.system(os_command_for_extraction)

list2 = os.listdir()
s = set(list1)
file_needed = [x for x in list2 if x not in s]


f = open(file_needed[0], "r")

s=""
for i in f:
    s=s+i
flag=False
temp_array_for_inserting_items="\t"
temp_array=[]

f.close()
os_command_for_deleting="del "+file_needed[0]
os.system(os_command_for_deleting)

# this block is for adding to array
for i in range(len (s)):
        if(s[i:i+7]=="</Item>"): 
            flag=False
            temp_array_for_inserting_items=temp_array_for_inserting_items+s[i:i+7]+"\n"
            temp_array.append(temp_array_for_inserting_items)
            temp_array_for_inserting_items="\t"
        if(s[i:i+10]=="<Item name"): 
                flag=True
        if (flag):
            temp_array_for_inserting_items=temp_array_for_inserting_items+s[i]
        








# this block is not needed anym ore


# needd to make new arr


wire_id=[]
wire_reg="identifier=\"([a-z]*wire)\" ID=\"([0-9]*)\""
# this block for getting the id's  and names

for i in range(len (temp_array)):
        a=re.search(wire_reg, temp_array[i])
        if(a!=None):
            b=a.group(1)+"  "+a.group(2)
            
            wire_id.append(b)








final_array=[]

name_id="(identifier=\"[A-Za-z0-9]+\" ID=\"[0-9]+\" )"
links="(<[A-Za-z0-9]+ w=\"[0-9]+\" i=\"[0-9]+\" \/>)"
some_flag=False

for i in range(len (temp_array)):
        some_flag=False
        if(re.findall(name_id, temp_array[i])!=[] and re.findall(links, temp_array[i])!=[]):
            ident_name=re.search(name_id, temp_array[i])
            final_array.append(ident_name.group(1))
            some_flag=True

        else:some_flag=False
        temp=""
        #upper condition must bew met to desceond into loop
        flagone=False
        flagtwo=False
        if(some_flag):
            a=str (temp_array[i])
            b=a.split("\n")
            flagone=False
            flagtwo=False

            #this whole for loop loooking for input/output with links
            for i in range (len(b)):

                if((b[i].find("<output") >0 or b[i].find("<input")>0) and b[i].find("/>")<1):
                    flagone=True
                    temp=""
                    #start over if found

                if(b[i].find("</output") >0 or b[i].find("</input")>0):
                    flagtwo=True
                    #found end

                if(flagone):
                    temp=temp+b[i]
                if(flagone and flagtwo):

                    into=temp.split(">")
                    for i in range(len(into)-1):
                        a=(str(into[i]))
                        if(len(a)>0):
                            a=a+">"

                        final_array.append(a)
                        #append it and reset
                    flagone=False;flagtwo=False




f = open("wires.xml", "w")
for i in range(len (wire_id)):

    f.write(str(wire_id[i]))
    f.write("\n")
f.close()


f = open("here_is_the list.xml", "w")
for i in range(len (final_array)):


                f.write(final_array[i])
                f.write("\n")

                

#this is a mockery of my self  i dare not touch  these two

with open("here_is_the list.xml") as my_file:
    final_array = my_file.readlines()



f.close()


import html_maker
html_maker.main(final_array,wire_id)