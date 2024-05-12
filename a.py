import re

txt = "The   rain in Spain rain  rainarain"



x=True
end=0
while x:    
        a=txt[end:len(txt)]
        y=re.search("rain",a)
        if(y==None or y==''):
            
            x=False

        else:

        

            end=int(y.end())
            print(end)
                