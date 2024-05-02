import random
from pyvis import network as net
from IPython.display import display, HTML
def main(f):
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
                bgcolor='white',font_color="red",notebook=True,
                heading="A Complete Networkx Graph",directed=True)

    colors=[]
    #burası nokta ekleme
    import re

    def adet(f):
        say=0
        
        for i in range(len(f)):
            if(re.findall("identifier=\"[A-Za-z0-9]+\" ID=\"[0-9]+\"",str(f[i]))!=[]):   
                say=say+1
        return say
        



    for dugum_nokta in range(adet(f)):  
        c = generate_color()
        while(c in colors):
            c = generate_color()
        colors.append(c)
        #renk seçmi
        val = buyukluk()
        #boyut seçimi
        b = random.randint(3,5)
        #bboş iş
        
        g_complete.add_node(dugum_nokta,label=str(dugum_nokta),color=c,value=val,
                            title="Hello! I am Node "+str(dugum_nokta),borderWidth=b)
        
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