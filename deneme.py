import random
from pyvis import network as net
from IPython.display import display, HTML

def generate_edge():

    #burası wire lar kime neye gidecek
    #source destitaniton
    
    s = random.randint(1,20)
    d = random.randint(1,20)
    return (s,d)

def generate_size_node():
    # boncuk büyüklük
    v = random.randint(5,20)
    return v

def generate_color():
    return '#%06x' % random.randint(0, 0xFFFFFF)

g_complete =net.Network(height='600px',width='50%',
            bgcolor='white',font_color="red",notebook=True,
            heading="A Complete Networkx Graph",directed=True)

colors=[]
#burası nokta ekleme
for dugum_nokta in range(1,45):  
    c = generate_color()
    while(c in colors):
        c = generate_color()
    colors.append(c)
    #renk seçmi
    val = generate_size_node()
    #boyut seçimi
    b = random.randint(3,5)
    #burası özellikleri
    g_complete.add_node(dugum_nokta,label=str(dugum_nokta),color=c,value=val,
                        title="Hello! I am Node "+str(dugum_nokta),borderWidth=b)
    
i=0
chosen_set = []

#burası  arrow
while(i!=20):
    eg = generate_edge()
    if(eg[0]!=eg[1] and not (eg in chosen_set)):
        chosen_set.append(eg)
        g_complete.add_edge(eg[0],eg[1])
        i+=1

g_complete.show_buttons(['physics'])

g_complete.show('A_Complete_Networkx_Graph.html')
display(HTML('A_Complete_Networkx_Graph.html'))