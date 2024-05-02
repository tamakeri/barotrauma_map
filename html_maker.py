import random
from pyvis import network as net
from IPython.display import display, HTML
import re
def main(dugum_array,wire_array):

    def yol():
        #burası wire lar kime neye gidecek
        #source destitaniton
        
        s = random.randint(1,20)
        d = random.randint(1,20)
        return (s,d)

    def buyukluk():
        # boncuk büyüklük
        v =5
        return v

    def generate_color():
        return '#%06x' % random.randint(0, 0xFFFFFF)

    g_complete =net.Network(height='600px',width='50%',
                bgcolor='black',font_color="red",notebook=True,
                heading="A Complete Networkx Graph",directed=True)

    colors=[]
    #burası nokta ekleme
    import re
    def node_adet(dugum_array):
        say=0
        
        for i in range(len(dugum_array)):
            if(re.findall("identifier=\"[A-Za-z0-9]+\" ID=\"[0-9]+\"",str(dugum_array[i]))!=[]):   
                say=say+1
        return say
    def wire_adet(wire):
        
        return len(wire)


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
                    

    def node_Add(array_sıra):
        for sayac in range(node_adet(array_sıra)):  
            c = generate_color()
            while(c in colors):
                c = generate_color()
            colors.append(c)
            #renk seçmi
            val = buyukluk()
            #boyut seçimi
            b = random.randint(3,5)
            #bboş iş
            
            g_complete.add_node(array_sıra[sayac],label=str(sayac),color=c,value=val,
                                title="Hello! I am Node "+str(sayac),borderWidth=b)
            





    def wire_add(wire_sıra):
        for sayac in range(wire_adet(wire_sıra)):  
            c = generate_color()
            while(c in colors):
                c = generate_color()
            colors.append(c)
            #renk seçmi
            val = buyukluk()
            #boyut seçimi
            b = random.randint(3,5)
            #bboş iş



            a=re.search("([A-Za-z]+)  ([0-9]+)",wire_sıra[sayac])
            print(a.group(1))
            print(a.group(2))
            g_complete.add_node(a.group(2),label=a.group(1),color=c,value=val,
                                title="Hello! I am Node "+a.group(1),borderWidth=b)
            
    #node_Add(dugum_array)
    wire_add(wire_array)
    i=0
    chosen_set = []

    #burası  arrow
    while(i!=20):
        eg = yol()
        if(eg[0]!=eg[1] and not (eg in chosen_set)):
            chosen_set.append(eg)
            # change label for penis
            g_complete.add_edge(eg[0],eg[1], label='5')
            i+=1

    g_complete.show_buttons(['physics'])

    g_complete.show('A_Complete_Networkx_Graph.html')
    display(HTML('A_Complete_Networkx_Graph.html'))