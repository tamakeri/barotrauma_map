import random
from pyvis import network as net
from IPython.display import display, HTML
import re
def main(dugum_array,wire_array):



    def generate_color():
        return '#%06x' % random.randint(0, 0xFFFFFF)

    g_complete =net.Network(height='500px',width='900px',
                bgcolor='black',font_color="red",notebook=True,
                heading="A Complete Networkx Graph",directed=True)

    colors=[]

    import re



    patern_ident="(identifier=\"([A-Za-z0-9]+)\" ID=\"([0-9]*)\" )" #get group 2 3
    patern_name="(<[A-Za-z0-9]+ name=\"(.*)\">)" #get group 2
    patern_link="(<link w=\"([0-9]*)\" i=\"([0-9]*)\" \/>)" #get group 23
    
    temp_input=""
    temp_link=0
    def add_compenent():
        states=0
        with open("here_is_the list.xml") as file:
                for line in file:
                    line=str(line)
                    state_found_id=re.search(patern_ident,line);     state_found_name=re.search(patern_name,line);      state_found_link=re.search(patern_link,line)
                    if state_found_id!=None:states=1
                    if state_found_name!=None:states=2
                    if state_found_link!=None:states=3
                    match states:
                        
                        case 1:#idnetfiear  and id
                            #add the node
                            temp_link=state_found_id.group(3)
                            c = generate_color()
                            while(c in colors):
                                c = generate_color()
                            colors.append(c)
                            val = 5
                            b = random.randint(3,5)
                            g_complete.add_node(state_found_id.group(3),label=state_found_id.group(2),color=c,value=val,
                                                title="Hello! I am Node "+str(state_found_id.group(2)),borderWidth=b)
                        case 2:#input/autpuname
                            temp_input=state_found_name.group(2)
                        case 3:#linkto  and type
                            #links two nodes
                            if(state_found_link.group(3)=="1"):
                                g_complete.add_edge(temp_link,state_found_link.group(2), label=temp_input)
                            else:
                                g_complete.add_edge(state_found_link.group(2),temp_link, label=temp_input)
                            pass
                        case 0:
                            pass
                    states=0
                    
                    


            

    def wire_add(wire_sıra):
        for sayac in range(len(wire_sıra)):  
            c = generate_color()
            while(c in colors):
                c = generate_color()
            colors.append(c)
            val = 5
            b = random.randint(3,5)
            a2=re.search("([A-Za-z]+)  ([0-9]+)",wire_sıra[sayac])
            g_complete.add_node(a2.group(2),label=a2.group(1),color=c,value=val,
                                title="Hello! I am Node "+a2.group(1),borderWidth=b)
            

    
    wire_add(wire_array) #tamamlandı
    add_compenent()

    g_complete.show_buttons(['physics'])

    g_complete.show('A_Complete_Networkx_Graph.html')
    display(HTML('A_Complete_Networkx_Graph.html'))